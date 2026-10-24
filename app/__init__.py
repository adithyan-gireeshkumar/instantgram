from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'development_only_change_me')

    @app.get('/')
    def home():
        return {"application " : "Social ai agent",
                "status" : "running",
                "backend" : "flask",
                }

                return app

                