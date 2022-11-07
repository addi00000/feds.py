import re

import requests
from bs4 import BeautifulSoup

import feds.exceptions as exceptions


class fetch:
    def __init__(self, url: str):
        self.url = url
        self.res = requests.get(url)
        self.soup = BeautifulSoup(self.res.text, 'html.parser')

        if not self.check_valid():
            raise exceptions.InvalidLinkException(url)

    def check_valid(self):
        if not re.match(r'^https:\/\/feds\.lol\/[a-zA-Z0-9]+$', self.url):
            return False

        if 'doesnt_exist' in self.res.text:
            return False

        return True

    def get_data(self):
        return {
            'style': self.get_style(),
            'url': self.url,
            'avatar': self.get_avatar(),
            'background': self.get_background(),
            'name': self.get_name(),
            'views': self.get_views(),
            'bio': self.get_bio(),
            'spotify': self.get_spotify(),
            'links': self.get_links()
        }

    def get_style(self):
        if self.soup.find('link', href=re.compile('https://feds.lol/module/biolink_css/app.css')) is not None:
            return 1
        elif self.soup.find('link', href=re.compile('https://feds.lol/module/style2_css/app.css')) is not None:
            return 2

    def get_avatar(self):
        if self.get_style() == 1:
            return self.soup.find('div', class_='picture').find('div', class_='image')['style'].split('url(')[1].split(')')[0].replace("'", '')
        elif self.get_style() == 2:
            return self.soup.find('div', {'class': 'profile-info-top-wrapper'}).find('div', {'class': 'image'})['style'].split('url(')[1].split(')')[0].replace("'", '')

    def get_background(self):
        if self.get_style() == 1:
            return self.soup.find('div', class_='profile-bkg-hero-wrapper')['style'].split('url(')[1].split(')')[0].replace("'", '')
        elif self.get_style() == 2:
            return self.soup.find('body')['style'].split('url(')[1].split(')')[0].replace("'", '')

    def get_name(self):
        if self.get_style() == 1:
            return self.soup.find('div', class_='profile-name-wrapper').find('h2').text
        elif self.get_style() == 2:
            return self.soup.find('div', {'class': 'profile-name-wrapper'}).find('h2').text

    def get_views(self):
        return self.soup.find('div', id='viewCount').text.strip()

    def get_bio(self):
        if self.get_style() == 1:
            return self.soup.find('p', class_='profile-bio profile-bio-dark').text
        elif self.get_style() == 2:
            return self.soup.find('p', {'class': 'profile-bio'}).text

    def get_spotify(self):
        if self.get_style() == 1:
            return self.soup.find('div', {'style': 'text-align: center;'}).find('iframe')['src'].split('uri=')[1].split('&theme')[0] if self.soup.find('div', {'style': 'text-align: center;'}) else None
        elif self.get_style() == 2:
            return self.soup.find('iframe')['src'].split('uri=')[1].split('&theme')[0] if self.soup.find('iframe') else None

    def get_links(self):
        links = []
        if self.get_style() == 1:
            for link in self.soup.find_all('a', {'class': 'link-button link-button-void w-inline-block'}):
                links.append({
                    'name': link.find('div', {'class': 'link-name'}).text,
                    'url': link['href']
                })
        elif self.get_style() == 2:
            for link in self.soup.find_all('a', {'class': 'link-button link-button-void w-inline-block'}):
                links.append({
                    'name': link.find('div', {'class': 'link-name'}).text,
                    'url': link['href']
                })
        return links
