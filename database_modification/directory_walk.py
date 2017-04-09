import os
import json
import re

# by padding filenames we can ensure that the feature extraction and
# other scripts iterate over them in a consistent and linear order
def pad(num):
    while len(num) < 4:
        num = '0' + num
    return num

limit = 2000
index = 0
folder = 3
for root, directory, files in os.walk('/Volumes/Seagate Expansion Drive/AudioFiler/mp3s'):
    # ensure that files are iterated over start with 000001.mp3
    for file in sorted(files):
        if not file.startswith('.') and index < limit:
            print('moving ' + root + '/' + file + ' to ' + f'/Volumes/Seagate Expansion Drive/AudioFiler/batches/batch_{folder}/' + file)
            os.rename(root + '/' + file, f'/Volumes/Seagate Expansion Drive/AudioFiler/batches/batch_{folder}/' + file)
            index += 1
            # mp3num = re.search('\d+', str(file)).group(0)
            # mp3num = pad(mp3num)
            # os.rename('./mp3s/' + file, './mp3s/' + mp3num + '.mp3')
        else:
            index = 0
            folder += 1
            print('moving ' + root + '/' + file + ' to ' + f'/Volumes/Seagate Expansion Drive/AudioFiler/batches/batch_{folder}/' + file)
            index += 1
            os.rename(root + '/' + file, f'/Volumes/Seagate Expansion Drive/AudioFiler/batches/batch_{folder}/' + file)
