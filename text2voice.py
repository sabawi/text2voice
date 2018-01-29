# python 3+ only
import os
import platform

import pyttsx3
from gtts import gTTS

PLATFORM = platform.system().lower()
OS_RELEASE = platform.release()

# Setup pytts voice engine
pytts = pyttsx3.init()
pyttsVolume = pytts.getProperty('volume')
pytts.setProperty('volume', 1.25)
pyttsRate = pytts.getProperty('rate')
pytts.setProperty('rate', 150)
pytts.setProperty('voice', 'english')
pyttsVoices = pytts.getProperty('voices')

pytts.setProperty('voice', pyttsVoices[1])
PROMPT = 'Type something>>'


def linuxVoices(line):
    # Uses google's gtts package
    tts = gTTS(text=line, lang='en')
    tts.save('line.mp3')
    os.system("mpg321 -q line.mp3")
    os.remove('line.mp3')


def windowsVoices(line):
    # Uses pyttsx3 package
    pytts.say(line)
    pytts.runAndWait()


def main():
    ptatform2voice = \
        {
            'linux': linuxVoices,
            'windows': windowsVoices
        }

    inp = input(PROMPT)
    while (not inp == '!q'):
        ptatform2voice[PLATFORM](inp)
        inp = input(PROMPT)


main()
