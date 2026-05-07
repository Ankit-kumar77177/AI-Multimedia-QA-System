from app.services.transcription_service import transcribe_file

result = transcribe_file("uploads/sample.mp3")

print(result["text"])

print(result["segments"])