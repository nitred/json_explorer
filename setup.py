"""Setup file for the package/project."""
from setuptools import find_packages, setup

setup(
    name='json_explorer',
    version='0.0.1',
    description='A small module to explore a large json object or string or file.',
    long_description='A small module to explore a large json object or string or file and print out its structure to the console.',
    author='Nitish Reddy Koripalli',
    author_email='nitish.k.reddy@gmail.com',
    url='https://github.com/nitred/json_explorer',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True
)
