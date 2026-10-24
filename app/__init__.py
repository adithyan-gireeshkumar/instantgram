
import os

from dotenv import load_dotenv
from flask import Flask

from app.routes.health import health_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "development-only-change-me",
    )

    app.register_blueprint(health_bp)

    return app