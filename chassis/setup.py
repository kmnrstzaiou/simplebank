from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chassis',
    version='0.0.1',
    description='A microservice chassis for Python projects',
    long_description=long_description,
    url='https://github.com/pap/simplebank',

    author='Simplebank Engineering',
    author_email='engineering@simplebank.book',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='microservices chassis development',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['peppercorn'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
