try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Numerical Analysis and Software Programming Assignment 2',
    'author': 'Peter Adam, Kieron Ellis, Andy McSweeney',
    'url': 'https://github.com/Padam-0/nas_prog2',
    'download_url': 'https://github.com/Padam-0/nas_prog2',
    'author_email': 'peter.adam@ucdconnect.ie, kieron.ellis@ucdconnect.ie,'
                    'andy.mcsweeney@ucdconnect.ie',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bsm', 'sor'],
    'scripts': [],
    'name': 'Solve Black Scholes via Successive Over Relaxation'
}

setup(**config)
