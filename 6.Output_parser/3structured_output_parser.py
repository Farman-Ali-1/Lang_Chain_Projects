import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


dotenv.load_dotenv()

#  in json outout parser it can not enforce schema like in that we can not tell in which format in need output


# Initialize model
model = ChatOpenAI()

# Initialize parser
parser = StructuredOutputParser()

# Prompt template
template = PromptTemplate(
    template="""Give me 5 facts about {topic} {format_instructions}""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)