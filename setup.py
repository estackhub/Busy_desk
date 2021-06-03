from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in busy_desk/__init__.py
from busy_desk import __version__ as version

setup(
	name='busy_desk',
	version=version,
	description='Custom integration to enhenance easy flow',
	author='Jide Olayinka',
	author_email='spryng.managed@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
