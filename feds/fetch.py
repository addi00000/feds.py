import feds.exceptions as exceptions
from bs4 import BeautifulSoup
import requests
import re


class fetch:
    def __init__(self, url: str):
        self.url = url
        self.res = requests.get(url)
        self.soup = BeautifulSoup(self.res.text, "html.parser")

        if not self.check_valid():
            raise exceptions.InvalidLinkException(url)

    def check_valid(self):
        if not re.match(r"^https:\/\/feds\.lol\/[a-zA-Z0-9]+$", self.url):
            return False

        if "doesnt_exist" in self.res.text:
            return False

        return True

    def get_data(self):
        return {
            "url": self.url,
            "avatar": self.get_avatar(),
            "background": self.get_background(),
            "name": self.get_name(),
            "views": self.get_views(),
            "bio": self.get_bio(),
            "audio": self.get_audio(),
            "links": self.get_links(),
        }

    def get_avatar(self):
        return self.soup.find("img")["src"]

    def get_background(self):
        return self.res.text.split("<main style=")[1].split(",url('")[1].split("')")[0]

    def get_name(self):
        return self.soup.find("h2").text.strip()

    def get_views(self):
        return self.res.text.split('<i class="ri-eye-2-fill"></i>\n')[1].split(" </p>")[
            0
        ]

    def get_bio(self):
        if (
            """<span class="typewrite" data-period="2000" data-type='"""
            in self.res.text
        ):
            return self.res.text.split(
                '''<span class="typewrite" data-period="2000" data-type='[ "'''
            )[1].split('"]')[0]
        else:
            return self.soup.find("pre").text.strip()

    def get_audio(self):
        if "source src" in self.res.text:
            return self.soup.find("source")["src"]
        else:
            if self.soup.find("iframe") != None:
               return self.soup.find("iframe")["src"].split("?&theme=0")[0]
            return None

    def get_links(self):
        links = []
        for link in self.soup.find_all(
            "a",
            {
                "class": "bg-main rounded-xl flex-[100%] sm:flex-[45%] animate-slide-up shadow-4xl p-3 button"
            },
        ):
            links.append(
                {
                    "name": link.find("h2").text.strip(),
                    "url": link["href"],
                }
            )
        return links
