import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("❌ OpenAI API key not found. Please add it to your .env file.")

# Initialize model
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.6, openai_api_key=openai_api_key)

# Define prompt
prompt = ChatPromptTemplate.from_template(
    "You are an intelligent IT assistant. Answer clearly and concisely:\n\n{question}"
)

# Build chain
chain = LLMChain(llm=llm, prompt=prompt)

def query_bot(question: str) -> str:
    """Handles LangChain-based user queries."""
    if not question.strip():
        return "⚠️ Please enter a valid question."
    try:
        response = chain.invoke({"question": question})
        return response["text"]
    except Exception as e:
        return f"❌ Error: {str(e)}"
