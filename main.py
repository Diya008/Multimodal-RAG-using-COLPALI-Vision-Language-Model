import base64
from pathlib import Path
HF_TOKEN = "" # include your Hugging Face token here
GOOGLE_API_KEY = "" # include your Google API key here if using Gemini model.
from byaldi import RAGMultiModalModel

RAG = RAGMultiModalModel.from_pretrained("vidore/colpali-v1.2", verbose=1, device="cpu")