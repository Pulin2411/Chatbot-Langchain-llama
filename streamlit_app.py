import os
from dotenv import load_dotenv
import streamlit as st
from pathlib import Path

# --- Load environment variables safely ---
def load_api_key():
    env_path = Path(__file__).resolve().parent / '.env'
    if not env_path.exists():
        st.error("⚠️ `.env` file not found. Please add one to your project root.")
        return None

    load_dotenv(dotenv_path=env_path)
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.error("⚠️ `OPENAI_API_KEY` not found in `.env`. Please add your key and restart.")
        return None

    if not api_key.startswith("sk-"):
        st.error("❌ Invalid API key format. It should start with `sk-`.")
        return None

    return api_key


# --- Streamlit UI Setup ---
st.set_page_config(
    page_title="AI Assistant | LangChain + LlamaIndex",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chat Assistant")
st.caption("Powered by **LangChain**, **LlamaIndex**, and **OpenAI**")

# --- Sidebar Config ---
st.sidebar.header("⚙️ Settings")
engine = st.sidebar.radio("Select Engine", ["LangChain", "LlamaIndex"])
model_choice = st.sidebar.selectbox("Select Model", ["gpt-3.5-turbo", "gpt-4-turbo"])
temperature = st.sidebar.slider("Response Creativity", 0.0, 1.0, 0.5, 0.1)

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# --- Load OpenAI API Key ---
api_key = load_api_key()

if not api_key:
    st.stop()  # stop execution if no key is found

# --- Import App Logic ---
try:
    if engine == "LangChain":
        from app_langchain import query_bot
    else:
        from app_llamaindex import query_bot
except ImportError as e:
    st.error(f"🚫 Import Error: {e}")
    st.stop()


# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("💬 Thinking..."):
            try:
                response = query_bot(prompt, api_key=api_key, model=model_choice, temperature=temperature)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")

# --- Footer ---
st.markdown("""
<hr style='margin-top:2em; margin-bottom:1em;'>

<p style='text-align:center; font-size:0.9em; color:gray;'>
Built with ❤️ using <b>Streamlit</b>, <b>LangChain</b>, and <b>LlamaIndex</b><br>
© 2025 Pulin Shah
</p>
""", unsafe_allow_html=True)
