from .model import user_phonenumber_query, User
from flask import Blueprint, render_template, request, flash, url_for, redirect, session


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main_bp.route('/SQL_injection', methods=['GET', 'POST'])
def sql_injection():
    if request.method == 'GET':
        return render_template('form_sql_injection.html')

    first_name = request.form.get('first name')
    if first_name == '':
        flash('Empty search')
        return redirect(url_for('main_bp.sql_injection'))
    results = user_phonenumber_query(first_name.capitalize())
    return render_template('form_sql_injection.html', results=results)


@main_bp.route('/csrf_in_form', methods=['GET', 'POST'])
def csrf():
    if request.method == 'GET':
        return render_template('form_csrf.html')

    return "Feedback noted!"


@main_bp.route('/broken_auth', methods=['GET', 'POST'])
def broken_auth():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    passwd = request.form.get('password')
    user = User.query.filter_by(username=username, password=passwd).first()
    if user:  # exists
        session['username'] = username
        if session['username'] == 'admin':
            return redirect(url_for('user.index_view'))
        else:
            return redirect(url_for('main_bp.lounge'))

    flash('Incorrect username/password')
    return redirect(url_for('main_bp.broken_auth'))


@main_bp.route('/user_lounge', methods=['GET'])
def lounge():
    if session['username'] is not None:
        return render_template('user.html')
    redirect(url_for('main_bp.broken_auth'))


@main_bp.route('/xss', methods=['GET', 'POST'])
def xss():
    return render_template('xss.html')
