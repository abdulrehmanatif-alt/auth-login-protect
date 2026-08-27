import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()


class AuthRequest(BaseModel):
    email: str
    password: str


@app.post("/auth/signup", status_code=201)
def signup(request: AuthRequest):
    response = supabase.auth.sign_up({
        "email": request.email,
        "password": request.password
    })

    return response.model_dump()


@app.post("/auth/login")
def login(request: AuthRequest):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password
        })

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except Exception:
        return {"error": "Invalid login credentials"}


@app.get("/")
def root():
    return {"message": "Server running and connected to Supabase"}