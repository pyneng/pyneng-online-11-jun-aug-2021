from setuptools import setup

setup(
    name="pyneng",
    version="1.0",
    py_modules=["pyneng"],
    install_requires=[
        "Click",
        "pyyaml",
        "pytest",
        "pytest-clarity==0.3.0a0",
        "pytest-json-report",
        "requests",
        "PyGithub",
        "six",
        "jinja2",
        "textfsm",
    ],
    entry_points="""
        [console_scripts]
        pyneng=pyneng:cli
    """,
)
