from abc import ABC, abstractmethod


class LLM(ABC):
    """Abstract interface for language model providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from a prompt."""
        raise NotImplementedError
