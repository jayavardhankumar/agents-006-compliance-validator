from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.config import (
    AMD_BASE_URL,
    AMD_API_KEY,
    MODEL_NAME
)


provider = OpenAIProvider(
    base_url=AMD_BASE_URL,
    api_key=AMD_API_KEY
)

model = OpenAIModel(
    MODEL_NAME,
    provider=provider
)

agent = Agent(model=model)


async def audit_document(prompt):

    result = await agent.run(prompt)

    return result.output