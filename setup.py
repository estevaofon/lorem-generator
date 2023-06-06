# setup.py

from setuptools import setup, find_packages

setup(
    name='lorem_ipsum',
    version='0.1.0',
    url='https://github.com/estevaofon/lorem-generator',
    author='Estevao',
    author_email='estevaopfon@gmail.com',
    description='Project to create Lorem Ipsum text',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lorem_ipsum = lorem_ipsum:main',
        ],
    },
)