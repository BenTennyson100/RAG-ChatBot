# 📚 RAG-ChatBot

A Retrieval-Augmented Generation (RAG) based chatbot that combines the power of Large Language Models (LLMs) with document-based retrieval. The system allows context-aware answering by retrieving relevant chunks from external documents and passing them to the LLM for response generation.

---

## 🔧 Features

- 📄 Ingests and indexes documents  
- 🔍 Contextual retrieval of information using semantic similarity  
- 🤖 Uses a local or remote LLM (like OpenAI or HuggingFace)  
- 🧠 Combines retrieval results with prompt for better answers  
- 🔄 Modular and extendable codebase  

---

## 🗂️ Folder Structure

```
RAG-ChatBot/
├── app.py                 # Main Streamlit app
├── loader.py              # Loads and chunks documents
├── rag_chain.py           # Defines the RAG chain logic
├── environment.yml        # Conda environment setup
├── requirements.txt       # Python package dependencies
├── .env                   # Environment variables (keys, paths)
└── README.md              # You're here
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/BenTennyson100/RAG-ChatBot.git
cd RAG-ChatBot
```

### 2. Set Up Environment

Using Conda:

```bash
conda env create -f environment.yml
conda activate rag-chatbot
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file and add:

```env
OPENAI_API_KEY=your_openai_key
```

*(or any other LLM provider's key you're using)*

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧩 Tech Stack

- Python  
- LangChain  
- Streamlit  
- OpenAI / HuggingFace  
- FAISS / Chroma (Vector DBs)

---

## 🛠️ To Do

- Add PDF/website/document upload via UI  
- Multi-turn conversation memory  
- Deploy on HuggingFace Spaces or Streamlit Cloud  

---

## 🤝 Contributions

Pull requests and suggestions are welcome!

---

## 📄 License

[MIT License](LICENSE)
