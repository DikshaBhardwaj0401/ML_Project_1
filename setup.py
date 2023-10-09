from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    Returns a list of requirements from the given file path.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] #to avoid the newline comment from requirements 

    return requirements

setup(
    name = 'ML_Project',
    version = '0.0.1',
    author = 'Diksha Bhardwaj',
    author_email = 'dikshaintech@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)