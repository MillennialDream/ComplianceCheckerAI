# AI Compliance Checker

A FastAPI application that checks webpage content against compliance policies using OpenAI's GPT-4. The API scrapes webpage content and analyzes it against specified compliance guidelines, returning detailed violation reports and recommendations.

Please refer to `https://platform.openai.com/docs/overview` for OpenAI documentation.


## Prerequisites

- Python 3.8+
- OpenAI API key

## Install dependencies:
```bash
pip install fastapi[standard] requests beautifulsoup4 openai
```

## Configuration

Setup system environment variables to securely store and access API key or skip to next step to use it with run command directly

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Application

1. Make sure your virtual environment is activated

2. Start the FastAPI server:
```bash
# Run server
fastapi run main.py

# Run dev server
fastapi dev main.py

# Run with environment variables 
OPEN_API_KEY= {your_openai_api_key} fastapi run main.py
```

The API will be available at `http://localhost:8000`

Please refer to FastAPI documentation at `https://fastapi.tiangolo.com/` for more details.

## API Endpoints

FastAPI automatically generates OpenAPI documentation which can be accessed from `http://localhost:8000/docs`

There are two API endpoints, one to test compliance and another for easier testing

### Check Compliance

**Endpoint:** `POST /check-compliance`

Checks a webpage against compliance policies. Requires webpage and compliance policy URLs as input.

### Example

**Endpoint:** `GET /example`

Endpoint for easier testing using test input data.
