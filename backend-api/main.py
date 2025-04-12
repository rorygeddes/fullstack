from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import anthropic

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# ✅ Add this block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] if using Create React App
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your existing POST route
class Message(BaseModel):
    name: str

@app.post("/hello")
def say_hello(msg: Message):
    return {"message": f"Hello, {msg.name}!"}
