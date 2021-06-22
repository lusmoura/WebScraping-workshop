import re
import requests
from lxml import html
from bs4 import BeautifulSoup

main_url = 'https://www.letras.mus.br'
artist = 'o grilo'
url = main_url + '/' + artist
response = requests.get(url)

# tree = html.fromstring(response.text)
# songs_tags = tree.xpath('//a[@class="song-name"]')

soup = BeautifulSoup(response.text, 'lxml')
songs_tags = soup.find_all('a', {'class': 'song-name'})

songs_urls = [song.get('href') for song in songs_tags]

# songs_urls = []
# for song in songs_tags:
#     songs_urls.append(song.get('href'))

word_count = {}
for song in songs_urls:
    print(song)
    url = main_url + song
    
    response = requests.get(url)
    # tree = html.fromstring(response.text)
    # lyrics = tree.xpath('//div[@class="cnt-letra p402_premium"]//text()')
    
    soup = BeautifulSoup(response.text)
    lyrics_div = soup.find('div', {'class': 'cnt-letra p402_premium'})
    lyrics_tags = lyrics_div.find_all('p')
    lyrics = [t.get_text(separator=' ') for t in lyrics_tags]

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
    if index > 50: break
    print(f'{key}:\t{value}')