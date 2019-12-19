from flask import Flask, session, url_for, redirect
from flask_wtf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# csrf = CSRFProtect()  # csrf tokens disabled globally


# This piece of code inherits ModelView and checks if the user accessing /admin is really admin
# Commented out to show bad security
# class MyModelView(ModelView):
#     def is_accessible(self):
#         return session.get('username') == 'admin'  # give access to admin only
#
#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('main_bp.broken_auth'))


def create_app():
    app = Flask(__name__)
    app.secret_key = 'bdb92dbe238008edfac05e92412b0c23'  # Another bad practice in security is
    # when you embed security keys in your code like this
    # app.config['PERMANENT_SESSION_LIFETIME'] = 120  # session lifetime disabled for showing bad security practice
    app.config['FLASK_ADMIN_SWATCH'] = 'united'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    admin = Admin(app, name='Admin-Panel', template_mode='bootstrap3')
    db.init_app(app)
    # csrf.init_app(app)

    with app.app_context():
        from application.views import main_bp
        from application.model import db_init, User, Comments
        app.register_blueprint(main_bp)

        # admin.add_views(MyModelView(User, db.session), MyModelView(Comments, db.session))  #  For the custom model above
        admin.add_views(ModelView(User, db.session), ModelView(Comments, db.session))
        db.drop_all()
        db_init()  # initialize sql injection db for part 1
        db.create_all()  # initialize db for logins, comments
        db.session.add(Comments(comment=' 🤘🏾🤘🏾 Spaces in code is the way to go. Who uses Tabs 😂😂?'))
        db.session.add(User(username='admin', password='1234'))
        db.session.add(User(username='ducky', password='hunter2'))
        db.session.commit()
        return app
