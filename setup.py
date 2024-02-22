from setuptools import setup, find_packages

setup(
    name='esperanto',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'esperanto = esperanto.__main__:main'
        ]
    },
    install_requires=[
        'lark-parser',
        'deep_translator',
        'gtts'
    ],
)