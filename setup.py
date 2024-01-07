from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace('\n', '') for req in requirements]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error occurred while reading '{file_path}': {e}")
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='kaustubh',
    author_email='kaustubh.dwi651@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)