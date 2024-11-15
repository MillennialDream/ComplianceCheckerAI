import openai
from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# Initialize Fastapi
app = FastAPI()

# Initialize OpenAI client
client = OpenAI()


def fetch_webpage_content(url: str):
    """
    Extracts webpage content using BeautifulSoup4
    :param url: url of the webpage
    :return: webpage text content
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove non-text elements like script, style, etc.
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text content
        text = soup.get_text(separator='\n')

        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        text = ' '.join(line for line in lines if line)

        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching webpage: {str(e)}")


def check_compliance(webpage_content, policy_content):
    """
    Checks webpage content against compliance policy using OpenAI.
    :param webpage_content: webpage content
    :param policy_content: compliance policy content
    :return: compliance findings
    """
    try:
        prompt = f"""
               Analyze the following webpage content against the given compliance policy;

               Compliance Policy:
               {policy_content}

               Webpage Content:
               {webpage_content}
               """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a compliance checking assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking compliance: {str(e)}")


@app.post("/check-compliance")
async def check_compliance_endpoint(webpage_url: str, policy_url: str):
    """
     Checks webpage content against compliance policy using AI and return findings.
    :param webpage_url: webpage url to check for compliance
    :param policy_url: policy url to check against
    :return: compliance findings
    """
    # Parse webpage content
    webpage_content = fetch_webpage_content(webpage_url)
    # print(webpage_content)

    # Parse policy page content
    policy_page_content = fetch_webpage_content(policy_url)
    # print(policy_page_content)

    # Check compliance
    compliance_result = check_compliance(webpage_content, policy_page_content)
    # print(compliance_result)

    return compliance_result