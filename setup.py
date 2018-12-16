"""
Hyperband
Author: zygmuntz
"""
from setuptools import setup

requirements = [
    'numpy',
    'hyperopt',
    'pprint',
    'sklearn',
]

setup(name='hyperband',
      version='0.0.0',
      description='Hyperband',
      author='zygmuntz',
      author_email='',
      package_dir = {'': '.'},
      packages=['hyperband'],
      install_requires = requirements
     )
