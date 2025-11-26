import json
import textwrap

class QuizGenerator:
    def __init__(self, llm_model):
        """
        Initializes the QuizGenerator with a language model.
        The LLM model is expected to be an object with a 'generate_content' method.
        """
        self.llm_model = llm_model

    def _generate_mcq_prompt(self, text, num_questions=5):
        """
        Generates a prompt for the LLM to create multiple-choice questions.
        """
        prompt = textwrap.dedent(f"""
        From the following text, generate {num_questions} multiple-choice questions (MCQs).
        Each MCQ should have 4 options (A, B, C, D), one correct answer, and a one-line explanation for the correct answer.
        The questions should be challenging and cover key concepts from the text.
        Provide the output as a JSON array of objects, where each object has the following structure:
        {{
            "type": "mcq",
            "q": "Question text?",
            "options": ["A. Option A", "B. Option B", "C. Option C", "D. Option D"],
            "answer": "B",
            "explanation": "Because..."
        }}

        Ensure the JSON output is valid and can be directly parsed.
        Text:
        ---
        {text}
        ---
        JSON Output:
        """)
        return prompt

    def _generate_mixed_quiz_prompt(self, text, num_questions=5):
        """
        Generates a prompt for the LLM to create a mixed quiz (60% MCQs, 40% short answers).
        """
        num_mcq = int(num_questions * 0.6)
        num_short_answer = num_questions - num_mcq

        prompt = textwrap.dedent(f"""
        From the following text, generate a mixed quiz with {num_questions} questions.
        {num_mcq} questions should be multiple-choice (MCQs) and {num_short_answer} questions should be short answer questions.

        For MCQs:
        - Each MCQ should have 4 options (A, B, C, D), one correct answer, and a one-line explanation.
        - Structure as: {{"type": "mcq", "q": "Question text?", "options": ["A. Opt A", "B. Opt B", "C. Opt C", "D. Opt D"], "answer": "B", "explanation": "Because..."}}

        For short answer questions:
        - Provide the question and a brief, correct answer.
        - Structure as: {{"type": "short_answer", "q": "Question text?", "answer": "Brief correct answer."}}

        Ensure the questions are challenging and cover key concepts from the text.
        Provide the entire output as a single JSON array of objects.
        Ensure the JSON output is valid and can be directly parsed.
        Text:
        ---
        {text}
        ---
        JSON Output:
        """)
        return prompt

    def generate_quiz(self, text, quiz_type="mcq", num_questions=5):
        """
        Generates a quiz (MCQs or mixed) from the given text.
        """
        if not text:
            return "No text provided for quiz generation."

        if quiz_type == "mcq":
            prompt = self._generate_mcq_prompt(text, num_questions)
        elif quiz_type == "mixed":
            prompt = self._generate_mixed_quiz_prompt(text, num_questions)
        else:
            raise ValueError("Invalid quiz_type. Must be 'mcq' or 'mixed'.")

        try:
            response = self.llm_model.generate_content(prompt)
            # Assuming the LLM returns text that is a JSON string
            quiz_json_string = response.text
            # Attempt to parse the JSON string. LLMs can sometimes add conversational text.
            # We'll try to extract the JSON part.
            try:
                # Basic attempt: look for the first '{' and last '}'
                first_brace = quiz_json_string.find('[')
                last_brace = quiz_json_string.rfind(']')
                if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
                    quiz_json_string = quiz_json_string[first_brace : last_brace + 1]
                return json.loads(quiz_json_string)
            except json.JSONDecodeError as e:
                return {"error": f"Failed to parse JSON from LLM response: {e}", "raw_response": quiz_json_string}
        except Exception as e:
            return {"error": f"Error generating quiz: {e}"}
