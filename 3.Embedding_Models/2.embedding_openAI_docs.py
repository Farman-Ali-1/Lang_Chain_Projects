from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

document = [
    "The capital of Pakistan is Islamabad.",
    "The capital of France is Paris.",
    "The capital of Germany is Berlin."
]

result = embedding.embed_documents(document)

print("Your Embedding Vector:")
print(result)