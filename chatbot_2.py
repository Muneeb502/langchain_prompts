# this chatbot is with storing the previous chat history
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


chat_history = []

while True:
    u_input = input("you : ")
    if u_input == "exit":
        print(chat_history)
        break
    chat_history.append(u_input)
    result = model.invoke(chat_history)
    chat_history.append(result)
    print(f"AI : {result.content}")