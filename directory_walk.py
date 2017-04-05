import os
import json


for root, directory, files in os.walk('./lastfm_train/A/Q/M'):
    for file in files:
        if not file.startswith('.'):
            with open(root + '/' + file) as data_file:
                data = json.load(data_file)
                print(data['title'], data['artist'], file)
