import requests
from io import BytesIO
from pathlib import path

class LocalImage:
    """get a picture from filepath"""
    def __init__(self, path):
        self._path = path
    def get_image(self):
        return open(self._path, 'rb')

class RemoteImage:
    """get a picture from URL"""
    def __init__(self, path):
        self._url = path
    def get_image(self):
        data = requests.get(self._url)
        # change file object from byte data
        return BytesIO(data.content)

class _LoremFlickr(RemoteImage):
    """get a picture from searching by keyword"""
    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600
    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))
    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')

KeywordImage = _LoremFlickr

# This is constractor.
# The word is started by a captal letter 
def ImageSource(keyword):
    """Return a suitable image class"""
    if keyword.startswitch(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)

def get_image(keyword):
    """Return a object file of a picture."""
    return ImageSource(keyword).get_image()
