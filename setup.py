from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of install requires
    """
    requirements=[]
    
    with open('requirements.txt') as f:
        requirements = f.readlines()
        [req.replace("\n", " ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
    
setup(
    name="classical_ml_project",
    version='0.0.1',
    author='johnisaacenriquez',
    author_email='johnisaacenriquez@cp.prec.eng.osaka-u.ac.jp',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)