from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')

# FIX: Removed 'dimensions=32' and updated 'model' to 'model_name'
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

result = embedding.embed_query("What is the capital of Pakistan?")

print("Your Embedding Vector:")
print(result)

print(f"\nTotal Dimensions: {len(result)}")