import re
import requests
from lxml import html
from requests_html import HTMLSession
from unidecode import unidecode

url = 'https://www.last.fm/'
session = HTMLSession()
response = session.get(url)
response.html.render()

tree = html.fromstring(response.html.html)
artists_tags = tree.xpath('//div[@class="bubble_name"]')
artists = [artist.text for artist in artists_tags]

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