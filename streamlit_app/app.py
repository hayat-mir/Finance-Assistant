# streamlit_app/app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.api_agent import get_stock_summary
from agents.scraping_agent import get_earnings_news
from agents.retriever_agent import RetrieverAgent
from agents.language_agent import LanguageAgent
from agents.voice_agent import VoiceAgent

st.set_page_config(page_title="Finance Assistant", layout="wide")
st.title("📊 AI Market Brief Assistant (Voice & Text)")
st.markdown("Ask for an 8 AM brief on Asia Tech risk & earnings.")

@st.cache_resource
def load_retriever():
    return RetrieverAgent()

@st.cache_resource
def load_language_model():
    return LanguageAgent()

@st.cache_data
def load_stock_data():
    tickers = ["TSM", "005930.KQ"]
    return get_stock_summary(tickers)

@st.cache_data
def load_news():
    tickers = ["TSM", "005930.KQ"]
    news = []
    for t in tickers:
        news.extend(get_earnings_news(t))
    return news


# 1. Load stock data
stock_data = load_stock_data()
st.write("📈 Stock Summary:", stock_data)

# 2. Get earnings news
news = load_news()
st.write("📰 Earnings News:", news)

# 3. Retrieve context from data
doc_chunks = [f"{t} moved {data['change_pct']}% to {data['today_close']}" for t, data in stock_data.items()]
doc_chunks.extend(news)

retriever = load_retriever()
retriever.ingest(doc_chunks)
query = "Any earnings surprises and Asia tech risk?"
relevant = retriever.retrieve(query)
st.write("🔍 Retrieved Context:", relevant)

# 4. Generate LLM summary
llm = load_language_model()
brief = llm.summarize_brief(" ".join(relevant))
st.subheader("📋 Morning Brief:")
st.write(brief)

# 5. Speak
voice = VoiceAgent()
if st.button("🔊 Speak Brief"):
    voice.speak(brief)
