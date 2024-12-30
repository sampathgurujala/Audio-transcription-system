import whisper
import os
from pydub import AudioSegment
# Set settings
source = "opto_sessions_ep_69.mp3"

sound = AudioSegment.from_mp3(source) # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

 # We could also chose here .mp3
 # For the sake of comparison with Vosk, I convert it to .wav
 # Extract the first 60 seconds
excrept = sound[0:60000]
output_path = os.path.splitext(source)[0]+"_excerpt.wav"
excrept.export(output_path, format="wav")


model = whisper.load_model("base")
result = model.transcribe("opto_sessions_ep_69_excerpt.wav")
print(result["text"])

