from playsound import playsound
from threading import Thread, Lock
from src.const import SUCCESS_SOUND, END_TASK_SOUND
# playsound version ==1.2.2
sound_lock = Lock()

def play_sound(path):
    def play():
        print("Playing", path)
        try:
            with sound_lock:
                playsound(path)
        except Exception as e:
            print("Error while playing sound:", e)

    if path == END_TASK_SOUND and sound_lock.locked():
        sound_lock.release()

    if not sound_lock.locked():
        sound_thread = Thread(target=play)
        sound_thread.start()
