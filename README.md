# 🚀 Multi-Modal RAG Chatbot (AI Knowledge Assistant)

An advanced **Multi-Modal Retrieval-Augmented Generation (RAG)** system built using real-world business data from *Prachi's Organics*.

This project demonstrates how to build an AI system that can:

* Understand PDFs (text + tables + images)
* Answer queries in multiple languages (English, Hinglish, Marathi)
* Serve responses via FastAPI backend
* Integrate with a real e-commerce website

---

## 🧠 Key Features

✅ Multi-modal document understanding (text, tables, images)
✅ Semantic search using vector database (ChromaDB)
✅ AI-generated contextual answers using LLMs
✅ Multilingual responses (EN + Hinglish + Marathi)
✅ FastAPI backend for real-time interaction
✅ Scalable architecture (ready for AWS EC2 deployment)

---

## 🏗️ Tech Stack

* **Python**
* **LangChain**
* **OpenAI API**
* **ChromaDB**
* **FastAPI**
* **Unstructured (PDF parsing)**

---

## 📂 Project Architecture

1. **Data Ingestion**

   * Parses PDF using `unstructured`
   * Extracts text, tables, and images
   * Converts into structured chunks

2. **Embedding Layer**

   * Generates embeddings using OpenAI
   * Stores in ChromaDB

3. **Retrieval System**

   * Semantic similarity search
   * Context-aware retrieval

4. **Generation Layer**

   * LLM generates responses using retrieved context
   * Supports multilingual output

5. **API Layer**

   * FastAPI serves responses to frontend

---

## ⚙️ Installation

```bash
git clone https://github.com/selvvinnn/multi-modal-rag-chatbot.git
cd multi-modal-rag-chatbot

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key
```

---

## ▶️ Run the Project

```bash
python app/api.py
```

---

## 🌐 Integration

This chatbot is integrated with:

👉 https://prachisorganics.com
👉 Frontend Repo: https://github.com/selvvinnn/prachisorganics-ecom-website-ai-ml

---

## 🚀 Future Improvements

* Deploy on AWS EC2
* Add voice-based interaction
* Improve image understanding (Vision models)
* Add user personalization

---

## 💡 What I Learned

* Building end-to-end RAG systems
* Handling real-world unstructured data
* Vector databases & embeddings
* API development with FastAPI
* AI system design for production

---

## 👨‍💻 Author

**Selvin Fernandes**

If you found this useful, ⭐ the repo!
