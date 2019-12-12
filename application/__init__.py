from flask import Flask
from flask_wtf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# csrf = CSRFProtect()  # csrf tokens disabled globally


def create_app():
    app = Flask(__name__)
    app.secret_key = 'bdb92dbe238008edfac05e92412b0c23'  # Another bad practice in security is
    # when you embed security keys in your code like this
    app.config['FLASK_ADMIN_SWATCH'] = 'united'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    admin = Admin(app, name='Admin-Panel', template_mode='bootstrap3')
    db.init_app(app)
    # csrf.init_app(app)

    with app.app_context():
        from application.views import main_bp
        from application.model import User, db_init
        app.register_blueprint(main_bp)

        admin.add_view(ModelView(User, db.session))
        db_init()  # initialize sql injection db for part 1
        db.create_all()  # initialize db for logins
        if User.query.all() is not None:
            User.query.delete()  # delete previous users
        db.session.add(User(username='admin', password='1234'))
        db.session.add(User(username='ducky', password='hunter2'))
        db.session.commit()
        return app
