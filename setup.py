from setuptools import setup

setup(
    name = 'iotwol',
    installl_requires=[
        'wakeonlan',
        'paho-mqtt'
    ],
    entry_points = {
        'console_scripts': [
            'iotwol = iotWol:main'
        ]
    }
)