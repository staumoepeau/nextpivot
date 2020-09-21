# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

#with open('requirements.txt') as f:
#	install_requires = f.read().strip().split('\n')

_version_re = re.compile(r'__version__\s+=\s+(.*)')

#with open('nextpivot/__init__.py', 'rb') as f:
#    version = str(ast.literal_eval(_version_re.search(
#        f.read().decode('utf-8')).group(1)))
	
# get version from __version__ variable in nextpivot/__init__.py

setup(
	name='nextpivot',
	version=version,
	description='creating custom pivot view',
	author='Dexciss',
	author_email='dexciss@support.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
#	install_requires=install_requires
)
