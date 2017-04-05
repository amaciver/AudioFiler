import sqlite3
import requests

conn = sqlite3.connect('main.db')
c = conn.cursor()

c.execute('''SELECT id, genre, preview_url from tracks limit 1000''')
for row in c:
    index = row[0]
    genre = row[1]
    preview_url = row[2]
    print(f"./mp3s/{index}.mp3")
    r = requests.get(preview_url)
    with open(f"./mp3s/{index}.mp3", 'wb') as mp3_file:
        mp3_file.write(r.content)
