from personal_assistant.llm.base import LLM


class AssistantService:
    """Core application service for the personal AI assistant."""

    def __init__(self, llm: LLM) -> None:
        self.llm = llm

    def chat(self, message: str) -> str:
        return self.llm.generate(message)
