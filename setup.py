from setuptools import setup

setup(
    name="pyneng",
    version="1.0",
    py_modules=["pyneng"],
    install_requires=[
        "Click",
        "pyyaml",
        "pytest",
        "pytest-clarity",
        "pytest-json-report",
        "requests",
        "PyGithub",
        "six",
    ],
    entry_points="""
        [console_scripts]
        pyneng=pyneng:cli
    """,
)
