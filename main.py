import os
import openai
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

openai.api_key = os.environ.get('OPENAI_API_KEY')
print(openai.api_key)
class ChatRequest(BaseModel):
    message: str
    conversation_id: str = None

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post("/chat")
async def chat(request: ChatRequest):
    response = openai.Completion.create(
            engine="davinci",
            prompt=f"Conversation with {request.conversation_id}\n\nHuman: {request.message}\nAI:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,)
    return {"message": response.choices[0].text.strip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)