
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

client = feds.Client(username = 'username13', password = 'password37')

client.login()
 
client.set_name('test') # Change biolink's display name
client.set_link('test') # Change biolink's URL
client.set_avatar('https://i.imgur.com/xxxxxxx.png') # Change biolink's profile picture
client.set_background('https://i.imgur.com/xxxxxxx.png') # Change biolink's background picture
client.set_bio('test') # Change biolink's bio
```


## Contributing

Feature additions and bug fixes/reports are welcome. Please open an issue or pull request.

## License

This project is licensed under the AGPL License - see the `LICENSE` file for details.

