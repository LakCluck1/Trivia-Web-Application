from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config
from flask_session import Session 

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
sess = Session()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        login_manager.init_app(app)
        sess.init_app(app)
    
    from . import models
    from .routes import main
    app.register_blueprint(main)

    # from app.users.routes import users
    # from app.quiz.routes import quiz
    # from app.home.routes import home
    # app.register_blueprint(users)
    # app.register_blueprint(quiz)
    # app.register_blueprint(home)
    return app
