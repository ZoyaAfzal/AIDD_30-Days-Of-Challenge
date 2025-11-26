# PDF Summarizer & Quiz Generator Agent

This project implements an AI-powered PDF Summarizer and Quiz Generator Agent using Streamlit, Google Gemini API, and a simulated OpenAgents SDK with Context7 MCP integration. Users can upload a PDF file, get different types of summaries, and generate quizzes (MCQs or mixed questions) based on the document's content.

## Features

-   **PDF Upload & Text Preview**: Upload PDF files and preview the extracted text.
-   **Intelligent Summarization**: Generate concise, bullet-point, or student-friendly summaries using the Google Gemini LLM.
-   **Dynamic Quiz Generation**: Create Multiple Choice Questions (MCQs) or mixed quizzes (MCQs and short answers) from the PDF content, complete with answers and explanations.
-   **Streamlit UI**: An interactive web interface for seamless interaction.
-   **Modular Design**: Separated logic for summarization, quiz generation, and agent orchestration for easy maintenance and scalability.

## Technologies Used

-   **Frontend**: Streamlit
-   **Backend/Agent**:
    -   Google Gemini API (via `google-generativeai`)
    -   OpenAgents SDK (simulated `WorkerAgent` interface)
    -   PyPDF2 (for UI text preview)
    -   `python-dotenv` (for environment variable management)
-   **PDF Text Extraction**: Simulated Context7 MCP integration (placeholder for actual CLI tool calls).

## Project Structure

```
pdf-summarizer-quiz-agent/
│
├── app.py                      # Streamlit UI for interaction
├── summarizer.py               # Logic for generating summaries
├── quiz_generator.py           # Logic for generating quiz questions
├── mcp_setup/                  # Context7 MCP setup scripts (placeholder config)
│ └── context7_config.json
│
├── agents/
│ └── pdf_agent.py              # OpenAgents SDK-like agent orchestrating LLM calls
│
├── examples/
│ └── sample_prompt.txt         # Example prompts for summary and quiz
│
├── gemini_agent_prompt.txt     # Instructions file for Gemini CLI (this agent)
├── requirements.txt            # Python dependencies
├── README.md                   # Project README (this file)
└── .gitignore                  # Git ignore file
```

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    # If this were a real repo:
    # git clone <repository-url>
    # cd pdf-summarizer-quiz-agent
    ```
    *(For this specific task, files are being generated directly.)*

2.  **Create a Virtual Environment and Activate it:**
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Google Gemini API Key:**
    -   Obtain a Google Gemini API Key from the [Google AI Studio](https://aistudio.google.com/app/apikey).
    -   Create a `.env` file in the root of the `pdf-summarizer-quiz-agent` directory (where `app.py` is located) with your API key:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

5.  **Context7 MCP Setup (Conceptual - Actual Integration Required):**
    The project is designed to integrate with Context7 MCP for robust PDF text extraction. While a direct Python SDK for Context7 MCP is not used in this example (it uses a simulated call within `pdf_agent.py`), the `GEMINI.md` specified the following setup command:
    ```bash
    npx -y @upstash/context7-mcp@latest
    ```
    In a full production environment, you would need to ensure Context7 MCP is properly installed and configured, and the `_get_pdf_text_from_mcp` method in `agents/pdf_agent.py` would be updated to interact with it directly (e.g., via a subprocess call or a dedicated Python client if available).

## Running the Application

Once the setup is complete:

1.  **Ensure your virtual environment is activated.**
2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    Your browser should open to the Streamlit application. If not, open your web browser and navigate to the local URL displayed in your terminal (e.g., `http://localhost:8501`).

## Contributing

(This section is a placeholder for actual contribution guidelines)

## License

(This section is a placeholder for license information)
