from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.strip() for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Gyansh",
    author_email="chaudhary_gyansh23@gmail.com",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},               
    install_requires=get_requirements("requirements.txt"),
)



