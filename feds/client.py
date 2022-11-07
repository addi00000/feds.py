import requests

import feds.exceptions as exceptions

class Client:
    def __init__(self, **kwargs):
        self.phpsessid = None
        self.username = None
        self.password = None

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        })
    
    def login_with_credentials(self, username: str, password: str):
        data = {
            'username': username,
            'password': password,
            'login': ''
        }
            
        res = self.session.post('https://feds.lol/login.php', data=data)
        self.phpsessid = requests.utils.dict_from_cookiejar(self.session.cookies)['PHPSESSID']

        if self.session.get('https://feds.lol/dash.php').status_code != 200:
            raise exceptions.InvalidCredentialsException(self.username, self.password)

        return

    def login_with_session(self, phpsessid: str):
        self.phpsessid = phpsessid
        self.session.cookies.set('PHPSESSID', self.phpsessid)

        if self.session.get('https://feds.lol/dash.php').status_code != 200:
            raise exceptions.InvalidSessionException(self.phpsessid)

        return

    def set_name(self, name: str) -> None:
        data = {
            'biolink_name': name,
            'biolinkname': ''
        }

        self.session.post('https://feds.lol/dash.php', data=data)
        
        return

    def set_link(self, link: str) -> None:
        if not link.isalnum():
            raise exceptions.InvalidLinkException(link)

        if 'doesnt_exist' not in self.session.get(f'https://feds.lol/{link}').text:
            raise exceptions.LinkTakenException(link)

        data = {
            'biolink_link': link,
            'biolinklink': ''
        }

        self.session.post('https://feds.lol/dash.php', data=data)

        return

    def set_avatar(self, avatar: str) -> None:
        data = {
            'biolink_profilepicture': avatar,
            'biolinkprofilepicture': ''
        }

        self.session.post('https://feds.lol/dash.php', data=data)
        
        return

    def set_background(self, background: str) -> None:
        data = {
            'biolink_background': background,
            'biolinkbackground': ''
        }

        self.session.post('https://feds.lol/dash.php', data=data)
        
        return

    def set_bio(self, bio: str) -> None:
        data = {
            'biolink_bio': bio,
            'biolinkbio': ''
        }

        self.session.post('https://feds.lol/dash.php', data=data)
        
        return