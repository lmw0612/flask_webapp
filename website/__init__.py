from flask import Flask

def create_app():
    app = Flask(__name__) # Name of the file
    app.config['SECRET_KEY'] = 'test2021'# Configure secret key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app