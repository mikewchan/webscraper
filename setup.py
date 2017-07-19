try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Webscraper that scrapes data from web pages',
    'author': 'Mike Chan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mike@mikewchan.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['webscraper_app'],
    'scripts':['bin/myscript.py'],
    'name': 'Web Scraper App'
}

setup(**config)
