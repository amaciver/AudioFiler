import sqlite3
import requests

conn = sqlite3.connect('main.db')
c = conn.cursor()

c.execute('''SELECT preview_url from tracks''')
index = 0
for row in c:
    print(f"./mp3s/{index}.mp3")
    r = requests.get(row[0])
    with open(f"./mp3s/{index}.mp3", 'wb') as mp3_file:
        mp3_file.write(r.content)
        index += 1
