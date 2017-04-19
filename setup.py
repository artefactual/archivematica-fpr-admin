import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='archivematica-fpr-admin',
    version='1.6.0',
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
        'django-autoslug==1.7.1',
        'django-extensions==1.1.1',
        'django-forms-bootstrap>=3.0.0,<4.0.0',
    ]
)
