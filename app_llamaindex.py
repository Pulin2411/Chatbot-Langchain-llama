import os
from dotenv import load_dotenv

# ✅ Correct imports for LlamaIndex 0.10.43
from llama_index.core import SimpleDirectoryReader, ServiceContext, StorageContext
from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# -------------------- ENVIRONMENT SETUP --------------------
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("❌ OpenAI API key not found. Please check your .env file.")

# -------------------- LLM + EMBEDDING SETUP --------------------
llm = OpenAI(model="gpt-4-turbo", api_key=openai_api_key)
embed_model = OpenAIEmbedding(model="text-embedding-3-small", api_key=openai_api_key)

# -------------------- SERVICE CONTEXT --------------------
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

# -------------------- LOAD DOCUMENTS --------------------
data_path = "data"
if not os.path.exists(data_path):
    print(f"⚠️ Directory '{data_path}' not found. Using empty document set.")
    documents = []
else:
    documents = SimpleDirectoryReader(data_path).load_data()


# -------------------- CREATE OR LOAD VECTOR INDEX --------------------
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# -------------------- QUERY FUNCTION --------------------
def query_bot(question: str) -> str:
    """Query the document-based chatbot using LlamaIndex."""
    query_engine = index.as_query_engine(similarity_top_k=3)
    response = query_engine.query(question)
    return str(response)
