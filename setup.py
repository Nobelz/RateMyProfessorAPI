import pathlib
import setuptools

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='RateMyProfessorAPI',
    version='1.3.1',
    description='Python web scraper to get professor ratings from ratemyprofessor.com website.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Nobelz/RateMyProfessorAPI',
    author='Nobel Zhou',
    author_email='nxz157@case.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    install_requires=requirements,
    project_urls={
        'Issue Tracker': 'https://github.com/Nobelz/RateMyProfessorAPI/issues',
    }
)
