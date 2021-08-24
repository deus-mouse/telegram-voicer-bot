from pydub import AudioSegment

Src = "755294.mp3"
dst = "new.wav"

sound = AudioSegment.from_mp3(Src)
sound.export(dst, format="wav")

