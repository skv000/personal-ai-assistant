from personal_assistant.assistant.service import AssistantService
from personal_assistant.llm.base import LLM


class FakeLLM(LLM):
    def generate(self, prompt: str) -> str:
        return f"Fake response to: {prompt}"


def test_assistant_chat() -> None:
    assistant = AssistantService(llm=FakeLLM())

    response = assistant.chat("Hello")

    assert response == "Fake response to: Hello"
