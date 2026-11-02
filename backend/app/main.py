from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.database.connection import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router

app = FastAPI(
    title="CareerPilot AI",
    description="AI-Powered Personal Career Intelligence Platform",
    version="1.0.0"
)
app.include_router(
    auth_router,
    prefix="/api/v1"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPilot AI",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CareerPilot Backend"
    }


@app.get("/api/v1/dashboard")
def dashboard():
    return {
        "project": "CareerPilot AI",
        "total_resumes": 0,
        "jobs_matched": 0,
        "skills_identified": 0,
        "interviews_completed": 0
    }
@app.get("/api/v1/database-check")
def database_check():
    try:
        with engine.connect() as connection:
            database_name = connection.execute(
                text("SELECT current_database()")
            ).scalar_one()

        return {
            "status": "success",
            "message": "PostgreSQL connected successfully!",
            "database": database_name
        }

    except SQLAlchemyError as error:
        print("Database connection error:", error)

        raise HTTPException(
            status_code=503,
            detail="Unable to connect to PostgreSQL database."
        )