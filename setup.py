import codecs
import os
import re

from setuptools import find_packages, setup


def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


README = read(os.path.join(os.path.dirname(__file__), 'README.md'))

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='archivematica-fpr-admin',
    version=find_version('fpr', '__init__.py'),
    packages=find_packages(exclude=['testproject']),
    include_package_data=True,
    license='AGPL',
    author='Artefactual',
    author_email='info@artefactual.com',
    description='Format Policy Registry - Django app',
    long_description=README,
    url='https://github.com/artefactual/archivematica-fpr-admin',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'django-annoying==0.7.7',
        'django-autoslug==1.9.3',
        'django-extensions==1.1.1',
        'django-forms-bootstrap>=3.0.0,<4.0.0',
    ]
)
