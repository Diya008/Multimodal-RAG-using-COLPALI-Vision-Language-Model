import base64
import io
import streamlit as st
from load_once import RAG
import google.generativeai as genai
from PIL import Image

# Setup Gemini API
GOOGLE_API_KEY = "" # include your Google API key here 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Streamlit Config
st.set_page_config(page_title="Chatbot", layout="centered")
st.title("Transformers Chatbot")

# Initialize session state-
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # List of dicts: {"user": ..., "bot": ..., "image": ...}

# User Input
query = st.text_input("💬 Your question:")

if st.button("Send") and query.strip():
    with st.spinner("Thinking and generating answer..."):
        try:
            # 1. Search RAG
            results = RAG.search(query, k=2)

            # 2. Decode images (skip specific pages)
            image_bytes_list = [
                base64.b64decode(result.base64)
                for result in results
                if result['page_num'] not in [1, 2, 3]
            ]
            image_pil_list = [Image.open(io.BytesIO(img_bytes)) for img_bytes in image_bytes_list]

            # 3. Most relevant image
            most_relevant_index = results.index(max(results, key=lambda x: x['score']))
            most_relevant_image = image_pil_list[most_relevant_index]

            # 4. Prepare conversation context for Gemini
            history_text = ""
            for turn in st.session_state.chat_history:
                history_text += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"

            prompt = f"{history_text}User: {query}\nAssistant:"

            # 5. Get model response
            response = model.generate_content([most_relevant_image, prompt])

            answer = response.text

            # 6. Save to history
            st.session_state.chat_history.append({
                "user": query,
                "bot": answer,
                "image": most_relevant_image
            })

        except Exception as e:
            st.error(f"Error: {e}")

# Display chat history
for turn in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {turn['user']}")
    #if turn["image"]:
        #st.image(turn["image"], caption="📷 Retrieved Image", use_container_width=True)
    st.markdown(f"**🤖 Bot:** {turn['bot']}")
    st.markdown("---")