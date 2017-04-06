import requests

def downloadPreview(url):
    # r = requests.get(preview_url)
    r = requests.get("https://p.scdn.co/mp3-preview/7c548326fe87f76161403d00bbb3b65b988a2c17?cid=null")
    with open("./data/preview.mp3", 'wb') as mp3_file:
        mp3_file.write(r.content)


downloadPreview("https://p.scdn.co/mp3-preview/7c548326fe87f76161403d00bbb3b65b988a2c17?cid=null")
