# tau-intro-to-pytest

This repository contains example code for *An Introduction to pytest*,
a [Test Automation University](https://testautomationu.applitools.com/) course
taught by [Andrew "Pandy" Knight](https://twitter.com/AutomationPanda).
This course teaches how to automate test cases in Python using [pytest](https://pytest.org).


## Repository Purpose

The best way to learn pytest is through hands-on coding.
In the first lesson of the course, you will create a new Python project for test cases.
(That project will *not* be the same as this repository.)
Each chapter then introduces new concepts and provides coding instructions for your project.
If you code along with each chapter,
then you will have a complete, functioning test automation project by the end of the course.

This repository provides all example code for the project.
If you get stuck while building your own project,
compare your code to the example code in this repository.
However, try to avoid blindly copying code from the repository into your project.
Take the time to learn the concepts and code presented in each chapter.


## Repository Branches

* `master` contains the README but no example code
* Each `example/*` branch contains chapter-specific example code
* `example/develop` contains the completed example code for the end of the course


## Python Setup

Python setup can be complicated.
This section documents how to set up your machine for Python test automation development.

### Python Installation and Tools

You can complete this course using any OS: Windows, macOS, Linux, etc.

This course requires Python 3.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).
Follow the appropriate installation instructions for your operating system.

You should have intermediate-level Python skills before attempting this course.
Learning the language is always a prerequisite for learning automation.
If you need help learning Python, check out this article:
[How Do I Start Learning Python?](https://automationpanda.com/2020/02/18/how-do-i-start-learning-python/)

You should also have a good Python editor/IDE.
Good choices include [PyCharm](https://www.jetbrains.com/pycharm/)
and [Visual Studio Code](https://code.visualstudio.com/docs/languages/python).

You will also need [Git](https://git-scm.com/) if you want to clone this repository locally.
If you are new to Git, [try learning the basics](https://try.github.io/).

### Python Installation Troubleshooting

Unfortunately, installing Python properly can be complicated,
especially if Python was previously installed on your machine.
To verify your Python installation, enter `python --version` at the command line.
You should see the proper version printed.

If the `python` command doesn't work or doesn’t print the expected version number,
then try using the `python3` command instead.
If that still doesn't work,
then the correct Python installation might not be included in your system path.
Find the directory into which Python was installed,
manually add it to the system path,
relaunch the command line,
and try running Python again.

* [System Path Instructions for Windows](https://geek-university.com/python/add-python-to-the-windows-path/)
* [System Path Instructions for macOS](https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac)
* [System Path Instructions for Linux](https://www.computerhope.com/issues/ch001647.htm)

### Python Packages

This course will use a handful of third-party packages:

* pytest
* pytest-cov
* pytest-html
* pytest-xdist
* requests

These packages are *not* part of Python's standard library.
They must be installed separately using `pip`, the standard Python package installer.
You can install them all before you create your test project,
or you can install them as you complete each chapter in the course.

To install each package, enter `pip install <package-name>` at the command line.
For example: `pip install pytest`.
If you already have a package installed but need to upgrade its version,
run `pip install --upgrade <package-name>`.

Please note that if you need to use the `python3` command to run Python,
then you might also need to use the `pip3` command in lieu of `pip`.

### Virtual Environments

Running `pip install` will install the pytest package globally for the whole system.
Installing Python packages globally is okay for this course,
but it typically isn't a best practice in the "read world."
Instead, each project should manage its own dependencies locally using a virtual environment.
Virtual environments let projects avoid unnecessary dependencies and version mismatches.

For simplicity, this course will not use or teach virtual environments.
If you would like to learn virtual environments on your own, then RealPython's article
[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
is an excellent place to start.

### Course Versions

This course was developed and tested using the following versions:

* macOS 10.14.6
* Python 3.8.1
* pytest 5.4.3
* pytest-cov 2.10.0
* pytest-html 2.1.1
* pytest-xdist 1.32.0
* requests 2.23.0


## Running Tests

To run the example tests from the command line, run `python -m pytest` from the project root directory.
This command will discover and run all tests in the project.

You can also run tests using the shorter `pytest` command.
However, I recommend always using the lengthier `python -m pytest` command.
The lengthier command automatically adds the current directory to `sys.path`
so that all modules in the project can be discovered.

The pytest command has several command line options.
Course material will cover many of them.
Check out the [Usage and Invocations](https://docs.pytest.org/en/stable/usage.html) page
for complete documentation.

*Warning:*
If you attempt to run tests from this example project,
make sure to checkout the correct branch first!


## Additional Resources

Python links:

* [Python.org](https://www.python.org/)
* [pytest.org](https://docs.pytest.org/)
* [How Do I Start Learning Python?](https://automationpanda.com/2020/02/18/how-do-i-start-learning-python/)
* [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)
* [Automation Panda's Python Page](https://automationpanda.com/python/)

Books:

* [Python Testing with pytest](https://pragprog.com/titles/bopytest/) by Brian Okken
* [pytest Quick Start Guide](https://www.packtpub.com/web-development/pytest-quick-start-guide) by Bruno Oliveira
* [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) by Harry J.W. Percival

Related TAU courses:

* [Python Programming](https://testautomationu.applitools.com/python-tutorial/)
* [Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
* [Behavior-Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
* [Automated Visual Testing with Python](https://testautomationu.applitools.com/visual-testing-python/)


## About the Author

This course was written and delivered by **Andrew Knight** (aka *Pandy*), the "Automation Panda".
Andy is a Pythonista who specializes in testing and automation.

* Twitter: [@AutomationPanda](https://twitter.com/AutomationPanda)
* Blog: [AutomationPanda.com](https://automationpanda.com/)
* LinkedIn: [andrew-leland-knight](https://www.linkedin.com/in/andrew-leland-knight/)
