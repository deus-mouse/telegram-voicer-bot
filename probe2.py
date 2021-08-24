import os
import pydub
import glob


ogg_files = glob.glob('*.ogg')
print(ogg_files)

for ogg_file in ogg_files:
    print(ogg_file)
    wav_file = os.path.splitext(ogg_file)[0] + '.wav'
    print(wav_file)
    sound = pydub.AudioSegment.from_ogg(ogg_file)
    print("sound", sound)
    sound.export(wav_file, format="wav")
    os.remove(ogg_file)
print("done")


