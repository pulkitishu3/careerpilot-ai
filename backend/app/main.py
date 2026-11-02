
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CareerPilot AI",
    description="AI-Powered Personal Career Intelligence Platform",
    version="1.0.0"
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
