import openai
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

openai.api_key = "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"

class ChatRequest(BaseModel):
    message: str
    conversation_id: str = None

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post("/chat")
async def chat(request: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )
    return {"message": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)