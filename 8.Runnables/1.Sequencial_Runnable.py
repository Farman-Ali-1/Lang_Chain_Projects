from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Write joke on {topic} and make it funny",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="explain me the jokes {text} in simple words",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

topic = input("Enter a topic for the joke: ")

output = chain.invoke({"topic": topic})

print(output)