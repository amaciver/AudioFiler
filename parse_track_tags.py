import os
import json

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
    'punk': 'punk',
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

new_genres = {}
our_genres = {}

total = 0
missed = 0
deleted = 0
# the lastfm_train directory is far too big to push up.
# this file was both a test script for iteration over folders to see how long
# it would take to iterate over the entire database. It also served to
# delete the entirity of the track files with no tags.
# the result is a count of how many tracks were iterated over,
# how many tracks had tags that we didn't account for or didn't use, and
# a list of each of our genres with the associated count of songs tagged
# with that genre.
for root, directory, files in os.walk('./lastfm_train'):
    for file in files:
        if not file.startswith('.'):
            with open(root + "/" + file) as data_file:
                data = json.load(data_file)
                if len(data['tags']) > 0:
                    genre1 = None
                    genre2 = None
                    genre3 = None
                    try:
                        genre1 = data['tags'][0][0]
                        genre2 = data['tags'][1][0]
                        genre3 = data['tags'][2][0]
                    except IndexError:
                        pass
                    total += 1
                    if genre1 in ACCEPTED_GENRES:
                        if ACCEPTED_GENRES[genre1] not in our_genres:
                            our_genres[ACCEPTED_GENRES[genre1]] = 0
                        else:
                            our_genres[ACCEPTED_GENRES[genre1]] += 1
                    elif genre2 in ACCEPTED_GENRES:
                        if ACCEPTED_GENRES[genre2] not in our_genres:
                            our_genres[ACCEPTED_GENRES[genre2]] = 0
                        else:
                            our_genres[ACCEPTED_GENRES[genre2]] += 1
                    elif genre3 in ACCEPTED_GENRES:
                        if ACCEPTED_GENRES[genre3] not in our_genres:
                            our_genres[ACCEPTED_GENRES[genre3]] = 0
                        else:
                            our_genres[ACCEPTED_GENRES[genre3]] += 1
                    else:
                        missed += 1
                # if the file has no tags, delete it so we don't have to deal with it in the future
                else:
                    os.remove(root + "/" + file)
                    deleted += 1
sum1 = 0
for genre, count in our_genres.items():
    sum1 += count
    print(genre, count)
print(total)
print(missed)
print(sum1)
