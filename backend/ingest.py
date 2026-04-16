from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def ingest():
    loader = TextLoader("../data/kb.txt")
    docs = loader.load()

    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    db.save_local("../vector_store")

    print("✅ Knowledge base ingested")

if __name__ == "__main__":
    ingest()