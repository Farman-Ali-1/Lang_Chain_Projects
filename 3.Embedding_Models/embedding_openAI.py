from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()

# Removed 'device' since OpenAI processes this in the cloud
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# Changed 'aembed_query' to 'embed_query' for standard synchronous execution
result = embedding.embed_query("What is the capital of Pakistan?")

print("Your Embedding Vector:")
print(result)
print(f"\nTotal Dimensions: {len(result)}")