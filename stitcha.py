from pathlib import Path
from pydub import AudioSegment

import random
import json

random.seed(42)

gsongs = Path('./normalized').glob("*.mkv")

songs = list(gsongs)
random.shuffle(songs)
songs.reverse()

print((songs[-1]))

it = AudioSegment.from_file(songs[0])
print(it.duration_seconds)

stitch = AudioSegment.empty()

data = []
for song in songs:
    print(song.name)
    start = int(stitch.duration_seconds)
    s = AudioSegment.from_file(song)
    stitch += s
    data.append((song.name, start, round(s.duration_seconds, 1)))


train = AudioSegment.from_file('./good-luck-my-way_oxeadd_a.mkv')

m10 = 60*10

padding = m10 - stitch.duration_seconds - train.duration_seconds

stitch += AudioSegment.silent(padding*1000)
stitch += train

print(json.dumps(data, indent=2))
Path('./stitch.json').write_text(json.dumps(data, indent=2))
print("exporting")
stitch.export('stitch.wav')




