from core.llm_runner import query_ollama
from plugins.dirty_talk import spice_up
from tts.synth import speak
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

while True:
    user_input = input("You: ")
    if not user_input.strip():
        continue
    response = query_ollama(user_input, model=config["model"])

    if config["nsfw"]:
        response = spice_up(response)

    print("Bot:", response)
    if config["tts"]:
        speak(response)
