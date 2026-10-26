from fastapi import FastAPI
from pydantic import BaseModel

from personal_assistant.assistant.service import AssistantService
from personal_assistant.config.settings import settings
from personal_assistant.llm.ollama import OllamaLLM

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


llm = OllamaLLM()
assistant = AssistantService(llm=llm)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    response = assistant.chat(request.message)

    return ChatResponse(response=response)
