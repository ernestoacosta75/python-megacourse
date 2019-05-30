'''
The __init__.py file assume an specific meaning:
It does that a project inside a folder will be considered
as a Python module.
In this way, we can import the blog module with the string
"import blog" normally.
'''

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav

bootstrap = Bootstrap()
nav = Nav()

def create_app():
    app = Flask(__name__)
    from .main import main as main_bp
    bootstrap.init_app(app)
    nav.init_app(app)
    app.register_blueprint(main_bp)

    return app

