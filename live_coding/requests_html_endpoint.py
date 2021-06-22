import re
import requests
from lxml import html
from requests_html import HTMLSession
from unidecode import unidecode

headers = {
    'authority': 'kerve.last.fm',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'accept': '*/*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'origin': 'https://www.last.fm',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.last.fm/',
    'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
}

params = (
    ('type', 'artist'),
    ('tracks', '1'),
    ('nr', '30'),
    ('format', 'json'),
)

response = requests.get('https://kerve.last.fm/kerve/charts', headers=headers, params=params)

data_json = response.json()
artists_elems = data_json['results']['artist']
artists = [artist['name'] for artist in artists_elems]

for artist in artists:
    print(artist)
    artist = unidecode(artist)
    main_url = 'https://www.letras.mus.br'
    url = main_url + '/' + artist
    response = requests.get(url)

    tree = html.fromstring(response.text)
    songs_tags = tree.xpath('//a[@class="song-name"]')

    songs_urls = [song.get('href') for song in songs_tags]

    word_count = {}
    for song in songs_urls[:5]:
        print(song)
        url = main_url + song
        
        response = requests.get(url)
        tree = html.fromstring(response.text)
        lyrics = tree.xpath('//div[@class="cnt-letra p402_premium"]//text()')
        
        for verse in lyrics:
            words = verse.split(' ')

            for word in words:
                word = word.lower()
                word = re.sub(r'\W+', '', word)

                if word == '':
                    continue

                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    word_count = {key: value for key, value in sorted(word_count.items(), key=lambda item:item[1], reverse=True)}

    for index, (key, value) in enumerate(word_count.items()):
        if index > 20: break
        print(f'{key}:\t{value}')