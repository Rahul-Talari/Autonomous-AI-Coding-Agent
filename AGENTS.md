# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

Early-stage Python project for an autonomous AI coding agent. There is currently no test suite, linter config, or README content.

## Commands

The project uses [uv](https://docs.astral.sh/uv/) and requires Python 3.14 (`.python-version`).

```sh
uv sync              # install dependencies into .venv
uv run main.py       # run the current entry point (sends a sample chat request)
uv add <package>     # add a dependency
```

## Architecture

- `main.py` (repo root) is the working entry point. It imports `client.llm_client` from the top-level `client/` package, so run it from the repo root.
- `client/llm_client.py` defines `LLMClient`, an async wrapper around `openai.AsyncOpenAI` pointed at OpenRouter (`https://openrouter.ai/api/v1`). The underlying client is created lazily in `get_client()` and must be released with `await close()`. `chat_completion(messages, stream=...)` sends to `_stream_response` or `_non_stream_response`.
- The project is not a package. `pyproject.toml` sets `[tool.uv] package = false` and has no build system or script entry point, and there is no `src/` layout. Code lives in top-level packages such as `client/`, and `main.py` runs it.

`chat_completion` is an async generator that yields `StreamEvent` objects (defined in `client/response.py`), so callers consume it with `async for`, not `await`.

`client/llm_client.py` reads `OPENROUTER_API_KEY` from a gitignored `.env` file in the repo root, loaded with python-dotenv.

## Known issues

- The model (`nvidia/nemotron-3.5-lightning:free`) is hardcoded in `chat_completion`.
