#This file is used to load the RAG model once and cache it for use in the main application.
from byaldi import RAGMultiModalModel
import streamlit as st

@st.cache_resource
def load_rag_model():
    return RAGMultiModalModel.from_index(
        index_path="data",       # folder name of your index (refer index.py file)
        index_root=".byaldi",    # root folder where the index is stored
        device="cpu",            # or "cuda" if GPU is available
        verbose=1
    )


RAG = load_rag_model()
