import re
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    return driver

def make_request(url, driver):
    ''' Make request with the selenium module and treat errors '''
    driver.get(url)

def get_songs_tags(driver):
    ''' Use lxml to parse artist page '''
    songs_tags = driver.find_elements_by_xpath('//a[@class="song-name"]')
    return songs_tags

def get_lyrics(response):
    ''' Use lxml to parse song lyrics page '''
    lyrics_tags = driver.find_elements_by_xpath('//div[@class="cnt-letra p402_premium"]')
    lyrics = [t.text.replace('\n', ' ') for t in lyrics_tags]
    return lyrics

def print_words(words, max_words=20):
    ''' Print first max_words according to the num of occurences '''
    count_words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}           
    
    for i, (k, v) in enumerate(count_words.items()):
        if i > max_words: break
        print(f'{k}:\t\t{v}')

if __name__ == '__main__':
    use_lxml = True                             # set which module to use
    max_songs = 5                               # set amount of songs to consider
    artist = 'Oasis'                            # set artist

    main_url = 'https://www.letras.mus.br'      
    clean_artist = artist.lower().replace(' ', '-')
    url = main_url + '/' + clean_artist

    driver = get_driver()

    # get artist page
    make_request(url, driver)
    
    # parse artist page
    songs_tags = get_songs_tags(driver)
    songs_urls = [song.get_attribute('href') for song in songs_tags]
    
    count_words = {}
    num_songs = min(len(songs_urls), max_songs)
    
    # get each song
    for index, url in enumerate(songs_urls[:num_songs], 1):
        song_name = url.split('/')[-2]
        print(f'[{index}/{num_songs}] - {song_name}')
        
        make_request(url, driver)

        # parse lyrics page
        lyrics = get_lyrics(driver)
        
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

    # sort dict and show result
    print_words(count_words)