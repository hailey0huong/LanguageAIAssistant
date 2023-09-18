import os
import anthropic
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

MODEL = "claude-2.0"


class ClaudeChat():
    def __init__(self) -> None:
        self.client = anthropic.Anthropic()
        self.chat_history = []
        self.last_response = None
    
    def _write_prompt_for_Claude(self):
        i=0
        prompt = ""
        while i < len(self.chat_history):
            if i%2 == 0:
                prompt = prompt + anthropic.HUMAN_PROMPT + " " + self.chat_history[i]
            else:
                prompt = prompt + anthropic.AI_PROMPT + " " + self.chat_history[i]
            i+=1
            
        prompt += anthropic.AI_PROMPT
        
        return prompt
    
    def _complete_response(self, prompt, max_tokens=1000, temperature=1) -> None:
        response = self.client.completions.create(
            prompt = prompt,
            stop_sequences = [anthropic.HUMAN_PROMPT],
            model=MODEL,
            max_tokens_to_sample=max_tokens,
            temperature=temperature,
        )
        return response

    
    def generate_response(self, prompt:str, max_tokens=1000, temperature=1) -> None:
        self.chat_history.append(prompt)
        final_prompt = self._write_prompt_for_Claude()
        response = self._complete_response(final_prompt, max_tokens=max_tokens, temperature=temperature)
        self.chat_history.append(response.completion)
        self.last_response = response
        self._print_human_prompt(prompt)
        self._print_ai_response()

    
    def reset(self) -> None:
        self.chat_history = []
        self.last_response = None
        
    def _print_human_prompt(self, prompt) -> None:
        print("HUMAN: " + prompt)
    
    def _print_ai_response(self) -> None:
        print("AI: "+ self.chat_history[-1])
