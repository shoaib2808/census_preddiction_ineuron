from setuptools import setup,find_packages

EHYPEN = '-e .'

def get_module()->list:
    package_list=list()
    with open("requirements.txt",'r') as file:
         package_list=list()
         text=file.readlines()
         for line in text:
               if(line == EHYPEN):
                   break
               package_list.append(line)

         return package_list


setup(
     name="census_prediction",
     version='0.0.1',
     author='md shoaib khan',
     packages=find_packages(),
     install_requires=get_module()


)