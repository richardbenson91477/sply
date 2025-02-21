# -*- coding: utf-8 -*-
from setuptools import setup

packages = ['sply', 'sply/overmind']

package_data = {'': ['*']}

setup_kwargs = {
    'name': 'sply',
    'version': '1.0.0',
    'description': 'a bridge between real and simulated python interpreters',
    'long_description': '',
    'author': 'Richard Benson',
    'author_email': 'richardbenson91477@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/richardbenson91477/sply',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}

setup(**setup_kwargs)

