# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ice Breaker is a Flask-based web application that generates personalized conversation starters by analyzing LinkedIn and Twitter profiles using LangChain and OpenAI.

## Development Commands

### Running the Application
```bash
# Install dependencies
pipenv install

# Run the Flask application
pipenv run python app.py

# Or directly with pipenv shell
pipenv shell
python app.py
```

### Code Quality Tools
```bash
# Format code with Black
pipenv run black .

# Sort imports with isort
pipenv run isort .

# Lint code with pylint
pipenv run pylint [module_name]
```

### Testing
```bash
# Note: No test files currently exist, but the README mentions pytest
pipenv run pytest .
```

## Architecture & Key Components

### Core Pipeline Flow
1. **Web Interface** (`app.py`): Flask server handling UI and API endpoints
2. **Main Logic** (`ice_breaker.py`): Orchestrates the entire ice breaker generation pipeline
3. **Agent System**: Profile lookup agents for LinkedIn and Twitter discovery
4. **Data Extraction**: Third-party integrations for scraping social media data
5. **AI Processing**: LangChain chains for generating summaries, interests, and ice breakers
6. **Output Parsing**: Structured response formatting using Pydantic models

### Key Modules

- **agents/**: LangChain ReAct agents for profile discovery
  - Uses Tavily for web search to find LinkedIn/Twitter profiles
  - Leverages LangChain hub prompts (hwchase17/react)

- **chains/**: Custom LangChain sequences for AI processing
  - Three distinct chains: summary, interests, ice breakers
  - Uses GPT-3.5-turbo with different temperature settings

- **third_parties/**: External API integrations
  - LinkedIn scraping via Scrapin.io API (`scrape_linkedin_profile`, supports `mock=True` for local testing using a hardcoded Gist URL)
  - Twitter data via tweepy (`scrape_user_tweets`), but `ice_breaker.py` currently calls `scrape_user_tweets_mock` which fetches from a GitHub Gist

- **tools/**: `get_profile_url_tavily` — wraps `TavilySearch` and is used by both agents

- **output_parsers.py**: Three Pydantic models (`Summary`, `TopicOfInterest`, `IceBreaker`) each with a `to_dict()` method; corresponding `PydanticOutputParser` instances are imported by chains

### Data Flow

```
POST /process  →  ice_break_with(name)
  → linkedin_lookup_agent.lookup(name)   # ReAct agent → Tavily search → returns LinkedIn URL
  → scrape_linkedin_profile(url)         # Scrapin.io API call
  → twitter_lookup_agent.lookup(name)    # ReAct agent → Tavily search → returns Twitter username
  → scrape_user_tweets_mock(username)    # Fetches mock tweets from GitHub Gist
  → get_summary_chain().invoke(...)      # GPT-3.5-turbo, temp=0 → Summary + 2 facts
  → get_interests_chain().invoke(...)    # GPT-3.5-turbo, temp=0 → 3 topics
  → get_ice_breaker_chain().invoke(...)  # GPT-3.5-turbo, temp=1 → 2 ice breakers
  → returns (Summary, TopicOfInterest, IceBreaker, profile_pic_url) as JSON
```

## API Dependencies

Required environment variables in `.env` (see `.env.example`):
- `OPENAI_API_KEY` - OpenAI API for LLM
- `SCRAPIN_API_KEY` - Scrapin.io for LinkedIn data
- `TAVILY_API_KEY` - Tavily for web search
- `TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_SECRET`, `TWITTER_BEARER_TOKEN` - Only needed if switching from mock to real Twitter API

Optional LangSmith tracing:
- `LANGCHAIN_TRACING_V2=true`
- `LANGCHAIN_API_KEY`
- `LANGCHAIN_PROJECT=ice_breaker`

## Development Notes

- Agents use GPT-4o-mini; chains use GPT-3.5-turbo
- Twitter is currently hardwired to mock data in `ice_breaker.py` — swap `scrape_user_tweets_mock` for `scrape_user_tweets` to use the real API
- LinkedIn also has `mock=True` on `scrape_linkedin_profile` for local testing without Scrapin.io credits
- Flask runs in debug mode on `0.0.0.0`; agents run with `verbose=True`
- No unit tests are currently implemented