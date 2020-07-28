from flask_login import LoginManager
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth
from .queries import get_user
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)

    app.register_blueprint(auth)
    login_manager.init_app(app)
    return app

from .models import User
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
