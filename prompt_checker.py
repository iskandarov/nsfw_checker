import re

class PromptChecker:
    def __init__(self):
        self.message = "success"
        self.deepl = DeepLTranslator()
        self.file_path = "general/banned_words.txt"
        self.banned_words = self.load_banned_words()

    def load_banned_words(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []

    async def check_prompt_banned_words(self, prompt):
        words = re.findall(r'\b\w+\b', prompt)

        for banned_word in self.banned_words:
            if " " in banned_word and banned_word in prompt:
                return banned_word
            elif any(word == banned_word for word in words):
                return banned_word
        return None

    async def check_prompt_exact_word(self, prompt):
        with open(self.file_path, 'r') as file:
            file_lines = [line.strip().lower() for line in file.readlines()]

        prompt_words = re.findall(r'\b\w+\b', prompt.lower())

        for word in prompt_words:
            if word in file_lines:
                return word
        return None
