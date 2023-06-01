import pyttsx3
from gtts import gTTS
import sys
import os

def linux_voices(line):
    # Uses Google's gTTS package
    tts = gTTS(text=line, lang='en')
    tts.save('line.mp3')
    os.system("mpg321 -q line.mp3")
    os.remove('line.mp3')

def windows_voices(line):
    # Uses pyttsx3 package
    pytts.say(line)
    pytts.runAndWait()

def get_char():
    """Get a single character from standard input"""
    import tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    pytts = pyttsx3.init()
    pytts.setProperty('volume', 1.25)
    pytts.setProperty('rate', 150)
    pytts.setProperty('voice', 'english')
    pytts_voices = pytts.getProperty('voices')
    pytts.setProperty('voice', pytts_voices[1])

    platform2voice = {
        'linux': linux_voices,
        'windows': windows_voices
    }

    prompt = 'Type something: '

    print(prompt, end='', flush=True)
    while True:
        line = ""
        while True:
            ch = get_char()
            line += ch
            print(ch, end='', flush=True)
            if ch == '\n' or ch == '\r': 
                print("\n")
                break
        
        if line.lower().strip() in ("-q", "-quit"):
            print("Bye!")
            break
        elif len(line.strip()) > 0:
            platform2voice[sys.platform](line)
            print(prompt, end='', flush=True)

if __name__ == '__main__':
    main()


