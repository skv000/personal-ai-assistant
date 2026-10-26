from ollama import Client

from personal_assistant.config.settings import settings
from personal_assistant.llm.base import LLM


class OllamaLLM(LLM):
    """Ollama-backed LLM implementation."""

    def __init__(
        self,
        model: str | None = None,
        host: str | None = None,
    ) -> None:
        self.model = model or settings.llm_model
        self.client = Client(host=host or settings.ollama_host)

    def generate(self, prompt: str) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]
