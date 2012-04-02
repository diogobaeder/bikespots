from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='bikespots',
      version=version,
      description="Código-fonte para o site bikespots.com.br",
      long_description="""\
Código-fonte para o site bikespots.com.br""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='bikespots bike bicicleta python tornado',
      author='Diogo Baeder',
      author_email='diogobaeder@yahoo.com.br',
      url='http://www.bikespots.com.br',
      license='BSD 2-clause',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
