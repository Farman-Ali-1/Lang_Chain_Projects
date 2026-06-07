import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# 1. Load variables from your .env file
load_dotenv()



# 2. Define your models (Replaced ChatAnthropic with OpenAI models to match your keys)
model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatOpenAI(model="gpt-4o-mini") # Alternatively, use HuggingFaceEndpoint here

# 3. Define Prompts
prompt1 = PromptTemplate(
    template='Create short and simple notes from the following text {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Create five short questions answers from the following text {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='merge the provided notes and quiz in a single document \n notes {notes} and quiz {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

# 4. Construct Parallel and Merge Chains
parralell_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parralell_chain | merge_chain

# 5. Input Text Block
text = """
Computer network is a collection of interconnected devices that communicate with each other to exchange data and resources. It enables efficient communication and supports services like email, file sharing, and internet access.

Nodes are physical devices such as computers, mobiles, or printers.
Routers and switches control the flow of information.
Transmission media carry data from one device to another.
Wired media includes Ethernet and optical fiber cables.
"""

# 6. EXECUTE THE CHAIN
# FIXED: Changed {'text':{text}} to {'text': text} to pass a clean string variable instead of a set
result = chain.invoke({'text': text})

print(result)





















# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_anthropic import ChatAnthropic
# from langchain_core.runnables import RunnableParallel

# load_dotenv()

# model1 = ChatOpenAI()

# model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

# prompt1 = PromptTemplate(
#     template='Create short and simple notes from the following text {text}',
#     input_variables=['text']
# )

# prompt2 = PromptTemplate(
#     template='Create five short questions answers from the following text {text}',
#     input_variables=['text']
# )

# prompt3 = PromptTemplate(
#     template='merge the provided notes and quiz in a single document \n notes {notes} and quiz {quiz}',
#     input_variables=['notes','quiz']
# )

# parser = StrOutputParser()

# parralell_chain = RunnableParallel({
#     'notes': prompt1 | model1 | parser,
#     'quiz': prompt2 | model2 | parser
# })

# merge_chain = prompt3 | model1 | parser

# chain = parralell_chain | merge_chain

# text = """
#     Computer network is a collection of interconnected devices that communicate with each other to exchange data and resources. It enables efficient communication and supports services like email, file sharing, and internet access.

# Nodes are physical devices such as computers, mobiles, or printers.
# Routers and switches control the flow of information.
# Transmission media carry data from one device to another.
# Wired media includes Ethernet and optical fiber cables.
# """

# result = chain.invoke({'text':{text}})

# print(result)