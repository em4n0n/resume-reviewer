import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer 📃")
st.markdown("Upload your resume in PDF format and get AI-powered feedback.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")