import requests
import json
import time as stdtime

import unicodedata
import re
from pathlib import Path
import sys


# sys.exit(1)

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


url = "https://.../8l3ktn.mp3"
name = "Voice ~Tadoritsuku Ba~sh/o~"

# name = slugify(name) + '_' + Path(url).name

# r = requests.get(url)
# Path(name).write_bytes(r.content)

movie_file = Path(r"C:\Users\viii\Desktop\pi\movies.json")
movie_dir = Path(r"C:\Users\viii\Desktop\pi\movies")

move_list = json.loads(movie_file.read_text('utf-8'))


movie = move_list[0]
for movie in move_list:
    print(movie)

    fname = slugify(movie["song"]) + '_' + Path(movie['linkSrc']).name
    dst = movie_dir / fname

    stdtime.sleep(45)

    r = requests.get(movie['linkSrc'])
    dst.write_bytes(r.content)

    print(dst)
