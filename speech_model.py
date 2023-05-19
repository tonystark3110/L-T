#
#
#from vosk import Model , KaldiRecognizer
#import pyaudio
#
#model = Model('C:\\Users\\20325730\\Desktop\\speech_rec\\vosk-model-en-us-0.22')
#recognizer = KaldiRecognizer(model , 16000)
#
#cap = pyaudio.PyAudio()
#stream = cap.open (format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
#stream.start_stream()
#
#while True:
#    data = stream.read(4096)
#    if len(data) == 0:
#        break
#
#    if recognizer.AcceptWaveform(data):
#        print(recognizer.Result())


from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model('C:\\Users\\20325730\\Desktop\\speech_rec\\vosk-model-en-us-0.22')
recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Listening...")

while True:
    data = stream.read(4096)
    if len(data) == 0:
        break

    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result_json = json.loads(result)
        recognized_text = result_json["text"]
        print(recognized_text)
        break

# Stop the audio stream
stream.stop_stream()
stream.close()
cap.terminate()
       