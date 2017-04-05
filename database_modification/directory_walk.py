import os
import json
import re

def pad(num):
    while len(num) < 4:
        num = '0' + num
    return num

for root, directory, files in os.walk('./mp3s'):
    for file in files:
        if not file.startswith('.'):
            mp3num = re.search('\d+', str(file)).group(0)
            mp3num = pad(mp3num)
            os.rename('./mp3s/' + file, './mp3s/' + mp3num + '.mp3')
