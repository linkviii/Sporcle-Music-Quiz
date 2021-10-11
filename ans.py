import json
from pathlib import Path
import re
import csv

def readj(p):
    # return json.loads(Path(p).read_text('utf-8', errors='ignore'))
    return json.loads(Path(p).read_text('utf-8', errors='replace'))

def get_id(s):    
    s = Path(s).stem
    r = r'_(?P<id>.*)(_[abc])?(\.*)'
    m = re.search(r, s)
    g = m.group('id')
    id = g.split('_')[0]
    return id

def make_db():
    movies = readj(r'C:\Users\viii\Desktop\pi\movies.json')
    db = {}
    for anime in movies:
        s = anime['linkSrc']
        print(s)
        id = Path(s).stem
        db[id] = anime

    Path('db.json').write_text(json.dumps(db, indent=4, ensure_ascii=False), 'utf-8')
    # Path('db.json').write_text(json.dumps(db, indent=4, encoding='utf-8'), 'utf-8')


def as_mss(t):
    m = t//60
    s = t%60
    return f'{m}:{s:02}'

stitch = readj("stitch.json")
db = readj('db.json')

print(len(stitch))
print(len(db))

# ans = csv.writer(open('ans.csv', 'w', encoding='utf-8'))
ans = csv.writer(open('ans.csv', 'w', encoding='utf-8',  newline=''))

for song_tup in stitch:
    id = (get_id(song_tup[0]))
    # print(id)
    stamp = str(as_mss(song_tup[1]))
    if id in db:
        line = [stamp, db[id]["anime"], db[id]["song"] ]
    else:
        line = [stamp, song_tup[0]]
    print(line)
    ans.writerow(line)


# make_db()