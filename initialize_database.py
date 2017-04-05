import sqlite3
import os
import json
import requests
import pdb

# map common variations of genres to our consistent version
ACCEPTED_GENRES = {
    'Alternative': 'Alternative',
    'Alternative Rock': 'Alternative',
    'Alternative rock': 'Alternative',
    'Alt Rock': 'Alternative',
    'Alt rock': 'Alternative',
    'Alt. Rock': 'Alternative',
    'Alt. rock': 'Alternative',
    'alternative': 'Alternative',
    'alternative rock': 'Alternative',
    'alt rock': 'Alternative',
    'alt. rock': 'Alternative',
    'Blues': 'Blues',
    'blues': 'Blues',
    'blues rock': 'Blues',
    'Classical': 'Classical',
    'classical': 'Classical',
    'Alt-country': 'Country',
    'Country': 'Country',
    'country': 'Country',
    'D&B': 'D&B',
    'D&b': 'D&B',
    'Drum And Bass': 'D&B',
    'Drum and Bass': 'D&B',
    'Drum and bass': 'D&B',
    'd&b': 'D&B',
    'drum and bass': 'D&B',
    'Disco': 'Disco',
    'disco': 'Disco',
    'Dubstep': 'Dubstep',
    'dubstep': 'Dubstep',
    'Electronic': 'Electronic',
    'Electronica': 'Electronic',
    'electronic': 'Electronic',
    'electronica': 'Electronic',
    'electro': 'Electronic',
    'Techno': 'Electronic',
    'techno': 'Electronic',
    'Folk': 'Folk',
    'folk': 'Folk',
    'Funk': 'Funk',
    'funk': 'Funk',
    'Hip-Hop': 'Hip-Hop',
    'Hip/Hop': 'Hip-Hop',
    'Hip Hop': 'Hip-Hop',
    'HipHop': 'Hip-Hop',
    'Hip-hop': 'Hip-Hop',
    'Hip/hop': 'Hip-Hop',
    'Hip hop': 'Hip-Hop',
    'Hiphop': 'Hip-Hop',
    'hip-hop': 'Hip-Hop',
    'hip/hop': 'Hip-Hop',
    'hip hop': 'Hip-Hop',
    'hiphop': 'Hip-Hop',
    'House': 'House',
    'EDM/House': 'House',
    'EDM': 'House',
    'house': 'House',
    'deep house': 'House',
    'electro house': 'House',
    'tech house': 'House',
    'Indie': 'Indie',
    'Independent': 'Indie',
    'Indie Rock': 'Indie',
    'Indie rock': 'Indie',
    'indie': 'Indie',
    'indie pop': 'Indie',
    'independent': 'Indie',
    'indie rock': 'Indie',
    'Jazz': 'Jazz',
    'Smooth Jazz': 'Jazz',
    'jazz': 'Jazz',
    'Metal': 'Metal',
    'Death-Metal': 'Metal',
    'Death Metal': 'Metal',
    'Death-metal': 'Metal',
    'Death metal': 'Metal',
    'Heavy Metal': 'Metal',
    'Heavy metal': 'Metal',
    'heavy metal': 'Metal',
    'Power Metal': 'Metal',
    'Power metal': 'Metal',
    'power metal': 'Metal',
    'Thrash Metal': 'Metal',
    'Thrash metal': 'Metal',
    'thrash metal': 'Metal',
    'doom metal': 'Metal',
    'Progressive Metal': 'Metal',
    'Progressive metal': 'Metal',
    'progressive metal': 'Metal',
    'metal': 'Metal',
    'death metal': 'Metal',
    'death-metal': 'Metal',
    'black metal': 'Metal',
    'Pop': 'Pop',
    'pop': 'Pop',
    'Punk': 'Punk',
    'Punk Rock': 'Punk',
    'Punk rock': 'Punk',
    'punk': 'Punk',
    'punk rock': 'Punk',
    'hardcore punk': 'Punk',
    'post-punk': 'Punk',
    'RB': 'R&B',
    'R&B': 'R&B',
    'RandB': 'R&B',
    'R And B': 'R&B',
    'R and B': 'R&B',
    'R and b': 'R&B',
    'rhythm and blues': 'R&B',
    'r&b': 'R&B',
    'rnb': 'R&B',
    'randb': 'R&B',
    'r and b': 'R&B',
    'Rap': 'Rap',
    'rap': 'Rap',
    'Gangsta Rap': 'Rap',
    'Rap/Hip-Hop': 'Rap',
    'Rap/Hip Hop': 'Rap',
    'Rap/Hip-hop': 'Rap',
    'Rap/Hip hop': 'Rap',
    'rap/hip-hop': 'Rap',
    'rap/hip hop': 'Rap',
    'Reggaeton': 'Reggaeton',
    'reggaeton': 'Reggaeton',
    'Reggae': 'Reggae',
    'reggae': 'Reggae',
    'Rock': 'Rock',
    'Rock and Roll': 'Rock',
    'rock n roll': 'Rock',
    'rock': 'Rock',
    'Hard Rock': 'Rock',
    'Hard rock': 'Rock',
    'hard rock': 'Rock',
    'Salsa': 'Salsa',
    'salsa': 'Salsa',
    'Ska': 'Ska',
    'ska': 'Ska',
    'Soul': 'Soul',
    'soul': 'Soul',
    'Hard Trance': 'Trance',
    'Trance': 'Trance',
    'trance': 'Trance',
    'psytrance': 'Trance',
    }

# create new database
conn = sqlite3.connect('main.db')
c = conn.cursor()

# c.execute('''DROP TABLE IF EXISTS tracks''')
# c.execute('''CREATE TABLE tracks (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, genre TEXT, preview_url TEXT)''')
# iterate through the directory, check the top 3 tags, and use the first one that is in our list as the genre.
# if it has none, skip it. Otherwise, send a query to spotify with the title and artist, and retreive the preview URL.
# if the query to spotify comes back empty, continue to the next one.
count = 0
for root, directory, files in os.walk('./lastfm_train'):
    for file in files:
        # take care of .ds_store
        if file.startswith('.'):
            continue
        with open(root + '/' + file) as data_file:
            data = json.load(data_file)
            track_title = data['title']
            track_artist = data['artist']
            genre1 = None
            genre2 = None
            genre3 = None

            try:
                genre1 = data['tags'][0][0]
                genre2 = data['tags'][1][0]
                genre3 = data['tags'][2][0]
            except IndexError:
                pass

            make_query = True

            if genre1 in ACCEPTED_GENRES:
                genre = genre1
            elif genre2 in ACCEPTED_GENRES:
                genre = genre2
            elif genre3 in ACCEPTED_GENRES:
                genre = genre3
            else:
                make_query = False

            if make_query:
                count += 1
                print(count, file)
                base_url = "https://api.spotify.com/v1/search?q="
                title = f"track:\"{data['title']}\""
                if '&' in title:
                    title = 'and'.join(title.split('&'))
                artist = f"artist:\"{data['artist']}\""
                if '&' in artist:
                    artist = 'and'.join(artist.split('&'))
                response = requests.get(base_url + title + "%20" + artist + "&type=track&limit=1")
                if response.status_code == 429:
                    print(response.text)
                    print(response.json())
                    print("hit 429 level error, committing what we have")
                    print(file)
                    conn.commit()
                    conn.close()
                try:
                    preview_url = response.json()['tracks']['items'][0]['preview_url']
                    track = (track_title, track_artist, ACCEPTED_GENRES[genre], preview_url)
                    c.execute('''INSERT INTO tracks(title, artist, genre, preview_url) VALUES(?,?,?,?)''', track)
                except IndexError:
                    print('deleted: ' + track_title + ' by ' + track_artist + file)
                    os.remove(root + '/' + file)
                except KeyboardInterrupt:
                    conn.commit()
                    conn.close()
                    print(file)
                    exit(0)
                except:
                    conn.commit()
                    print('deleted: ' + track_title + ' by ' + track_artist + file)
                    os.remove(root + '/' + file)


conn.commit()
conn.close()
