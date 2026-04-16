from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from openai import OpenAI

embeddings = OpenAIEmbeddings()
db = FAISS.load_local(
    "../vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)
client = OpenAI()

def get_answer(query):
    docs = db.similarity_search(query, k=3)

    if not docs:
        return "I don't have an answer for that yet.", []

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are Bugasura AI Assistant.

Answer ONLY using this knowledge:

{context}

Question: {query}

Answer in bullet points.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    return answer, ["Knowledge Base"]