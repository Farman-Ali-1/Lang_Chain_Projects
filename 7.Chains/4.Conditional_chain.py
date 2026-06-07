from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

# 1. Load variables from your .env file
load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description='Give the sentiment of Feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='classify the sentiment of the given feedback into positive or negative {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

chain2 = prompt2 | model | parser
chain3 = prompt3 | model | parser

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', chain2),
    (lambda x: x.sentiment == 'negative', chain3),
    RunnableLambda(lambda x: "could not find sentiment")
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback':'this is tarrible phone'})

# print(result)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'this is tarrible phone'}))