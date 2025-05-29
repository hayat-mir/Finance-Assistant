# 📊 AI Finance Assistant – Voice-Powered Market Brief Generator

This project is an open-source, multi-agent financial assistant that delivers **spoken market briefs** based on real-time stock data and earnings news. Built for the "Agents Intern Assignment", it integrates live data ingestion, retrieval-augmented generation (RAG), natural language summarization, and voice I/O — all in a clean Streamlit interface.

---

## 🧠 Use Case

> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

🗣️ Example Output:
> "Today, your Asia tech allocation is 22% of AUM. TSMC beat estimates by 4%, Samsung missed by 2%. Regional sentiment is neutral with a cautionary tilt due to rising yields."

---

## 📐 Architecture

User (Voice/Text)
↓
Streamlit UI
↓
Voice Input → Whisper (STT) → Query
↓
[API + Scraper + Retriever Agents]
↓
Language Agent (Tiny GPT via Transformers)
↓
TTS Response → pyttsx3 → Streamlit UI → 🔊

## 🧩 Agents

| Agent             | Role                                                                 |
|------------------|----------------------------------------------------------------------|
| **API Agent**     | Fetches stock prices and changes using `yfinance`                   |
| **Scraping Agent**| Pulls latest earnings-related news from Yahoo Finance               |
| **Retriever Agent**| Embeds all context using `sentence-transformers`, indexes via FAISS |
| **Language Agent**| Uses lightweight local LLM (`tiny-gpt2`) for generating the brief   |
| **Voice Agent**   | Uses `Whisper` for STT and `pyttsx3` for speech                     |

---

## ⚙️ Project Structure

finance-voice-assistant/
├── agents/ # Core agent logic
│ ├── api_agent.py
│ ├── scraping_agent.py
│ ├── retriever_agent.py
│ ├── language_agent.py
│ └── voice_agent.py
├── streamlit_app/ # Streamlit UI
│ └── app.py
├── docs/ # AI tool usage logs
│ └── ai_tool_usage.md
├── requirements.txt # Python dependencies
├── Dockerfile # (Optional) for deployment
└── README.md # This file

---

## 🔧 Tools & Frameworks

- `streamlit` – User interface
- `yfinance` – Real-time stock data
- `BeautifulSoup` – Earnings news scraping
- `sentence-transformers` + `FAISS` – RAG engine
- `transformers` (Tiny GPT-2) – Language generation
- `whisper` – Speech-to-text (STT)
- `pyttsx3` – Text-to-speech (TTS)


## ⚡ Optimizations

- Cached models and data using `@st.cache_resource` and `@st.cache_data`
- Whisper model set to `"tiny"` for faster STT
- Local LLM (`sshleifer/tiny-gpt2`) for speed and no dependency on APIs
- All agents modularized for easy development

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/finance-voice-assistant.git
cd finance-voice-assistant

pip install -r requirements.txt

streamlit run streamlit_app/app.py

