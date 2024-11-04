import whisper

# Load the Whisper model
model = whisper.load_model("small")  # You can change "small" to another model size if needed

# Transcribe the entire audio file directly
result = model.transcribe("output_audio.mp3", language="pt", task="transcribe", temperature=0.1)

# Print the full transcription
print(result['text'])
