import asyncio
import edge_tts
import pygame
import tempfile
import os
import threading
import time

VOICE = "en-IN-NeerjaNeural"   # Indian Female Voice

pygame.init()
pygame.mixer.init()

speech_thread = None
stop_flag = False


async def generate_speech(text, filename):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)


def _play(text):

    global stop_flag

    stop_flag = False

    fd, filename = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)

    # ----------------------------
    # Generate TTS
    # ----------------------------
    start = time.time()

    asyncio.run(generate_speech(text, filename))

    print(f"🔊 TTS Generation : {time.time() - start:.2f} sec")

    # ----------------------------
    # Start Audio
    # ----------------------------
    start = time.time()

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    print(f"▶ Audio Start     : {time.time() - start:.2f} sec")

    # ----------------------------
    # Wait until speech finishes
    # ----------------------------
    while pygame.mixer.music.get_busy():

        if stop_flag:
            pygame.mixer.music.stop()
            break

        time.sleep(0.05)

    # ----------------------------
    # Cleanup
    # ----------------------------
    try:
        pygame.mixer.music.unload()
    except:
        pass

    try:
        os.remove(filename)
    except:
        pass


def speak(text):

    global speech_thread

    if not text:
        return

    # Stop previous speech if any
    stop()

    speech_thread = threading.Thread(
        target=_play,
        args=(text,),
        daemon=True
    )

    speech_thread.start()


def stop():

    global stop_flag

    stop_flag = True

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    except:
        pass


def speaking():
    return pygame.mixer.music.get_busy()