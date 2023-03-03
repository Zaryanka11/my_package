import setuptools
import logging

with open('readme.md') as file:
    read_me_desc = file.read()

setuptools.setup(
    name='calculator1234',
    version="0.4",
    author='Zaryanka',
    author_email='email123@mail.ru',
    description='My description',
    long_description=read_me_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Zaryanka11/my_package',
    packages=['calculator1234'],
    install_requires=['logging'],
    python_requires='>=3.6',
)
