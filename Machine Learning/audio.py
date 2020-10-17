import pyglet
import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

'''
file = pyglet.resource.media('audio/wet.mp3')
file.play()

pyglet.app.run()
'''

running = True

def say(text):
    subprocess.call('say '+ text)



def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening...")
    play_audio("./audio/audio_initiate.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("./audio/audio_end.wav")

    command=""
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro")

    print("Your command ", command)
    if command in ["quit","bye", "exit", "goodbye"]:
        global running
        running = False
    cmd.discover(command)
    #say('You said: ' + command)

while running == True
     initSpeech()
