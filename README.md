<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f7dcf153-9f47-40a3-b55f-d1ba51886843" />



<img width="1890" height="823" alt="image" src="https://github.com/user-attachments/assets/77a7ae68-28a8-4df2-ad81-89e52094fc18" />



# 🤖 Conversational Chatbot (LangChain + LlamaIndex)

A Streamlit-based conversational chatbot showcasing:
- **LangChain** for natural language conversations
- **LlamaIndex** for document-based retrieval QA

🧠 AI Chat Assistant (LangChain + LlamaIndex + Streamlit)

This project is an intelligent conversational assistant built using LangChain, LlamaIndex, and OpenAI GPT models.
It allows you to switch between LangChain and LlamaIndex backends dynamically from a modern Streamlit UI, making it flexible for experimenting with different reasoning engines.

🚀 Features

💬 Chat interface powered by Streamlit

🧩 Dual engine support — switch between:

LangChain (gpt-3.5 / gpt-4)

LlamaIndex (document-based querying)

🔐 Secure API key handling via .env file

⚙️ Configurable model, creativity (temperature), and session reset

📁 Modular design — app_langchain.py, app_llamaindex.py, streamlit_app.py

🌈 Clean and responsive UI

🏗️ Project Structure
📦 ChatbotProject
│
├── app_langchain.py          # LangChain engine logic
├── app_llamaindex.py         # LlamaIndex engine logic
├── streamlit_app.py          # Streamlit frontend controller
├── .env                      # Contains your OpenAI API key
├── requirements.txt          # All dependencies
├── data/                     # Folder for document ingestion (LlamaIndex)
└── README.md                 # Project documentation


## 🚀 Setup Instructions

1️⃣ Create a Virtual Environment
```bash
python -m venv venv
.env\Scripts\activate
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Add Your OpenAI API Key
Create a `.env` file:
```
OPENAI_API_KEY=sk-your_api_key_here
```

4️⃣ Run the Chatbot
```bash
python -m streamlit run streamlit_app.py
```

Open your browser: http://localhost:8501
