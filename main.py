from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load marks from file
with open("marks.json", "r") as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = []):
    result = [student_marks.get(n, None) for n in name]
    return {"marks": result}
