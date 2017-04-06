import sqlite3
import requests

conn = sqlite3.connect('../main.db')
c = conn.cursor()


def pad(num):
    while len(num) < 6:
        num = '0' + num
    return num
c.execute('''SELECT id, genre, preview_url from tracks offset 35422''')
for row in c:
    index = str(row[0])
    genre = row[1]
    preview_url = row[2]
    print(f"/Volumes/Seagate\ Expansion\ Drive/mp3s/{pad(index)}.mp3", genre)
    r = requests.get(preview_url)
    with open(f"/Volumes/Seagate Expansion Drive/mp3s/{pad(index)}.mp3", 'wb') as mp3_file:
        mp3_file.write(r.content)
