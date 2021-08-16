# check out the video I made on this topic
# https://youtu.be/yPhH0Fw_GFM
# make the necessary changes according to your need

#pip install gtts --> gtts is the google text to speech package
#pip install pyglet --> pyglet is the media manager for python
from gtts import gTTS
import pyglet
import os
from time import sleep

def say(sentence):
    #this function uses gtts to speak whatever is in the argument
    output=gTTS(text=sentence,lang='en',slow=False) # get the audio from google
    filename="temp.mp3"  # filename of the file where we will save the audio that we got from google
    output.save(filename) # saving the audio
    voice=pyglet.media.load(filename,streaming=True) # now we open that audio file with pyglet
    voice.play() # we play the audio file
    sleep(voice.duration)   # wait till the audio is played completely
    os.remove(filename) # delete the temporary audio file, otherwise it will take up a lot of memory

say("Replace this with whatever you want the computer to say")
# we pass the sentence that we want to be said, as an argument to the function say , that we defined earlier
#you can call this function as many times you want ..anywhere in the program...

