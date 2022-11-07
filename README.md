
# feds.py

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

A [feds.lol](https://feds.lol/) API wrapper for Python.
## Installation

Install feds.py with pip

```bash
pip3 install feds.py
```
## Usage/Examples

```python
import feds

client = feds.Client()
client.login_with_credentials('username', 'password')

client.set_name('test') # Change biolink's display name
client.set_link('test') # Change biolink's URL
client.set_avatar('https://i.imgur.com/xxxxxxx.png') # Change biolink's profile picture
client.set_background('https://i.imgur.com/xxxxxxx.png') # Change biolink's background picture
client.set_bio('test') # Change biolink's bio
```

```python
import feds

client = feds.Client()
client.login_with_session('PHPSESSID')

client.set_name('test') # Change biolink's display name
client.set_link('test') # Change biolink's URL
client.set_avatar('https://i.imgur.com/xxxxxxx.png') # Change biolink's profile picture
client.set_background('https://i.imgur.com/xxxxxxx.png') # Change biolink's background picture
client.set_bio('test') # Change biolink's bio
```

```python
>>> import feds
>>> import json
>>>
>>> data = feds.fetch('https://feds.lol/1').get_data()
>>> 
>>> print(json.dumps(data, indent=4))
{
    "style": 1,
    "url": "https://feds.lol/1",
    "avatar": "https://i.imgur.com/hZpOceo.jpeg",
    "background": "https://i.imgur.com/zx6en3Q.gif",
    "name": "b",
    "views": "5869",
    "bio": "test",
    "spotify": "spotify:track:3AIxrqGApkV8E7uH0x2xF3?si=490a05333d6a4692",
    "links": [
        {
            "name": "GITHUB",
            "url": "https://github.com/addi00000"
        }
    ]
}
```

## Contributing

Feature additions and bug fixes/reports are welcome. Please open an issue or pull request.

## License

This project is licensed under the AGPL License - see the `LICENSE` file for details.

