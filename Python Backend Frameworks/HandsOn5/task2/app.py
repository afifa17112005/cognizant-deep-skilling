from flask import Flask
from flask_migrate import Migrate

from config import Config
from models import db
from courses.routes import bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    Migrate(app, db)

    app.register_blueprint(
        bp,
        url_prefix="/api/courses"
    )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)