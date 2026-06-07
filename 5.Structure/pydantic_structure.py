from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import Field,BaseModel
from typing import Literal,Optional
load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini"
)

class Reviews(BaseModel):

    keyTheme: list[str] = Field(description="Write down all themes discussed in the review")
    summary: list[str] = Field(description="Write a short summary of the review")
    sentiment: Literal['pos','neg'] = Field(description="Return Sentimental of review either positive or neagtive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write all pros mentioned in the review")
    cons: Optional[list[str]] = Field(default=None, description="Write all cons mentioned in the review")
   
structured_model = model.with_structured_output(Reviews)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
""")

print(result)

#  we can print saperatly summary and sentiment from that dict 
# print(result['summary'])













# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional

# class user(BaseModel):
#     name:str
#     age:Optional[int] = None
#     # email:EmailStr
#     email:str
#     cgpa: float = Field(gt=0, lt=10, default=5, description='represent CGPA')
# # pudantic can define type structure and also apply validation on data 
# # it can convert type by own like i have age int but i put like '25' it can convert it into int
# # it has some by default validations like emailstr it is use to validate email 
# # you can add constains and regax using Feild 


# new_user = {'name':"Farman", 'age':25, 'email':'abc@gmail.com'}
# student = user(**new_user)

# # you can convert pydantic object into json or dict

# print(student)
# student_dist=dict(student)
# print(student_dist['age'])
# student_json = student.model_dump_json()
# print(student_json)