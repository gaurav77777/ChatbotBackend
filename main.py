from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from local_model import generate_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message")
    reply = generate_reply(message)
    return {"reply": reply}
