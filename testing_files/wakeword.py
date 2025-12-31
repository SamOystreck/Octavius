#Will house speech to text code and methods (if required, still looking into vosk)
import pvporcupine
from dotenv import load_dotenv
import os
from pvrecorder import PvRecorder


load_dotenv()

porcupine = pvporcupine.create(
    access_key=os.getenv("PORCUPINE_ACCESS_KEY"),
    keyword_paths=['picovoice\\Octavius_en_windows_v4_0_0.ppn']
)

recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

try:
    recorder.start()

    while True:
        frame = recorder.read()
        keyword_index = porcupine.process(recorder.read())
        if keyword_index >= 0:
            print(f"Detected")
            #start sending audio to vosk processor (websocket)

except KeyboardInterrupt:
    recorder.stop()
finally:
    porcupine.delete()
    recorder.delete()
