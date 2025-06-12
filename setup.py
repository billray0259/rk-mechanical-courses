from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='rk-mechanical-courses',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt')
)