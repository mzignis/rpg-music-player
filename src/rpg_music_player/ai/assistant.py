import ollama
from pathlib import Path


class YouTubeSearchAssistant:
    def __init__(self):
        self.name = "AI Assistant"
        self.system_types: dict = {
            'convert': 'search.txt',
            'background': 'background.txt',
            'combat': 'combat.txt',
            'collector': 'collector.txt',
        }

    def get_system_prompt(self, input_type) -> dict:
        filename = self.system_types[input_type]
        prompt_filepath: Path = Path(__file__).parent.parent.parent.parent / 'prompts' / filename
        with open(prompt_filepath, 'r') as file:
            prompt_content: str = file.read()

        return {
            'role': 'system',
            'content': prompt_content
        }

    @staticmethod
    def get_user_prompt(user_input: str) -> dict:
        return {
            'role': 'user',
            'content': user_input
        }

    def convert_search_prompt(self, user_input: str) -> str:
        system_message: dict = self.get_system_prompt('convert')
        user_message: dict = self.get_user_prompt(user_input)
        messages: list[dict] = [system_message, user_message]

        response: dict = ollama.chat(model='llama3.2', messages=messages)

        assistant_reply: str = response['message']['content']

        return assistant_reply

    def get_background_prompt(self, user_input: str) -> str:
        system_message: dict = self.get_system_prompt('background')
        user_message: dict = self.get_user_prompt(user_input)
        messages: list[dict] = [system_message, user_message]

        response: dict = ollama.chat(model='llama3.2', messages=messages)

        assistant_reply: str = response['message']['content']

        return assistant_reply

    def get_combat_prompt(self, user_input: str) -> str:
        system_message: dict = self.get_system_prompt('combat')
        user_message: dict = self.get_user_prompt(user_input)
        messages: list[dict] = [system_message, user_message]

        response: dict = ollama.chat(model='llama3.2', messages=messages)

        assistant_reply: str = response['message']['content']

        return assistant_reply

    def select_videos_by_title(self, prompt, titles) -> list:
        system_message: dict = self.get_system_prompt('collector')
        user_input: str = f"Input: {prompt} \nTitles: {titles}"
        user_message: dict = self.get_user_prompt(user_input)
        messages: list[dict] = [system_message, user_message]

        response: dict = ollama.chat(model='llama3.2', messages=messages)

        assistant_reply: list = eval(response['message']['content'])

        return assistant_reply


if __name__ == '__main__':
    pass
