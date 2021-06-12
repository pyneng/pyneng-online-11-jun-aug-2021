import sys
import subprocess
import re
import os
from pprint import pprint
from collections import defaultdict
import tempfile
import json
import pathlib
from getpass import getpass
import stat
import shutil
from datetime import datetime, timedelta
from glob import glob


import click
import yaml
import pytest
from pytest_jsonreport.plugin import JSONReport
import requests
import github


task_dirs = [
    "04_data_structures",
    "05_basic_scripts",
    "06_control_structures",
    "07_files",
    "09_functions",
    "11_modules",
    "12_useful_modules",
    "15_module_re",
    "17_serialization",
    "18_ssh_telnet",
    "19_concurrent_connections",
    "20_jinja2",
    "21_textfsm",
    "22_oop_basics",
    "23_oop_special_methods",
    "24_oop_inheritance",
    "25_db",
    "task_25_1",
    "task_25_2",
    "task_25_3",
    "task_25_4",
    "task_25_5",
    "task_25_5a",
    "task_25_6",
]


class PynengError(Exception):
    """
    Ошибка в использовании/работе скрипта pyneng
    """


def red(msg):
    return click.style(msg, fg="red")


def green(msg):
    return click.style(msg, fg="green")


def exception_handler(exception_type, exception, traceback):
    """
    sys.excepthook для отключения traceback по умолчанию
    """
    print(f"\n{exception_type.__name__}: {exception}\n")


class CustomTasksType(click.ParamType):
    """
    Класс создает новый тип для click и преобразует
    допустимые варианты строк заданий в отдельные файлы тестов.

    Кроме того проверяет есть ли такой файл в текущем каталоге
    и оставляет только те, что есть.
    """

    def convert(self, value, param, ctx):
        regex = (
            r"(?P<all>all)|"
            r"(?P<number_star>\d\*)|"
            r"(?P<letters_range>\d[a-i]-[a-i])|"
            r"(?P<numbers_range>\d-\d)|"
            r"(?P<single_task>\d[a-i]?)"
        )
        current_chapter = current_dir_name()
        if current_chapter not in task_dirs:
            task_dirs_line = "\n    ".join(
                [d for d in task_dirs if not d.startswith("task")]
            )
            self.fail(
                red(
                    f"\nСкрипт нужно вызывать из каталогов с заданиями:"
                    f"\n    {task_dirs_line}"
                )
            )

        tasks_list = re.split(r"[ ,]+", value)
        if "25" in current_chapter:
            return {25: tasks_list}

        current_chapter = current_chapter_id()
        test_files = []
        for task in tasks_list:
            match = re.fullmatch(regex, task)
            if match:
                if task == "all":
                    return value
                else:
                    if match.group("letters_range"):
                        task = f"{task[0]}[{task[1:]}]"  # convert 1a-c to 1[a-c]
                    elif match.group("numbers_range"):
                        task = f"[{task}]"  # convert 1-3 to [1-3]

                    test_files += glob(f"test_task_{current_chapter}_{task}.py")
            else:
                self.fail(
                    red(
                        f"Данный формат не поддерживается {task}. "
                        "Допустимые форматы: 1, 1a, 1b-d, 1*, 1-3"
                    )
                )
        return test_files


def call_command(command, verbose=True, return_stdout=False, return_stderr=False):
    """
    Функция вызывает указанную command через subprocess
    и выводит stdout и stderr, если флаг verbose=True.
    """
    result = subprocess.run(
        command,
        shell=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    std = result.stdout
    stderr = result.stderr
    if return_stdout:
        return std
    if return_stderr:
        return result.returncode, stderr
    if verbose:
        print("#" * 20, command)
        if std:
            print(std)
        if stderr:
            print(stderr)
    return result.returncode


def post_comment_to_last_commit(msg, repo, delta_days=14):
    """
    Написать комментарий о сдаче заданий в последнем коммите.
    Комментарий пишется через Github API.

    Для работы функции должен быть настроен git.
    Функция пытается определить имя пользователя git из вывода git config --list,
    Если это не получается, запрашивает имя пользователя.

    Пароль берется из переменной окружения GITHUB_PASS или запрашивается.
    """
    token = os.environ.get("GITHUB_TOKEN")
    since = datetime.now() - timedelta(days=delta_days)
    repo_name = f"pyneng/{repo}"

    try:
        g = github.Github(token)
        repo_obj = g.get_repo(repo_name)
    except github.GithubException:
        raise PynengError(
            red("Аутентификация по токену не прошла. Задание не сдано на проверку")
        )
    else:
        commits = repo_obj.get_commits(since=since)

        try:
            last = commits[0]
        except IndexError:
            print("За указанный период времени не найдено коммитов")
        else:
            last.create_comment(msg)


def send_tasks_to_check(passed_tasks):
    """
    Функция отбирает все задания, которые прошли
    тесты при вызове pyneng, делает git add для файлов заданий,
    git commit с сообщением какие задания сделаны
    и git push для добавления изменений на Github.
    После этого к этому коммиту добавляется сообщение о том,
    что задания сдаются на проверку с помощью функции post_comment_to_last_commit.
    """
    ok_tasks = [test.replace("test_", "") for test in passed_tasks]
    tasks_num_only = sorted(
        [task.replace("task_", "").replace(".py", "") for task in ok_tasks]
    )
    message = f"Сделаны задания {' '.join(tasks_num_only)}"

    for task in ok_tasks:
        call_command(f"git add {task}")
        # добавление шаблонов для заданий jinja, textfsm
        if "20" in task or "21" in task:
            call_command("git add templates")
    call_command(f'git commit -m "{message}"')
    call_command("git push origin main")

    git_remote = call_command("git remote -v", return_stdout=True)
    repo_match = re.search(r"online-\d+-\w+-\w+", git_remote)
    if repo_match:
        repo = repo_match.group()
    else:
        raise PynengError(
            red(
                "Не найден репозиторий online-11-имя-фамилия. "
                "pyneng надо вызывать в репозитории подготовленном для курса."
            )
        )
    post_comment_to_last_commit(message, repo)


def dummy_send_tasks_to_check(tasks):
    """
    Функция делает
    git add .
    git commit
    git push
    для добавления изменений на Github.
    В коммит добавляются всеефайлы в текущем каталоге.

    После этого к этому коммиту добавляется сообщение о том,
    что задания сдаются на проверку с помощью функции post_comment_to_last_commit.
    """
    message = f"Сделаны задания 25 {' '.join(tasks)}"

    call_command(f"git add .")
    call_command(f'git commit -m "{message}"')
    call_command("git push origin main")

    git_remote = call_command("git remote -v", return_stdout=True)
    repo_match = re.search(r"online-\d+-\w+-\w+", git_remote)
    if repo_match:
        repo = repo_match.group()
    else:
        raise PynengError(
            red(
                "Не найден репозиторий online-11-имя-фамилия. "
                "pyneng надо вызывать в репозитории подготовленном для курса."
            )
        )
    post_comment_to_last_commit(message, repo)


def current_chapter_id():
    """
    Функция возвращает номер текущего раздела, где вызывается pyneng.
    """
    pth = str(pathlib.Path().absolute())
    last_dir = os.path.split(pth)[-1]
    current_chapter = int(last_dir.split("_")[0])
    return current_chapter


def current_dir_name():
    pth = str(pathlib.Path().absolute())
    current_chapter_name = os.path.split(pth)[-1]
    return current_chapter_name


def parse_json_report(report):
    """
    Отбирает нужные части из отчета запуска pytest в формате JSON.
    Возвращает список тестов, которые прошли.
    """
    if report and report["summary"]["total"] != 0:
        all_tests = defaultdict(list)
        summary = report["summary"]

        test_names = [test["nodeid"] for test in report["collectors"][0]["result"]]
        for test in report["tests"]:
            name = test["nodeid"].split("::")[0]
            all_tests[name].append(test["outcome"] == "passed")
        all_passed_tasks = [name for name, outcome in all_tests.items() if all(outcome)]
        return all_passed_tasks
    else:
        return []


def copy_answers(passed_tasks):
    """
    Функция клонирует репозиторий с ответами и копирует ответы для заданий,
    которые прошли тесты.
    """
    pth = str(pathlib.Path().absolute())
    current_chapter_name = os.path.split(pth)[-1]
    current_chapter_number = int(current_chapter_name.split("_")[0])

    homedir = pathlib.Path.home()
    os.chdir(homedir)
    returncode, stderr = call_command(
        "git clone --depth=1 https://github.com/natenka/pyneng-answers",
        verbose=False,
        return_stderr=True,
    )
    if returncode == 0:
        os.chdir(f"pyneng-answers/answers/{current_chapter_name}")
        copy_answer_files(passed_tasks, pth)
        print(
            green(
                "\nОтветы на задания, которые прошли тесты "
                "скопированы в файлы answer_task_x.py\n"
            )
        )
        os.chdir(homedir)
        shutil.rmtree("pyneng-answers", onerror=remove_readonly)
    else:
        if "could not resolve host" in stderr.lower():
            raise PynengError(
                red(
                    "Не получилось скопировать ответы. Возможно нет доступа в интернет?"
                )
            )
        else:
            raise PynengError(red(f"Не получилось скопировать ответы. {stderr}"))
    os.chdir(pth)


def remove_readonly(func, path, _):
    """
    Вспомогательная функция для Windows, которая позволяет удалять
    read only файлы из каталога .git
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def copy_answer_files(passed_tasks, pth):
    """
    Функция копирует ответы для указанных заданий.
    """
    for test_file in passed_tasks:
        task_name = test_file.replace("test_", "")
        answer_name = test_file.replace("test_", "answer_")
        if not os.path.exists(f"{pth}/{answer_name}"):
            call_command(
                f"cp {task_name} {pth}/{answer_name}",
                verbose=False,
            )


@click.command(
    context_settings=dict(
        ignore_unknown_options=True, help_option_names=["-h", "--help"]
    )
)
@click.argument("tasks", default="all", type=CustomTasksType())
@click.option(
    "--disable-verbose", "-d", is_flag=True, help="Отключить подробный вывод pytest"
)
@click.option(
    "--answer",
    "-a",
    is_flag=True,
    help=(
        "Скопировать ответы для заданий, которые "
        "прошли тесты. При добавлении этого флага, "
        "не выводится traceback для тестов."
    ),
)
@click.option(
    "--check",
    "-c",
    is_flag=True,
    help=(
        "Сдать задания на проверку. "
        "При добавлении этого флага, "
        "не выводится traceback для тестов."
    ),
)
@click.option("--debug", is_flag=True, help="Показывать traceback исключений")
def cli(tasks, disable_verbose, answer, check, debug):
    """
    Запустить тесты для заданий TASKS. По умолчанию запустятся все тесты.

    Примеры запуска:

    \b
        pyneng            запустить все тесты для текущего раздела
        pyneng 1,2a,5     запустить тесты для заданий 1, 2a и 5
        pyneng 1,2a-c,5   запустить тесты для заданий 1, 2a, 2b, 2c и 5
        pyneng 1,2*       запустить тесты для заданий 1, все задания 2 с буквами и без
        pyneng 1,3-5      запустить тесты для заданий 1, 3, 4, 5
        pyneng 1-5 -a     запустить тесты и записать ответы на задания,
                          которые прошли тесты, в файлы answer_task_x.py
        pyneng 1-5 -c     запустить тесты и сдать на проверку задания,
                          которые прошли тесты.
        pyneng -a -c      запустить все тесты, записать ответы на задания
                          и сдать на проверку задания, которые прошли тесты.

    Флаг -d отключает подробный вывод pytest, который включен по умолчанию.
    Флаг -a записывает ответы в файлы answer_task_x.py, если тесты проходят.
    Флаг -c сдает на проверку задания (пишет комментарий на github)
    для которых прошли тесты.
    Для сдачи заданий на проверку надо сгенерировать токен github.
    Подробнее в инструкции: https://pyneng.github.io/docs/pyneng-prepare/
    """
    token_error = red(
        "Для сдачи заданий на проверку надо сгенерировать токен github. "
        "Подробнее в инструкции: https://pyneng.github.io/docs/pyneng-prepare/"
    )

    if not debug:
        sys.excepthook = exception_handler

    json_plugin = JSONReport()
    pytest_args_common = ["--json-report-file=none", "--disable-warnings"]

    if disable_verbose:
        pytest_args = [*pytest_args_common, "--tb=short"]
    else:
        pytest_args = [*pytest_args_common, "-vv"]

    # если добавлен флаг -a или -c нет смысла выводить traceback,
    # так как скорее всего задания уже проверены предыдущими запусками.
    if answer or check:
        pytest_args = [*pytest_args_common, "--tb=no"]

    # запуск pytest
    if tasks == "all":
        pytest.main(pytest_args, plugins=[json_plugin])
    elif type(tasks) == dict:  # 25_db
        print(green("Для заданий 25го раздела нет тестов"))
    else:
        pytest.main(tasks + pytest_args, plugins=[json_plugin])

    # для заданий 25го раздела делается глупое добавление всех файлов
    if type(tasks) == dict:  # 25_db
        if answer:
            raise PynengError(
                red(
                    "Задания 25_db без автоматических ответов. Проверка выполняется "
                    "вручную и вместе с проверкой выкладываются ответы"
                )
            )
        if check:
            token = os.environ.get("GITHUB_TOKEN")
            if not token:
                raise PynengError(token_error)
            dummy_send_tasks_to_check(tasks[25])
    else:
        # получить результаты pytest в формате JSON
        passed_tasks = parse_json_report(json_plugin.report)

        if passed_tasks:
            # скопировать ответы в файлы answer_task_x.py
            if answer:
                copy_answers(passed_tasks)

            # сдать задания на проверку через github API
            if check:
                token = os.environ.get("GITHUB_TOKEN")
                if not token:
                    raise PynengError(token_error)
                send_tasks_to_check(passed_tasks)


if __name__ == "__main__":
    cli()
