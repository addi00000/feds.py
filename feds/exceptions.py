class LinkTakenException(Exception):
    def __init__(self, link):
        self.link = link

    def __str__(self):
        return f'The link {self.link} is already taken.'

class InvalidLinkException(Exception):
    def __init__(self, link):
        self.link = link

    def __str__(self):
        return f'The link {self.link} is invalid.'

class InvalidCredentialsException(Exception):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'The credentials {self.username}:{self.password} are invalid.'

class InvalidSessionException(Exception):
    def __init__(self, phpsessid):
        self.phpsessid = phpsessid

    def __str__(self):
        return f'The session {self.phpsessid} is invalid.'

class InvalidLinkException(Exception):
    def __init__(self, link):
        self.link = link

    def __str__(self):
        return f'The link {self.link} is invalid.'