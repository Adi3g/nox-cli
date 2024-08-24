from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

setup(
    name='nox-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'PyJWT',
        'cryptography',
        'boto3',
        'SQLAlchemy',
    ],
    entry_points='''
        [console_scripts]
        nox=nox.main:cli
    ''',
)
