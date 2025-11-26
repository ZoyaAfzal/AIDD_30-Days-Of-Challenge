import textwrap

class Summarizer:
    def __init__(self, llm_model):
        """
        Initializes the Summarizer with a language model.
        The LLM model is expected to be an object with a 'generate_content' method.
        """
        self.llm_model = llm_model

    def _generate_prompt(self, text, summary_type):
        """
        Generates the appropriate prompt for the LLM based on the desired summary type.
        """
        if summary_type == "concise":
            prompt = textwrap.dedent(f"""
            Please provide a concise summary of the following text in two paragraphs.
            Ensure the summary is clean, meaningful, readable, structured, and avoids jargon where possible.
            Text:
            ---
            {text}
            ---
            Concise Summary:
            """)
        elif summary_type == "bullet_points":
            prompt = textwrap.dedent(f"""
            Please provide a summary of the following text in bullet points.
            Ensure the summary is clean, meaningful, readable, structured, and avoids jargon where possible.
            Text:
            ---
            {text}
            ---
            Bullet Point Summary:
            """)
        elif summary_type == "student_friendly":
            prompt = textwrap.dedent(f"""
            Please provide a student-friendly summary of the following text in simple language.
            Ensure the summary is clean, meaningful, readable, structured, and avoids jargon where possible.
            Text:
            ---
            {text}
            ---
            Student-Friendly Summary:
            """)
        else:
            raise ValueError("Invalid summary_type. Must be 'concise', 'bullet_points', or 'student_friendly'.")
        return prompt

    def generate_summary(self, text, summary_type):
        """
        Generates a summary of the given text using the specified summary type.
        """
        if not text:
            return "No text provided for summarization."

        prompt = self._generate_prompt(text, summary_type)
        try:
            # The actual LLM call is expected to happen here.
            # In the final integrated system, self.llm_model will be the Gemini model
            # and generate_content will be its method.
            response = self.llm_model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating summary: {e}"
