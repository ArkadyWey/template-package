from setuptools import setup

setup(name='template_package',
      version='1.0.0',
      description='A package to explore MWE functionality.',
      url='https://github.com/ArkadyWey/template-package/',
      author='Arkady Wey',
      packages=['tstools'],
      install_requires = 
      ["numpy", 
       "matplotlib"],
      license='GPLv3')