# This file is used to index a PDF file using the RAG model.
# It will create an index that can be used later for searching and retrieval.
from main import RAG

if __name__ == "__main__":
    RAG.index(
        input_path="data.pdf", # path to your PDF file
        index_name="data", # name of the index to be created
        store_collection_with_index=True, # set this to false if you don't want to store the base64 representation
        overwrite=True
    )

#The index will be stored in the ".byaldi" folder by default.
