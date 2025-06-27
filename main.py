from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "It works! Subscribe to my channel if you like this video"}

@app.get("/health")
def health():
    return {"status": "ok"}

class ReverseRequest(BaseModel):
    text: str

@app.post("/reverse")
def reverse(req: ReverseRequest):
    reversed_text = req.text[::-1]
    return {"reversed": reversed_text}
