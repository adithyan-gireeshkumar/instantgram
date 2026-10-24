from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "development-only-change-me",
    )

    @app.get("/")
    def home():
        return {
            "application": "Instantgram",
            "status": "running",
            "backend": "Flask",
        }

        return app