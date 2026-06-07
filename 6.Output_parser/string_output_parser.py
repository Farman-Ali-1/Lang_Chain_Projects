# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

model = ChatOpenAI()

template1 = PromptTemplate(
    template="give me detail information about {topic}", 
    input_variables=['topic']
)


template2 = PromptTemplate(
    template="give me summary of {text} in 5 lines",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':'result1'})

result2 = model.invoke(prompt2)

print(result2.content)
