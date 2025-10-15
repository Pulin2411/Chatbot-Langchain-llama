import streamlit as st
from dotenv import load_dotenv
import os

# --- Load environment variables ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HEADER ---
st.title("🤖 AI Chat Assistant")
st.markdown("""
Welcome to your interactive AI assistant powered by **LangChain** and **LlamaIndex**.
Use the sidebar to choose your engine, model, and creativity settings.
""")

# --- SIDEBAR CONFIG ---
st.sidebar.header("⚙️ Settings")

# Engine selection
engine_choice = st.sidebar.radio(
    "Select Engine",
    ["LangChain Engine", "LlamaIndex Engine"],
    index=1
)

# Dynamic import based on choice
if engine_choice == "LangChain Engine":
    from app_langchain import query_bot
else:
    from app_llamaindex import query_bot

# Model and creativity settings
model_choice = st.sidebar.selectbox(
    "Select Model",
    ["gpt-3.5-turbo", "gpt-4-turbo"],
    index=0
)

temperature = st.sidebar.slider(
    "Response Creativity",
    0.0, 1.0, 0.5, 0.1
)

# Chat Reset Button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.sidebar.success("Chat history cleared.")
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("💡 Tip: GPT-4 is slower but more contextually accurate.")

# --- SESSION STATE (Memory) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT ---
prompt = st.chat_input("Type your question here...")

if prompt:
    if not api_key:
        st.error("⚠️ OpenAI API key missing in your .env file.")
    else:
        # Store user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = query_bot(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")

# --- FOOTER ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, LangChain & LlamaIndex | © 2025 Pulin Shah")
