import sqlite3
import numpy as np

conn = sqlite3.connect("/Volumes/Seagate Expansion Drive/AudioFiler/main.db")
c = conn.cursor()

GENRES = {
   'Alternative': 0,
   'Blues': 1,
   'Classical': 2,
   'Country': 3,
   'D&B': 4,
   'Disco': 5,
   'Dubstep': 6,
   'Electronic': 7,
   'Folk': 8,
   'Funk': 9,
   'Hip-Hop': 10,
   'House': 11,
   'Indie': 12,
   'Jazz': 13,
   'Metal': 14,
   'Pop': 15,
   'Punk': 16,
   'R&B': 17,
   'Rap': 18,
   'Reggaeton': 19,
   'Reggae': 20,
   'Rock': 21,
   'Salsa': 22,
   'Ska': 23,
   'Soul': 24,
   'Trance': 25
}

c.execute('''SELECT genre, id from tracks''')
master_array = []
for row in c:
    print(row)
    one_hot = [0.] * 26
    genre = row[0]
    index = GENRES[genre]
    one_hot[index] = 1.
    master_array.append(one_hot)
np.savetxt("/Volumes/Seagate Expansion Drive/AudioFiler/one_hot_genre_tags.txt", master_array)
