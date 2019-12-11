import model
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf import CSRFProtect


app = Flask(__name__)
# csrf = CSRFProtect(app)  # csrf tokens disabled globally
app.secret_key = 'bdb92dbe238008edfac05e92412b0c23'  # Another bad practice in security is when you embed security keys
# in your code like this


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/SQL_injection', methods=['GET', 'POST'])
def sql_injection():
    if request.method == 'GET':
        return render_template('form_sql_injection.html')

    first_name = request.form.get('first name')
    if first_name == '':
        flash('Empty search')
        return redirect(url_for('sql_injection'))
    results = model.user_phonenumber_query(first_name.capitalize())
    return render_template('form_sql_injection.html', results=results)


@app.route('/csrf_in_form', methods=['GET', 'POST'])
def csrf():
    if request.method == 'GET':
        return render_template('form_csrf.html')

    return "Feedback noted!"


@app.route('/broken_auth', methods=['GET', 'POST'])
def broken_auth():
    pass


if __name__ == '__main__':
    app.run()
