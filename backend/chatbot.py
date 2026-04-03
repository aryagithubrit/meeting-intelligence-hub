import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize client
client = None

def get_client():
    global client
    if client is None:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client

def analyze_with_ai(text):
    prompt = f"""
    Analyze this meeting transcript and return:

    1. Summary
    2. Action Items (with person if possible)
    3. Key Decisions
    4. Risks or Issues
    5. Suggested priorities

    Transcript:
    {text}
    """

    try:
        response = get_client().chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"