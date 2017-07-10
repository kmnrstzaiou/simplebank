#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='simplebank-orders',
    version='0.0.1',
    description='Store and serve orders',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'nameko==2.6.0',
        'nameko-sqlalchemy==0.0.4',
        'alembic==0.8.7',
        'marshmallow==2.9.1',
        'psycopg2==2.6.2',
    ],
    extras_require={
        'dev': [
            'pytest==3.1.1',
            'coverage==4.4.1',
            'flake8==3.3.0'
        ],
    },
    zip_safe=True
)
