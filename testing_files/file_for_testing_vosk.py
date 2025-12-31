import json
from vosk import Model, KaldiRecognizer
from pvrecorder import PvRecorder
from array import array

#Things to address - large boot time when starting up audio recognition
#                  - tendancy to just throw "the" in there for no reason at the start
#                  - Need to add some custom words it won't recognize

# Load Vosk model
hertz = 16000
vosk_model = Model("vosk-model-en-us-0.22(1.8G)")
kaldi_recognier = KaldiRecognizer(vosk_model, hertz)


# Initialize PvRecorder
recorder = PvRecorder(device_index=-1, frame_length=512)  # -1 = default mic
recorder.start()
print("Listening... Press Ctrl+C to stop")

# Skip the first few frames to avoid spurious "the"
skip_frames = 2
frame_count = 0

try:
    while True:
        # Read a frame from the microphone
        frame = recorder.read()

        # Convert list[int16] -> bytes for Vosk
        data = array('h', frame).tobytes()

        # Increment frame counter and skip first frames
        frame_count += 1
        if frame_count <= skip_frames:
            continue  # ignore first frames

        # Feed to Vosk recognizer
        if kaldi_recognier.AcceptWaveform(data):
            result = json.loads(kaldi_recognier.Result())
            print(result.get("text", ""))
        else:
            pass
            # result = json.loads(recog.PartialResult())
            # print(result.get("partial", ""), end="\r")  # optional partial display

except KeyboardInterrupt:
    print("\nStopped by user")
finally:
    recorder.stop()
    recorder.delete()