'''
Web scrapper for Ebay.
Program is PEP8 formated.
'''

import time
import sys
from bs4 import BeautifulSoup
import requests

def scrapper():
    '''
    Function to get the requests and find appropriate data for search.
    Links and HTML attribues can be changed to meet needs.
    '''

    try:
        #Allows users to enter the items they would like to scrape.
        url = input('Please enter the Ebay site you would like to scrape: ')
        #Exits program is link is blank
        if url == "":
            sys.exit(0)
        else:
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'lxml')
            items = soup.find_all('li', class_ = 's-item s-item__pl-on-bottom s-item--watch-at-corner')
            for index, item in enumerate(items):
                brand = item.find('div', class_ = 's-item__title').span.text
                condition = item.find('div', class_ = 's-item__subtitle').span.text
                price = item.find('div', class_ = 's-item__detail s-item__detail--primary').span.text
                more_info = item.find('a', class_ = 's-item__link')['href']
                #Creates a new file every 15 minutes with new info
                #These files get placed into the posts folder
                with open(f'posts/{index}.txt', 'w', encoding = 'utf-8') as f:
                    f.write(f'Brand: {brand.strip()} \n')
                    f.write(f'Condition: {condition.strip()} \n')
                    f.write(f'Price: {price.strip()} \n')
                    f.write(f'More Info: {more_info.strip()} \n')
                print(f'File saved: {index}')
    except ValueError:
        print('Enter a valid link for scrapping')

#Setting a 15 min execution timer
if __name__ == '__main__':
    while True:
        scrapper()
        TIME_WAIT = 15
        print(f'Waiting {TIME_WAIT} minutes...')
        print('Press CTRL-C to exit program')
        time.sleep(TIME_WAIT * 60)
        print()
