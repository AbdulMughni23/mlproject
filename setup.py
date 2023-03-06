from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets = [req.replace("\n", "") for req in requiremnets]

        if HYPEN_E_DOT in requiremnets:
            requiremnets.remove(HYPEN_E_DOT)
    
    return requiremnets 


setup(
name = "mlproject",
version='0.0.1',
author='Mohammad_Abdul_Mughni',
author_email='mughniabdul23@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)