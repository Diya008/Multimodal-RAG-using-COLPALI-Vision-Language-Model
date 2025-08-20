# Multimodal-RAG-using-COLPALI-Vision-Language-Model
This repository contains the necessary files to create a Multimodal RAG based Chatbot , that ingests a PDF having text, tables and images. 
Using Colpali Model we can embed the page as image and pass it to any VLM for generation of responses based on query.

VISION MODEL USED: google/gemini-2.0-flash
COLPALI Reference: https://github.com/illuin-tech/colpali
Video Reference : https://youtu.be/DI9Q60T_054?si=fRoBC_JTg5Gb4d6i


PDF LINK: https://arxiv.org/abs/1706.03762

INSTALLATION FOR SYSTEMS WITHOUT CPU(NO GPU): Can run it in VSCode
pip install byaldi
pip install -q git+https://github.com/huggingface/transformers.git qwen-vl-utils optimum
pip install streamlit 

INSTALLATION FOR SYSTEMS WITH GPU:Run it in Colab using T4 GPU
pip install byaldi
!sudo apt-get install -y poppler-utils
!pip install -q git+https://github.com/huggingface/transformers.git qwen-vl-utils flash-attn optimum auto-gptq bitsandbytes
