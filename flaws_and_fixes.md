#### SQL Injection

##### Description of flaw:
On the 'phone directory' it is possible to get more information than what
is given (or even better delete or update the database).
The web application uses the user input as the query without validating it.
To test that injection works try ``jaime" or "1" ="1``

##### How to fix it:
The fix is, of course, to validate or sanitize user input;
This can be done by parameterized queries. By 'parameterizing' a query,
extra or invalid input is stripped away.
An example fix is commented in the code (file 'model.py').


#### Cross-Site Request Forgery

##### Description of flaw:
The flaw here is simple because none of the forms in the application
use a CSRF token. In the test scenario,
we can imagine that the feedback form is important and
we wouldn't want an adversary to fill the forms in the
place of a user.

##### How to fix it:
In the Flask web framework,
to use CSRF tokens we use extensions such as 'Flask-WTF'
to help us easily implement them. The fix is shown in the code
in files '\_\_init__.py' and 'form_csrf.html' commented.


#### Cross-Site Scripting

##### Description of flaw:
In our made-up forum or comment posting thread
we can test for XSS vulnerability by adding a post using
any HTML tags, for example ``<b>Test</b>``,
we'll notice the HTML code is rendered.
This is, of course, is not enough to tell us that the
web application has an XSS vulnerability; next,
we'll input ``<script>alert(43-1)</script>`` and
you'll notice that the javascript code is run.

##### How to fix it:
By default Flask's templating engine jinja2
escapes HTML, therefore, this vulnerability is not there
by default, it has to be enabled. In our scenario,
we could imagine a forgetful dev testing something
and forgetting to revert to the default behavior.
The fix is commented in the file 'xss.html'.


#### Broken Authentication

##### Description of flaw:
The web application does not hash and salt passwords;
By using the previously mentioned SQL injection vulnerability,
one can also get these passwords.
The passwords are also weak and can be easily brute-forced
(the admin password can be brute-forced in 10 seconds using
the most common passwords dictionary).

##### How to fix it:
Salt and hash passwords; Even better,
use a well-known library or module (for example Bcrypt)
instead of implementing your own salt & hash scheme.
The other fix is to force a minimum password length
(for now the recommended is >= 6);
additional info https://imgs.xkcd.com/comics/password_strength.png

#### Broken Access Control

##### Description of flaw:
By using a crawler or just manually investigating you'll notice the
endpoint '/admin'; By going to that URL you'll notice that you got
in without providing any credentials whatsoever.
In the admin panel you can do a lot of interesting stuff.
The web application does not check your credentials when
you go to that URL and this is an access control vulnerability
as there exists a login form that was bypassed.

##### How to fix it:
The fix for broken access control is to check whether whoever is
trying to access a sensitive resource is authorized to do so.
In the code, the fix is in the file '\_\_init\_\_.py'
line 11 and line 38
(which means line 39 must be commented if you want to try the fix it out).
It should be noted while this fix works,
a better solution is to completely block the view and
log some info about the event (more info at https://flask-admin.readthedocs.io/en/latest/introduction/).

#### Other small stuff
##### Problem:
The web application has permanent sessions unless the user logs out
##### Fix:
Implement a session lifetime; The more sensitive the web application,
the less the web application session time.

##### Problem:
Embedding security keys in code
##### Fix:
A better way to import security keys is by using environment variables
or from a file outside the git directory.
Example https://pypi.org/project/python-dotenv/