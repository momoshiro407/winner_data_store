from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User


# アプリケーションの初期化
app = Flask(__name__, static_folder='../../frontend/dist/static',
            template_folder='../../frontend/dist')

# SQLAlchemyの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wrdb_admin:wrdb12345@localhost/winner_result_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyとFlask-Migrateの初期化
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
