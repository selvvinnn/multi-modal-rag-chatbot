from fastapi import FastAPI
from pydantic import BaseModel

import rag 

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(query: Query):
    user_query = query.query

    # Initialize RAG (runs only once)
    rag.initialize_rag()

    # Now retriever is ready
    chunks = rag.retriever.invoke(user_query)

    # Generate answer
    answer = rag.generate_final_answer(chunks, user_query)

    return {"answer": answer}


