from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Paper Summarizer")

user_input = st.text_input("Enter your prompt")


if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)






