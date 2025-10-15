import os
from dotenv import load_dotenv
from pathlib import Path

# ✅ Updated imports for latest LlamaIndex versions
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# --- Load environment variables ---
load_dotenv()

def query_bot(question: str, api_key=None, model="gpt-4-turbo", temperature=0.5) -> str:
    """Query the document-based chatbot using LlamaIndex (new Settings API)."""

    # --- Use passed or .env API key ---
    openai_api_key = api_key or os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        return "❌ OpenAI API key not found. Please check your .env file."

    try:
        # ✅ Initialize OpenAI models using new Settings API
        llm = OpenAI(
            model=model,
            temperature=temperature,
            api_key=openai_api_key
        )

        embed_model = OpenAIEmbedding(
            model="text-embedding-3-small",
            api_key=openai_api_key
        )

        # ✅ Register in Settings (replaces ServiceContext)
        Settings.llm = llm
        Settings.embed_model = embed_model

        # --- Load documents from 'data' folder ---
        data_path = Path("data")
        if not data_path.exists() or not any(data_path.iterdir()):
            print(f"⚠️ No documents found in '{data_path}'. Using empty dataset.")
            documents = []
        else:
            documents = SimpleDirectoryReader(str(data_path)).load_data()

        # --- Create index and query ---
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine(similarity_top_k=3)
        response = query_engine.query(question)

        return str(response)

    except Exception as e:
        return f"❌ LlamaIndex Engine Error: {str(e)}"
