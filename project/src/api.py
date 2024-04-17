from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from Engine import Engine

load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Authorization", "Content-Type"]
)

engine = Engine(mode="api")

@app.get("/api/status")
def getStatus():
    return {"connected": True}

@app.get("/api/tokenize/{data}")
def tokenize(data: str):
    token = engine.tokenizeData(data)
    if token == None:
        raise HTTPException(status_code=400, detail="Data too long")
    return {"token": token}

@app.get("/api/untokenize/{token}")
def untokenize(token: str):
    data = engine.untokenizeData(token)
    if data == None:
        raise HTTPException(status_code=404, detail="Token not found")
    return {"data": data}

@app.get("/api/generate/{number}")
def generate(number: int):
    result = engine.generateToken(number)
    if result == None:
        raise HTTPException(status_code=500, detail="Token generation error")
    return {"number_generated": result}