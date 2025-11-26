# PDF Summarizer & Quiz Generator Agent  
### Using Streamlit, OpenAgents SDK, PyPDF, Gemini CLI, and Context7 MCP

---

## 1. Project Overview

This project creates an AI-powered **PDF Summarizer and Quiz Generator** agent.  
Users will upload a PDF file, and the system will:

1. Extract text using **PyPDF**
2. Summarize the document clearly and simply
3. Generate a quiz (MCQs or Mixed questions) using the **original PDF text**, not the summary
4. Display everything inside a **Streamlit UI**
5. Use **Gemini CLI + Context7 MCP** to create the backend agent

This document provides ALL specifications required for Gemini CLI to create the entire project step-by-step.

---

## 2. Tech Stack & Tools

Gemini CLI will create and configure the following:

### **Backend / Agent**
- **Gemini 2.0 Flash Thinking / Pro** (via Gemini CLI)
- **Context7 MCP** (as the document/tool provider)
- **OpenAgents SDK** (optional agent orchestration template)
- PDF extraction using **PyPDF**

### **Frontend**
- **Streamlit** (recommended)
- Optional alternative: HTML/CSS interface

### **Other Tools**
- Python Virtual Environment
- Requirements installation
- GitHub version control

---

## 3. Project Folder Structure (to be created by Gemini CLI)

Gemini CLI must generate the following project structure:

pdf-summarizer-quiz-agent/
│
├── app.py # Streamlit UI
├── summarizer.py # Logic for summarization
├── quiz_generator.py # Quiz creation logic
├── mcp_setup/ # Context7 MCP setup scripts
│ └── context7_config.json
│
├── agents/
│ └── pdf_agent.py # OpenAgents SDK agent template
│
├── examples/
│ └── sample_prompt.txt # Example quiz + summary prompts
│
├── gemini_agent_prompt.txt # The Gemini CLI instructions file
├── gemini.md # THIS FILE
│
├── prompt_screenshots/
│ └── gemini_cli_prompt.png # You must manually add this screenshot
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 4. Requirements File (Gemini CLI must generate this)

Content for `requirements.txt`:

streamlit
pypdf
openai
python-dotenv
requests


---

## 5. Detailed Task Instructions for Gemini CLI

Gemini CLI MUST follow these steps in order:

---

## **STEP 1 — Create Virtual Environment**

Gemini CLI must generate instructions to create and activate:

python -m venv .venv
source .venv/bin/activate (Mac/Linux)
.venv\Scripts\activate (Windows)


---

## **STEP 2 — Generate all Python files**

Gemini CLI must create the following files:

### **app.py**
Streamlit UI that:
- Accepts PDF upload  
- Extracts text via PyPDF  
- Creates summary  
- Creates quiz  
- Displays results  

### **summarizer.py**
Handles:
- PDF text input  
- Clean summary generation  
- Student-friendly formatting  

### **quiz_generator.py**
Generates:
- MCQs  
- Mixed questions  
- JSON output  
- Correct answers & explanations  

### **agents/pdf_agent.py**
Implements:
- OpenAgents SDK template  
- Calls summary + quiz generator  
- Communicates with Context7 MCP  

### **mcp_setup/context7_config.json**
Defines:
- MCP server  
- Tools available  
- PDF reading tool  

---

## 6. PDF Summarization Requirements

The agent must:
- Use full extracted PDF text (not partial)  
- Produce one of 3 formats:
  1. **Concise summary (2 paragraphs)**  
  2. **Bullet-point summary**  
  3. **Student-friendly simple language**

The summary must:
- Remove noise
- Be readable and structured
- Avoid jargon unless needed

---

## 7. Quiz Generator Requirements

When user clicks **Create Quiz**:

The agent must generate:

### **For MCQs**
- 4 options (A, B, C, D)
- One correct answer
- One-line explanation

### **For Mixed Quiz**
- 60% MCQs  
- 40% short answers  

### **Output Format (JSON Array)**

[
{
"type": "mcq",
"q": "What is ...?",
"options": ["A...", "B...", "C...", "D..."],
"answer": "B",
"explanation": "Because..."
}
]

---

## 8. Context7 MCP Instructions

Gemini CLI must configure Context7 MCP:

Install command:

npx -y @upstash/context7-mcp@latest


The agent must call Context7 MCP to read and fetch the **FULL PDF TEXT**.

---

## 9. Streamlit UI Requirements

The UI must include:

### **Upload Section**
- PDF upload widget  
- Extract text preview  

### **Summary Section**
- Style dropdown (concise, detailed, simple)  
- Generate summary button  
- Display summary inside a card  
- Allow summary download  

### **Quiz Section**
- Quiz type selector  
- Question slider  
- Generate quiz button  
- Display MCQs nicely  
- Show correct answers  

---

## 10. GitHub Submission Requirements

Your GitHub repository must contain:

### Mandatory Files
- `gemini.md`
- All Python files
- Requirements file
- Screenshot in `/prompt_screenshots/gemini_cli_prompt.png`
- README.md

---

## 11. Expected Behavior of the Agent

When running, the agent must:

1. Accept instructions from Streamlit UI  
2. Load the PDF into Context7 MCP  
3. Summarize using backend model  
4. Generate quiz based on original PDF text  
5. Return JSON response to Streamlit  
6. Display output cleanly  

---

## 12. Final Gemini CLI Prompt (place inside `gemini_agent_prompt.txt`)

Follow all instructions written in gemini.md.

Create the full project structure, all Python files, MCP setup, Streamlit UI, and logic exactly as described.

Use Context7 MCP as the tool provider for PDF text extraction.

Implement:

app.py

summarizer.py

quiz_generator.py

agents/pdf_agent.py

mcp_setup/context7_config.json

requirements.txt

README.md

Ensure the agent can:

Summarize PDFs using the original text.

Generate quizzes (MCQs or mixed) with JSON output.

Communicate with Streamlit UI.

After creating all files, initialize the project environment exactly per gemini.md.


5. Commit to GitHub

---

## 14. Running the Project

pip install -r requirements.txt
streamlit run app.py


---

# END OF gemini.md

