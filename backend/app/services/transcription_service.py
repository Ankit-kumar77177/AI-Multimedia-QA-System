import whisper

model = whisper.load_model("base")

def transcribe_file(file_path):

    result = model.transcribe(file_path)

    return {
        "text": result["text"],
        "segments": result["segments"]
    }