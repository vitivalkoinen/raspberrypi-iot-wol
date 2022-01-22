from setuptools import setup

setup(
    name = 'iotwol',
    install_requires=[
        'wakeonlan',
        'paho-mqtt'
    ],
    entry_points = {
        'console_scripts': [
            'iotwol = iotWol:main'
        ]
    }
)