from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Chatbot:", result.content)

print("Chat history:", chat_history)