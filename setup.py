from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="PACKAGE_NAME",
    version="0.1.0",
    description="Python package for ()",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Author Name",
    author_email="Author Email",
    url="https://github.com/(owner)/(repo)",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=required,
)
