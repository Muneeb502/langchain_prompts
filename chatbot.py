# this chatbot is without storing the previous chat history
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

while True:
    u_input = input("you : ")
    if u_input == "exit":
        break
    result = model.invoke(u_input)
    print(f"AI : {result.content}")


    

