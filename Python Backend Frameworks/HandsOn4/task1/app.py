from flask import Flask
from config import Config
from courses.routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(bp, url_prefix="/api/courses")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)