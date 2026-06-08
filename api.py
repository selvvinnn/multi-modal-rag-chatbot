from fastapi import FastAPI
from pydantic import BaseModel
import time
import json
from datetime import datetime

import rag

app = FastAPI()

rag.initialize_rag()

class Query(BaseModel):
    query: str


@app.post("/ask")
def ask(query: Query):

    start = time.time()

    user_query = query.query

    chunks = rag.retriever.invoke(user_query)


    
    answer = rag.generate_final_answer(
        chunks,
        user_query
    )

    # ====================================
    # FALLBACK WHATSAPP SUPPORT
    # ====================================

    if "I don't have enough information" in answer:

        whatsapp_number = "918879176107"  # replace with your number

        whatsapp_link = f"https://wa.me/{whatsapp_number}"

        answer += f"""

    Please contact our support team on WhatsApp 🌿

    {whatsapp_link}
    """
    end = time.time()

    response_time = round(end - start, 2)

    print(f"Response Time: {response_time} seconds")


    log_data = {
        "time": str(datetime.now()),
        "query": user_query,
        "answer": answer,
        "response_time": response_time
    }

    with open("logs.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data) + "\n")


    return {
        "answer": answer,
        "response_time": response_time
    }