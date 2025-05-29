import openai_whisper as whisper
from transformers import pipeline
import numpy as np

# Audio narration to text using Whisper
def audio_to_text(video_path):
    try:
        model = whisper.load_model("small")
        result = model.transcribe(video_path)
        return result["text"]
    except FileNotFoundError:
        return "Video file not found. Please provide a valid video file."

# Generate summary using Llama (simulated with OPT-350m)
def generate_summary(audio_text, video_features):
    generator = pipeline("text-generation", model="facebook/opt-350m")  # Llama placeholder
    prompt = f"Summarize this video content: {audio_text} (Features: {video_features.shape})"
    summary = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return summary
