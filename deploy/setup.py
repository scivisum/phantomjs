from setuptools import setup, find_packages


with open("VERSION") as version_file:
    VERSION = version_file.read().strip()


setup(
    name="svPhantomJS",
    packages=find_packages(),
    version=VERSION,
    include_package_data=True,
    author="Scivisum",
    author_email="phantomjs@scivisum.co.uk",
    description="Python package containing custom PhantomJS",
    url="https://github.com/scivisum/phantomjs"
)
