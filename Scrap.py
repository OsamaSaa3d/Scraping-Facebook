from bs4 import BeautifulSoup
import requests


def get_numbers(link):
    new_link = link + '/friends_likes'
    response = requests.get(new_link)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    about = soup.find('div', class_='x78zum5 x1q0g3np x1a02dak x1qughib')
    return about


link = 'https://www.facebook.com/Alkayanhomedecor'
about = get_numbers(link)
print(about)
