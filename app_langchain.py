import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# --- Load environment variables ---
load_dotenv()

def query_bot(question: str, api_key=None, model="gpt-4-turbo", temperature=0.6) -> str:
    """Handles LangChain-based user queries with flexible API key and model."""

    # --- Validate question ---
    if not question.strip():
        return "⚠️ Please enter a valid question."

    # --- Load or use passed API key ---
    openai_api_key = api_key or os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        return "❌ OpenAI API key not found. Please add it to your .env file."

    # --- Initialize model dynamically ---
    try:
        llm = ChatOpenAI(
    model=model,
    temperature=temperature,
    api_key=openai_api_key  # ✅ updated param name in new version
)
       #llm = ChatOpenAI(model=model, temperature=temperature, openai_api_key=openai_api_key)
        prompt = ChatPromptTemplate.from_template(
            "You are an intelligent IT assistant. Answer clearly and concisely:\n\n{question}"
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.invoke({"question": question})
        return response["text"]
    except Exception as e:
        return f"❌ LangChain Engine Error: {str(e)}"
