import os
import sys
from pathlib import Path

import setuptools
from setuptools.command.install import install


def run(self):
    os.system('rm -vrf ./build ./dist ./*.pyc ./*.pyo ./*.pyd ./*.tgz ./   *.egg-info `find -type d -name __pycache__`')


with open('README.md') as readme:
    readme_file = readme.read()

with open('requirements.txt') as requirement:
    INSTALL_REQUIRES = requirement.readlines()
    INSTALL_REQUIRES = [sd.replace('\n', '') for sd in INSTALL_REQUIRES]


setuptools.setup(
    name="User Analytics In The Telecommunication",
    version="0.0.1",
    description="some description do it later",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    url="https://github.com/Azizadx/user_analytics_in_the_telecommunication/",
    project_urls={
        "Source Code": "https://github.com/Azizadx/user_analytics_in_the_telecommunication/",
        "Bug Tracker": "",
        "Release notes": "",
        "Documentation": "",
    },
    author="Nasrallah Hassan AKA(azizadx)",
    author_email="azizadx.tech@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 0 - Pre/release",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    include_package_data=True,
)
