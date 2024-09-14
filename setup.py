from __future__ import annotations

import pathlib

from setuptools import find_packages
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='nox-cli',
    use_scm_version=True,
    setup_requires=['setuptools-scm'],
    description='A powerful CLI tool for various automation tasks.',
    author='Adib Grouz',
    author_email='contact@adib-grouz.com',
    url='https://github.com/Adi3g/nox-cli',
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=[
        'click',
        'PyJWT',
        'cryptography',
        'boto3',
        'SQLAlchemy',
        'rsa',
        'requests',
        'python-whois',
        'types-requests',
        'speedtest-cli',
        'docker',
        'python-dotenv',
        'pytz',
        'types-pytz',
        'confluent-kafka',
        'tqdm',
        'whois',
        'redis',

    ],
    entry_points='''
        [console_scripts]
        nox=nox.main:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    tests_require=['pytest', 'pytest-cov'],
)
