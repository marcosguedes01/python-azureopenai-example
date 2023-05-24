import load_modules
import os
import openai
from dotenv import load_dotenv
from convert.convert_response import getResultFromResponse

load_dotenv()

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_DAVINCE_NAME") #This will correspond to the custom name you chose for your deployment when you deployed a model. 

animal = "dog"

# Send a completion call to generate an answer
start_phrase = """Suggest three names for an animal that is a superhero.
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(animal)

response = openai.Completion.create(
    engine=deployment_name,
    prompt=start_phrase,
    max_tokens=30
)

result = getResultFromResponse(response)
print(result)