from client.llm_client import LLMClient
import asyncio

async def main():
    llm_client = LLMClient()
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Can you help me with a question?"},
        ]
        async for event in llm_client.chat_completion(messages, stream=True):
            print(event)
    finally:
        await llm_client.close()

asyncio.run(main())