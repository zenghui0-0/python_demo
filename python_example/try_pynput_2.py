from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play
import threading
import time
import random
import os


SOUND_FOLDER = "wood_fish"
SPECIL_SOUND = "amituofo"

# collecting sound list to play
SOUND_LIST = []
for root, dirs, files in os.walk(SOUND_FOLDER):
    for f in files:
        if f.endswith(".mp3"):
            file_path = os.path.join(root, f)
            SOUND_LIST.append(file_path)

SPECIL_SOUND_LIST = []
for root, dirs, files in os.walk(SPECIL_SOUND):
    for f in files:
        if f.endswith(".mp3"):
            file_path = os.path.join(root, f)
            SPECIL_SOUND_LIST.append(file_path)

print(SOUND_LIST, SPECIL_SOUND_LIST)

last_key_time = 0
counting = 0
def on_press(key):
    global counting 
    counting += 1
    global last_key_time
    current_time = time.time()
    # 防抖：忽略 0.1 秒内的重复事件
    if current_time - last_key_time < 0.1:
        return
    last_key_time = current_time
    # key_char = key.char.lower()
    # print(f"user input: {key_char}")
    try:
        sound_file = random.choice(SOUND_LIST)
        specil_sound_file = random.choice(SPECIL_SOUND_LIST)
        try:
            if counting % 5 == 0:
                print(f"{counting}")
                play_sound(specil_sound_file)
            else:
                play_sound(sound_file, decibel=-10)
        except Exception as e:
            print(f"Failed to play sound: {sound_file}, error: {e}")
    except AttributeError:
        # 忽略特殊键（如Shift、Ctrl等）
        pass

def play_sound(sound_file, clipps=1000, decibel=0):
    print(f"paly sound_file:{sound_file}")
    # using AudioSegment to load sound file
    sound = AudioSegment.from_file(sound_file)
    # print(rf"clipps {clipps}ms, decibel: {decibel}")
    sound += decibel
    clipped_sound = sound[:clipps]
    threading.Thread(target=play, args=(clipped_sound,)).start()

def on_release(key):
    # press ESC to stop
    if key == keyboard.Key.esc:
        print("stop keyboard listenning...")
        return False

print("start to listenning keyboard input, press ESC to exit...")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
