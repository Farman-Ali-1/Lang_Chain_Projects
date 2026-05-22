from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

# Load your environment variables (.env file)
load_dotenv('.env')

# Make sure LangChain can see your token from the environment
# (Ensure your .env file has: HUGGINGFACEHUB_API_TOKEN=your_actual_token)
embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction" # This tells the API to return vector embeddings
)

# This will now make a cloud API request instead of running locally
result = embedding.embed_query("What is the capital of Pakistan?")

print("Your Cloud-Generated Embedding Vector:")
print(result)
print(f"\nTotal Dimensions: {len(result)}")