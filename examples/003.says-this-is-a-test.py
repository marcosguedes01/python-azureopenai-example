import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_DAVINCE_NAME")

response = openai.Completion.create(
    engine=deployment_name,
    prompt="Say this is a test",
    temperature=0,
    max_tokens=7
)

result = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(result)