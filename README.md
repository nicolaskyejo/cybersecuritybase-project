# cybersecuritybase-project
Project with the goal of creating a vulnerable web application
and provide [fixes](https://github.com/nicolaskyejo/cybersecuritybase-project/blob/master/flaws_and_fixes.md)
for it.

## Requirements
* Python 3.6 or above


## Installation instructions:

### Using Docker
```docker run -it -p 5000:5000 nicolaskyejo/vulnerableapp```

### Without Docker

#### Ubuntu (tested on 18.04.3)
Python 3 is usually installed by default, check with
 ``$ python3 --version``,
Python version should be 3.6 or above. If the version is not correct, follow the instructions
for your linux distro for installing the newest version of Python.

```
$ git clone https://github.com/nicolaskyejo/cybersecuritybase-project.git
$ cd cybersecuritybase-project
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python run.py
```

#### Windows 10 (tested on build 18362)
Make sure you have git and Python 3.6+ installed, if you don't:
https://git-scm.com/download/win
and
https://www.python.org/downloads/windows/

Alternatively, get Python 3 from the Windows store

Open cmd, Powershell, or git bash:

```
git clone https://github.com/nicolaskyejo/cybersecuritybase-project.git
cd cybersecuritybase-project
python -m venv venv	
```
If using cmd -->``venv\Scripts\activate.bat``,
If using Powershell -->``venv\Scripts\activate.ps1``,
If using git bash -->``$ source venv\Scripts\activate``
```
pip install -r requirements.txt
python run.py
```

#### MacOS (tested on Catalina)
If you don't have Python 3.6 or above installed, install [Homebrew](https://github.com/Homebrew/install)
first
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ homebrew install python
```

The clone the project
```
git clone https://github.com/nicolaskyejo/cybersecuritybase-project.git
cd cybersecuritybase-project
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python run.py
```

#### Acknowledgements
* https://flask.palletsprojects.com/en/1.1.x/security/
* https://medium.com/@smirnov.am/securing-flask-web-applications-f877e374b427
