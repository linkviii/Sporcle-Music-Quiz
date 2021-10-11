# Sporcle-Music-Quiz
Notes for making a music quiz


Got a db of songs like this (`movies.json`):

```json
[
  {
    "type": "Ending 1",
    "song": "Kaneda",
    "artist": "Geinoh Yamashiro-gumi",
    "linkSrc": "https://..../ps4so0.mp3",
    "anime": "Akira"
  },
  {
    "type": "Ending 1",
    "song": "Sen no Yoru wo Koete",
    "artist": "Aqua Timez",
    "linkSrc": "https://..../g4gk06.mp3",
    "anime": "Bleach the Movie: Memories of Nobody"
  },
]
```

Download the mp3 files as song_id (`get.py`).

Go through every song looking for interesting samples.

* Plop the mp3 into audacity
* Scrub for interesting samples
* Copy interesting samples into another audacity window
* Save project as song_id.au
* Select ~15s and export the selection as song_id.wav

Normalize the audio levels: `ffmpeg-normalize wav/*`

Stitch the normalized clips into a single wave file. Log the start time and duration of each sample. `stitcha.py` → `stitch.json`


```json
[
  ["good-luck-my-way_oxeadd_b.mkv", 0, 20.0],
  ["against-the-abyss_4ugi1b.mkv", 20, 10.0],
  ["lost-heaven_n1a7wj.mkv", 30, 15.0],
]
```  

Generate thumbnails for each song with song # and timestamp: `thumb.py` → `frames.txt`

Join the thumbnails and the audio: `ffmpeg -f concat -i frames.txt -i ../yes/stitch.wav  out.mp4`

Upload to youtube and hope it doesn't get blocked...

Create answer csv for import into sporcle. `ans.py`. **Next time:** Use tsv instead. The importer does not handle quoted commas. Format: Timestamp, answer, extra info.

Extra answers are deliminated with `/`.


---

https://github.com/jiaaro/pydub/blob/master/API.markdown

https://trac.ffmpeg.org/wiki/Slideshow

https://github.com/slhck/ffmpeg-normalize

