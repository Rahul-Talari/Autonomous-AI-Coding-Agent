# Tech Stack

## Language and tooling

| Technology | Version | Purpose |
| --- | --- | --- |
| Python | 3.14 or later | Application language |
| uv | 0.12.5 | Manages the virtual environment, dependencies, and the lockfile, and runs the app |
| Git | Not pinned | Version control |

## LLM integration

| Item | Value |
| --- | --- |
| Gateway | [OpenRouter](https://openrouter.ai) |
| API base URL | `https://openrouter.ai/api/v1` |
| API format | OpenAI-compatible chat completions |
| Model | `nvidia/nemotron-3.5-lightning:free` |
| Authentication | `OPENROUTER_API_KEY` in a gitignored `.env` file |

## Packages

### Direct dependencies

| Package | Locked version | Purpose |
| --- | --- | --- |
| `openai` | 3.42.0 | `AsyncOpenAI` client for calling OpenRouter |
| `python-dotenv` | 1.2.4 | Loads `.env` into the environment |

### Transitive dependencies

| Package | Locked version |
| --- | --- |
| `annotated-types` | 0.8.0 |
| `anyio` | 4.15.1 |
| `h11` | 0.16.0 |
| `httpcore2` | 2.16.0 |
| `httpx2` | 2.16.0 |
| `httpx2-jsfetch` | 1.0 |
| `idna` | 3.20 |
| `jiter` | 0.18.0 |
| `pydantic` | 2.14.2 |
| `pydantic-core` | 2.50.2 |
| `sniffio` | 1.3.1 |
| `truststore` | 0.10.5 |
| `typing-extensions` | 4.16.0 |
| `typing-inspection` | 0.4.4 |

### Standard library

| Module | Used for |
| --- | --- |
| `asyncio` | Running the async entry point and LLM calls |
| `dataclasses` | Event and token usage data types |
| `enum` | Event type enumerations |
| `os` | Reading environment variables |
| `typing` | Type hints |
