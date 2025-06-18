import os
from dotenv import load_dotenv
from google import genai


class ImproperlyConfigured(Exception):
    pass


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ImproperlyConfigured("Please check the api key configurations")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
)
print(
    f"{response.text}\n\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}"
)
