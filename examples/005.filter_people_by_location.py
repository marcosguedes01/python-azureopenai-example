import load_modules
import os
import openai
from dotenv import load_dotenv
from convert.convert_response import getResultFromResponse

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_DAVINCE_NAME")
prompt = """Consider the following people:
people = [
    {
        "id", 1
        "name": "Mario",
        "localization": "Recife"
    },
    {
        "id", 2
        "name": "Antonio",
        "localization": "Recife",
    },
    {
        "id", 3
        "name": "Maria",
        "localization": "Bahia",
    },
    {
        "id", 4
        "name": "Ana",
        "localization": "Recife",
    },
    {
        "id", 5
        "name": "Pedro",
        "localization": "Rio de Janeiro",
    }
]
    
    return suggestions from people who might know Mario (by localization)
    return in json format: { "id": 1, "name":"person name" }
"""

response = openai.Completion.create(
    engine=deployment_name,
    prompt=prompt,
    temperature=0,
    max_tokens=100
)
# print(response)
result = getResultFromResponse(response)
print(result)