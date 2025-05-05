from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.messages import HumanMessage ,AIMessage , SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)



chat_history = [
    SystemMessage(content="you are a helpful assistent")
]


while True:
    u_input = input("you : ")
    chat_history.append(HumanMessage(content=u_input))
    if u_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(result.content)

print(chat_history)


