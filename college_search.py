import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variables (for GenerativeAI)
load_dotenv('.env')
palm_api_key = os.environ.get("PALM_API_KEY")


# Configure genai (optional, comment out if not using GenerativeAI)
if palm_api_key:
  genai.configure(api_key=palm_api_key)
  model = genai.GenerativeModel('gemini-pro')


def get_colleges(state, city):
  
  if palm_api_key:
    prompt = f"generate a list of colleges in {city}"
    response = model.generate_content(prompt)
    return response.text.split('\n')  # Return college info from GenerativeAI
  else:
    return ["No information found for colleges in this location."]
