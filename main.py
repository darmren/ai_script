import whisper

model = whisper.load_model("base")
result = model.transcribe("path_to_file")#указать путь до файла на диске
print(result["text"])

with open('text.txt', 'w') as file:
    file.write(result)
