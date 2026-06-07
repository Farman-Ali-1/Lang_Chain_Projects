from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatOpenAI()

templete1 = PromptTemplate(
    template="Give me detailed information about {topic}",
    input_variables=['topic']
)

templete2 = PromptTemplate(
    template="Give me summary of {text} in 5 lines",
    input_variables=['text']
)

parser = StrOutputParser()

chain = templete1 | model | parser | templete2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)