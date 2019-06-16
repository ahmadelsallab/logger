import os
from setuptools import setup
from setuptools import find_packages
# requirements is generated by pipreqs <project_path>
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
   name='mllogger',
   version='1.0',
   description='Machine learning experiments logger',
   author='Ahmad El Sallab',
   author_email='ahmad.elsallab@gmail.com',
   install_requires=required, #external packages as dependencies
   packages=find_packages()
)
