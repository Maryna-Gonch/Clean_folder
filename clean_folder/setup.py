from setuptools import setup

setup(
    name='clean_folder',
    version='0.1.1',
    description='Code for cleaning folder',
    url='https://github.com/Maryna-Gonch/Homework_06',
    packages=['clean_folder'],
    entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:main']}
)