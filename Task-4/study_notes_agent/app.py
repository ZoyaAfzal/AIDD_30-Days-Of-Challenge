import streamlit as st
import os
import tempfile
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Adjusting the path to import PDFAgent
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "agents"))
from pdf_agent import PDFAgent

# Load environment variables (for GEMINI_API_KEY)
load_dotenv()

# --- Streamlit UI Configuration ---
st.set_page_config(page_title="AI-Powered PDF Study Agent", layout="wide")
st.title("📚 AI-Powered PDF Summary & Quiz Maker")

# Initialize PDFAgent
# Streamlit reruns the script, so use st.session_state to avoid re-initializing
if "pdf_agent" not in st.session_state:
    st.session_state.pdf_agent = PDFAgent()
agent = st.session_state.pdf_agent

# --- Helper to extract text for preview ---
def extract_text_from_pdf_for_preview(uploaded_file):
    # Ensure the file pointer is at the beginning
    uploaded_file.seek(0)
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# --- Sidebar for Agent info and settings ---
with st.sidebar:
    st.header("Agent Preferences")
    st.info("This agent can summarize PDFs and generate quizzes from them.")
    st.markdown("---")
    st.write("Powered by Google Gemini & OpenAgents SDK")
    st.markdown("---")
    if os.getenv("GEMINI_API_KEY"):
        st.success("Gemini API Key Loaded!")
    else:
        st.error("Gemini API Key not found. Please set GEMINI_API_KEY in your .env file.")

# --- Main Content ---

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Save uploaded file temporarily to pass path to agent (simulating Context7 MCP input)
    # The temporary file is needed because PyPDF2.PdfReader can take a file-like object,
    # but the simulated _get_pdf_text_from_mcp in PDFAgent expects a path.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_pdf_path = tmp_file.name

    st.success(f"PDF '{uploaded_file.name}' uploaded successfully!")

    # --- Text Preview Section ---
    st.subheader("Extracted Text Preview")
    with st.spinner("Extracting text for preview..."):
        preview_text = extract_text_from_pdf_for_preview(uploaded_file)
        if preview_text:
            with st.expander("Click to view full extracted text"):
                st.text(preview_text)
        else:
            st.warning("Could not extract text from PDF for preview.")

    st.markdown("---")

    # --- Summary Section ---
    st.header("Generate Summary")
    summary_type = st.selectbox(
        "Select Summary Type",
        options=["concise", "bullet_points", "student_friendly"],
        index=0,
        help="Choose the style of summary you want."
    )

    if st.button("Generate Summary"):
        if not os.getenv("GEMINI_API_KEY"):
            st.error("Cannot generate summary: Gemini API Key is missing.")
        else:
            with st.spinner(f"Generating {summary_type} summary..."):
                try:
                    # Call agent's summarize_pdf method
                    summary = asyncio.run(agent.summarize_pdf(temp_pdf_path, summary_type))
                    st.subheader(f"{summary_type.replace('_', ' ').title()} Summary:")
                    st.markdown(summary)

                    # Download button
                    st.download_button(
                        label="Download Summary",
                        data=summary,
                        file_name=f"{uploaded_file.name.replace('.pdf', '')}_{summary_type}_summary.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"An error occurred during summarization: {e}")

    st.markdown("---")

    # --- Quiz Section ---
    st.header("Generate Quiz")
    quiz_type = st.radio(
        "Select Quiz Type",
        options=["mcq", "mixed"],
        index=0,
        horizontal=True,
        help="Choose between Multiple Choice Questions or a mix of MCQs and Short Answers."
    )
    num_questions = st.slider("Number of Questions", min_value=1, max_value=10, value=5, step=1)

    if st.button("Generate Quiz"):
        if not os.getenv("GEMINI_API_KEY"):
            st.error("Cannot generate quiz: Gemini API Key is missing.")
        else:
            with st.spinner(f"Generating {num_questions} {quiz_type} questions..."):
                try:
                    # Call agent's generate_quiz_from_pdf method
                    quiz_data = asyncio.run(agent.generate_quiz_from_pdf(temp_pdf_path, quiz_type, num_questions))

                    if isinstance(quiz_data, dict) and "error" in quiz_data:
                        st.error(f"Error generating quiz: {quiz_data['error']}")
                        if "raw_response" in quiz_data:
                            with st.expander("Raw LLM Response (for debugging)"):
                                st.code(quiz_data["raw_response"])
                    elif isinstance(quiz_data, list):
                        st.subheader(f"{quiz_type.replace('_', ' ').title()} Quiz:")
                        for i, q in enumerate(quiz_data):
                            st.markdown(f"**Question {i+1}:** {q['q']}")
                            if q["type"] == "mcq":
                                for option in q["options"]:
                                    st.write(option)
                                with st.expander("Show Answer & Explanation"):
                                    st.success(f"Correct Answer: {q['answer']}")
                                    st.info(f"Explanation: {q['explanation']}")
                            elif q["type"] == "short_answer":
                                with st.expander("Show Answer"):
                                    st.success(f"Answer: {q['answer']}")
                            st.markdown("---")
                    else:
                        st.error("Failed to generate quiz in expected format.")
                except Exception as e:
                    st.error(f"An error occurred during quiz generation: {e}")

    # Remove temporary file after use (Streamlit rerun handling)
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
else:
    st.info("Please upload a PDF to get started!")
