
from TTS.api import TTS
import os

# Load a pre-trained TTS model (en-US female)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def speak(text):
    output_path = "outputs/output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    os.system(f"aplay {output_path}")
