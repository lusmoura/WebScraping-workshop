import re
from lxml import html
from bs4 import BeautifulSoup
from unidecode import unidecode
from requests_html import HTMLSession

def print_words(words, max_words=20):
    ''' Print first max_words according to the num of occurences '''
    count_words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}           
    
    for i, (k, v) in enumerate(count_words.items()):
        if i > max_words: break
        print(f'{k}:\t{v}')

def make_request(url):
    ''' Make request with the request_html module and treat errors '''

    headers = {
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    }

    session = HTMLSession()
    try:
        response = session.get(url, headers=headers)
        response.html.render()
    except Exception as e:
        print(f'Error - {e.args}')
        return None
    
    if response.status_code != 200:
        return None

    return response

def get_songs_tags_lxml(response):
    ''' Use lxml to parse artist page '''
    tree = html.fromstring(response.html.html)
    songs_tags = tree.xpath('//a[@class="song-name"]')
    return songs_tags

def get_songs_tags_bs4(response):
    ''' Use BeautifulSoup to parse artist page '''
    soup = BeautifulSoup(response.html.html, 'lxml')
    songs_tags = soup.find_all('a', {'class': 'song-name'}, href=True)
    return songs_tags

def get_lyrics_lxml(response):
    ''' Use lxml to parse song lyrics page '''
    tree = html.fromstring(response.html.html)
    lyrics = tree.xpath('//div[@class="cnt-letra p402_premium"]//text()')
    return lyrics

def get_lyrics_bs4(response):
    ''' Use BeautifulSoup to parse song lyrics page '''
    soup = BeautifulSoup(response.html.html, 'lxml')
    lyrics_div = soup.find('div', {'class': 'cnt-letra p402_premium'})
    lyrics_tags = lyrics_div.find_all('p')
    lyrics = [t.get_text(separator=' ') for t in lyrics_tags]
    return lyrics

if __name__ == '__main__':
    use_lxml = True                             # set which module to use
    max_songs = 10                              # set amount of songs to consider
    artist = 'Olivia Rodrigo'                   # set artist
    
    main_url = 'https://www.letras.mus.br'      
    clean_artist = artist.lower().replace(' ', '-')
    url = main_url + '/' + clean_artist

    # get artist page
    response = make_request(url)
    
    if response == None:
        print('Failed')
        exit(1)
    
    # parse artist page
    if use_lxml:
        songs_tags = get_songs_tags_lxml(response)
    else:
        songs_tags = get_songs_tags_lxml(response)

    songs_urls = [main_url + song.get('href') for song in songs_tags]
    
    count_words = {}
    num_songs = min(len(songs_urls), max_songs)
    
    # get each song
    for index, url in enumerate(songs_urls[:num_songs], 1):
        song_name = url.split('/')[-2]
        print(f'[{index}/{num_songs}] - {song_name}')

        response = make_request(url)
        if response is None:
            print(f'{url} failed')
            continue

        # parse lyrics page
        if use_lxml:
            lyrics = get_lyrics_lxml(response)
        else:
            lyrics = get_lyrics_bs4(response)
        
        # loop over verses and words counting them
        for verse in lyrics:
            words = verse.split(' ')

            for word in words:
                word = word.lower()
                word = unidecode(word)
                word = re.sub(r'\W+', '', word)

                if word == '':
                    continue

                if word in count_words:
                    count_words[word] += 1
                else:
                    count_words[word] = 1

    # show result
    print_words(count_words)