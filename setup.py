#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()


setup(
    name='django-light',
    description='Disable dark mode in Django admin UI.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0-3',
    url='https://github.com/frnhr/django-light',
    author='Fran Hrzenjak',
    author_email='fran@changeset.hr',
    scripts=[],
    packages=['django_light'],
    include_package_data=True,
    license='MIT',
    keywords='',
    install_requires=[],
    extras_require={},
)
