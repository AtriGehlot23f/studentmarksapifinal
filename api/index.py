from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks data (make sure marks.json is at root)
MARKS_PATH = os.path.join(os.path.dirname(__file__), '..', 'marks.json')

with open(MARKS_PATH, "r") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {student["name"]: student["marks"] for student in data}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
