from tools.utils import ClaudeChat

class LanguageAIAssitant(ClaudeChat):
    def __init__(self) -> None:
        super().__init__()
    
    def _set_system_message(self, system_message=None):
        self.chat_history.append(system_message)
        prompt=self._write_prompt_for_Claude()
        response = self._complete_response(prompt, max_tokens=1000, temperature=1)
        self.chat_history.append(response.completion)
        self.last_response = response

    def generate_learning(self):
        prompt = """
        Please give me a summary of what I learned so far. \
        Please make sure that for each word/ phrase, you note its \
        definition and tips to use. Make it a list for me to review.
        Please start with "Here is what you have learned so far".
        """
        self.chat_history.append(prompt)
        final_prompt = self._write_prompt_for_Claude()
        response = self._complete_response(final_prompt, max_tokens=5000, temperature=1)
        self.chat_history.append(response.completion)
        self.last_response = response
        self._print_ai_response()

    def reset(self) -> None:
        self.generate_learning()
        super().reset()






