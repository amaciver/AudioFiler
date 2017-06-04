import sqlite3
import requests

r = requests.post(
    'https://accounts.spotify.com/api/token',
    data={'grant_type':'client_credentials'},
    headers={'Authorization': 'Basic MmVmM2JlZTRmNDdhNGM1M2E1OTMyNjU5ZDAxMjUyYjI6YzdjYjFlNjEzNDJjNDM0NjljYTJlM2M0OTBiZTY3N2I='}
    )

# print(r.json()['access_token'])
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS tokens''')
c.execute('''CREATE TABLE tokens (id INTEGER PRIMARY KEY, token TEXT)''')
c.execute('''INSERT INTO tokens(token) VALUES(?)''', (r.json()['access_token'],))
conn.commit()
conn.close()
