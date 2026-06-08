import json
import os
from typing import List

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv

load_dotenv()

# ==============================
# GLOBAL VARIABLES
# ==============================

DB_PATH = os.getenv("CHROMA_DB_PATH")

vectorstore = None
retriever = None


# ==============================
# ANSWER GENERATION
# ==============================

def generate_final_answer(chunks, query):
    """Generate final answer using multimodal content"""

    try:
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0
        )

        prompt_text = f"""
Based on the following documents, answer this question:

QUESTION:
{query}

DOCUMENTS:
"""

        for i, chunk in enumerate(chunks):

            prompt_text += f"\n--- DOCUMENT {i+1} ---\n"

            if "original_content" in chunk.metadata:

                original_data = json.loads(
                    chunk.metadata["original_content"]
                )

                raw_text = original_data.get("raw_text", "")

                if raw_text:
                    prompt_text += f"\nTEXT:\n{raw_text}\n"

                tables_html = original_data.get("tables_html", [])

                if tables_html:

                    prompt_text += "\nTABLES:\n"

                    for j, table in enumerate(tables_html):
                        prompt_text += f"\nTable {j+1}:\n{table}\n"

        prompt_text += """

Provide:
- clear answer
- concise answer
- Hinglish if user asks in Hinglish
- English otherwise

If answer not found:
"I don't have enough information."

ANSWER:
"""

        message_content = [
            {
                "type": "text",
                "text": prompt_text
            }
        ]

        # Add images if available
        for chunk in chunks:

            if "original_content" in chunk.metadata:

                original_data = json.loads(
                    chunk.metadata["original_content"]
                )

                images_base64 = original_data.get(
                    "images_base64",
                    []
                )

                for image_base64 in images_base64:

                    message_content.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    })

        message = HumanMessage(content=message_content)

        response = llm.invoke([message])

        return response.content

    except Exception as e:

        print(f"Answer generation failed: {e}")

        return "Sorry, I encountered an error while generating the answer."


# ==============================
# INITIALIZE RAG
# ==============================

def initialize_rag():

    global vectorstore, retriever

    if retriever is None:

        if not os.path.exists(DB_PATH):
            raise Exception(
                "Vector DB not found. Run ingestion first."
            )

        embedding_model = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

        vectorstore = Chroma(
            persist_directory=DB_PATH,
            embedding_function=embedding_model
        )

        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 5,
                "fetch_k": 10
            }
        )