import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("transcript.mp3")
sound.export("transcript.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source and output clarity percentage                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + str(r.recognize_google(audio, language='en-US', show_all=True)))
        
#search for inefficiencies
i = str(r.recognize_google(audio, language='en-US', show_all=True))
if "this" in i:
        print("Instead of saying \"this\", say that")  
