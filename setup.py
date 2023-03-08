from typing import List
from setuptools import find_packages,setup

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    this sfunction will return the list of requirements

    Args:
        file_path (str): _description_

    Returns:
        List[str]: _description_
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name = 'e2e_mlproject',
    version = '0.0.1',
    author = 'Nithesh',
    author_email = 'nryreddy18@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt'),
)