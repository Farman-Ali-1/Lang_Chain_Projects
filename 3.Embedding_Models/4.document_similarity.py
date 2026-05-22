from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Pakistan national cricket team has produced many legendary cricketers who are famous around the world for their talent and passion.",  
    "Babar Azam is known for his elegant batting style and consistency in international cricket.",
    "Shaheen Afridi is one of Pakistan’s best fast bowlers and is famous for taking early wickets.",
    "Wasim Akram is considered one of the greatest swing bowlers in cricket history.",
    "Shahid Afridi became popular for his aggressive batting and record-breaking fast centuries."
]

query = "Who is the best fast bowler in Pakistan cricket history?"

document_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)
scores = cosine_similarity([query_embedding], document_embedding)[0]

index, score = sorted(enumerate(scores), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score:", score)