from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    Name: str = Field(...,description='Name of Person')
    Age: int = Field(..., gt=0, description='Age of Person')
    City: str = Field(..., description='City where person live')

parser = PydanticOutputParser(pydantic_object=Person)

templete = PromptTemplate(
    template='Genrate Name Age and City of of {place} person \n {formate_instruction}',
    input_variables=['place'],
    partial_variables={'formate_instruction': parser.get_format_instructions()}
)

# prompt = templete.invoke({'place':'pakistan'})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = templete | model | parser

final_result = chain.invoke({'place':'pakistan'})

print(final_result)