import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()                                                  
groq=ChatGroq(model=os.getenv("GROQ_MODEL"),
             api_key=os.getenv("GROQ_API_KEY"))
gemini=ChatGoogleGenerativeAI(model=os.getenv("GEMINI_MODEL"),api_key=os.getenv("GEMINI_API_KEY"))    
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])                  
groq_chain=prompt | groq
groq_response=groq_chain.invoke({"question":"What is langchain how it works"})
print("GROQ:")
print(groq_response.content)

gemini_chain=prompt | gemini
gemini_response=gemini_chain.invoke({"question":"What is langgraph?"})
print("\n GEMINI:")
print(gemini_response.content)