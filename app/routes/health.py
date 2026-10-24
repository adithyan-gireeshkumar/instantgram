from flask import Blueprint

health_bp = Blueprint("health", __name__)

@health_bp.get("/")
def home():
    return {
        "application": "Instantgram",
        "status": "running",
        "backend": "Flask",
    }

    @health_bp.get("/health")
    def health_check():
        return {"status": "healthy"},200

        
