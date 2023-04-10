from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_chat():
    # Test a new conversation
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    # assert response.json() == {"message": "Hi, how can I help you today?"}

    # Test a continued conversation
    conversation_id = "abc123"
    response = client.post("/chat", json={"message": "Can you tell me more about your products?", "conversation_id": conversation_id})
    assert response.status_code == 200
    # assert response.json() == {"message": "Sure, we offer a wide range of products. What specifically are you interested in?"}

    # Test a conversation with invalid conversation ID
    invalid_conversation_id = "xyz789"
    response = client.post("/chat", json={"message": "Hello", "conversation_id": invalid_conversation_id})
    assert response.status_code == 200
    # assert response.json() == {"message": "I'm sorry, I don't recognize that conversation ID. Let's start a new conversation."}
