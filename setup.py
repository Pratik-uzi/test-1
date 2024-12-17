from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .") # -e . is used to install the package in the current directory and is linked to the setup.py file
    return requirements

setup(
    name="test-1",
    version="0.0.1",
    author="Pratik",
    author_email="chakrabortyemon21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
