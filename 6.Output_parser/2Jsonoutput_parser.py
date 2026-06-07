import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

#  in json outout parser it can not enforce schema like in that we can not tell in which format in need output


# Initialize model
model = ChatOpenAI()

# Initialize parser
parser = JsonOutputParser()

# Prompt template
template = PromptTemplate(
    template="""Give me 5 facts about {topic} {format_instructions}""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Create chain
chain = template | model | parser

# Invoke chain
result = chain.invoke({
    "topic": "black hole"
})

print(result)


















# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# model = ChatOpenAI()

# templete1 = PromptTemplate(
#     template="Give me detailed information about {topic}",
#     input_variables=['topic']
# )

# templete2 = PromptTemplate(
#     template="give me summary of {text} in 5 lines",
#     input_variables=['text']
# )

