from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
import os

load_dotenv()

# Debug: Check if API key exists
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not found in .env file")
else:
    print(f"API Key found: {api_key[:10]}...")
    model = ChatOpenAI(model='gpt-4')
    result = model.invoke("what is programing ?")
    print(result)