from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in datawiseafrica/__init__.py
from datawiseafrica import __version__ as version

setup(
	name="datawiseafrica",
	version=version,
	description="dDcustom home page",
	author="peete",
	author_email="datawisepro@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
