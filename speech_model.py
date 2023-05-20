from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model('C:\\Users\Manikandan\\Desktop\L-T-main\\vosk-model-en-us-0.22')
recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Dictionary to map words to their replacements
word_replacements = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eye" : "i"
    # Add more word replacements as needed
}

print("Listening...")

while True:
    data = stream.read(4096)
    if len(data) == 0:
        break

    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result_json = json.loads(result)
        recognized_text = result_json["text"]

        # Convert recognized words to integers and apply word replacements
        recognized_numbers = recognized_text.split()
        for i, word in enumerate(recognized_numbers):
            if word.isdigit():
                recognized_numbers[i] = str(int(word))
            elif word in word_replacements:
                recognized_numbers[i] = word_replacements[word]

        # Print the recognized text with spaces
        recognized_text = " ".join(recognized_numbers)
        break

text_2 = recognized_text.replace(" ","")
print (text_2)
