from setuptools import setup

setup(
    name='guessing_bio',
    version='0.1.0',
    author='Joseph Njeri',
    author_email='kitgaedesigaidi4@gmail.com',
    packages=['guessing_bio'],
    url='https://github.com/karianjahi/guessing_bio_package',
    license='LICENSE',
    description="A package that guess someone's bio",
    long_description=open('README.md').read(),

    install_requires=[
        "Faker",
    ],
)
