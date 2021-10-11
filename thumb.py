from PIL import Image, ImageDraw, ImageFont
import json
from pathlib import Path


colors = ["#8d6a9f","#0c0a3e","#453823","#d58936","#d7816a"]



f = r"C:\Windows\Fonts\comic.ttf"
fnt = ImageFont.truetype(f, 300)


def draw(n, stamp, bg):
    img = Image.new('RGB', (1280, 720), color = bg)

    d = ImageDraw.Draw(img)

    ns = f'{n:02}'
    t = f'{ns}) {stamp}'

    p = (20,40)
    d.text(p, t, font=fnt, fill=(255, 255, 255))
    
    img.save(f'{ns}.png')


pstitch = r"C:\Users\viii\Desktop\pi\movies\yes\stitch.json"
stitch = json.loads(Path(pstitch).read_text())

print(stitch[0])

def as_mss(t):
    m = t//60
    s = t%60
    return f'{m}:{s:02}'

frames = []

i = 0
for song in stitch:
    bg = colors[i%len(colors)]
    i += 1
    stamp = as_mss(song[1])
    draw(i,stamp, bg)

    fn = f'{i:02}.png'
    d = song[2]

    frames.append(f"file '{fn}'")
    frames.append(f"duration {d}")

frames.append(frames[-2])
f = '\n'.join(frames)

Path("frames.txt").write_text(f)