# Flaskアプリの生成と拡張機能の初期化
from flask import Flask
from .db import init_db

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    # app.pyなどの登録
    from .app import app as blueprint_app
    app.register_blueprint(blueprint_app)

    return app
