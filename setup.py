from setuptools import find_packages, setup
from typing import List

HYPHENE_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHENE_DOT in requirements:
            requirements.remove(HYPHENE_DOT)
    
    return requirements

setup(
    name = 'mymlproject',
    version = '0.0.1',
    author = 'Nasif Safwan',
    author_email = 'nasifsafwan@gmail.com',
    packages = find_packages(),
    install_requiores = get_requirements('requirements.txt')
)
