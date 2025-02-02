from pydantic import BaseModel, Field
from anthropic import Anthropic
from chat_with_doc.interfaces.llm_api import LlmApi


class AnthropicConfig(BaseModel):
    """Configuration for Anthropic API."""

    api_key: str = Field(..., description="Anthropic API key")
    model: str = Field(default="claude-3-opus-20240229", description="Model to use")
    max_tokens: int = Field(default=1024, description="Maximum tokens in response")
    temperature: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Temperature for response generation"
    )


class AnthropicLlm(LlmApi):
    """Anthropic implementation of the LLM API interface."""

    def __init__(self, config: AnthropicConfig):
        """Initialize Anthropic client with configuration.

        Args:
            config: Configuration for Anthropic API
        """
        self.config = config
        self.client = Anthropic(api_key=config.api_key)

    def query(self, prompt: str) -> str:
        """Send a query to Anthropic's Claude and return the response.

        Args:
            prompt: The input prompt to send to Claude

        Returns:
            str: Claude's response

        Raises:
            Exception: If the API call fails
        """
        try:
            message = self.client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            return message.content[0].text  # type: ignore
        except Exception as e:
            raise Exception(f"Failed to query Anthropic API: {str(e)}")
