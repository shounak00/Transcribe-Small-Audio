import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav
filepath= 'C:/Users/User/Desktop/work/B-024/0-15mins.mp3'                                                      
sound = AudioSegment.from_mp3(filepath)
sound.export("a.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "a.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))