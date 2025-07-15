import streamlit as st
from loader import load_pdf_and_split
from rag_chain import get_rag_chain

st.set_page_config(page_title="Chat with PDF", layout="wide")
st.title("🧠 Chat with your PDF (RAG App)")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and processing..."):
        chunks = load_pdf_and_split(uploaded_file)
        rag_chain = get_rag_chain(chunks)
        st.success("RAG system ready! Start chatting below 👇")

    user_input = st.text_input("Ask a question about your document:")

    if user_input:
        with st.spinner("Thinking..."):
            response = rag_chain.run(user_input)
            st.write("💬", response)
