# cybersecuritybase-project
Project with the goal of creating a vulnerable web application
and provide fixes for it.

### Installation instructions:
#### Ubuntu (tested on 18.04.3)
Python 3 is usually installed by default, check with
 ``$ python3 --version``,
Python version should be 3.6+

```
$
```

#### Windows (tested on build 18362)
Make sure you have git and python 3.6+ installed, if you don't:
https://git-scm.com/download/win
https://www.python.org/downloads/windows/
Alternatively, get Python 3 from the Windows store

Open cmd, Powershell or git bash:

```
git clone https://github.com/nicolaskyejo/cybersecuritybase-project.git
cd cybersecuritybase-project
python -m venv venv	
venv\Scripts\activate.bat
pip install -r requirements.txt
python app_name.py
```

#### MacOS (tested on Catalina)
If you don't have python3 installed, install [Homebrew](https://github.com/Homebrew/install)
first

```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
homebrew install python
```

#### Acknowledgements
* https://flask.palletsprojects.com/en/1.1.x/security/
* https://medium.com/@smirnov.am/securing-flask-web-applications-f877e374b427