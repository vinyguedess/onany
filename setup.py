import os
from setuptools import setup


with open(os.path.join("README.rst")) as file:
    readme = file.read()


with open(os.path.join("requirements.txt")) as file:
    requirements = file.read().split("\n")


setup(
    name="onany",
    packages=["onany"],
    version=os.getenv("GITHUB_REF") \
        .replace("refs/tags/v", ""),
    license="MIT",
    description="Event manager library",
    long_description=readme,
    author="Vinicius Guedes",
    author_email="viniciusgued@gmail.com",
    url="https://github.com/vinyguedess/onany",
    download_url="https://github.com/vinyguedess/onany/archive/master.zip",
    keywords=["event", "events", "listener", "dispatch"],
    
    install_requires=requirements,
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ])
