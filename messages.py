from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


messages = [
    SystemMessage(content="you are helpful python expert"),
    HumanMessage(content="tell about langchain in easy way ")
]


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

