from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wrm3_settings",
    version="0.1.0",
    author="WRM3",
    author_email="wrmartel3@gmail.com",
    description="A settings library for keeping your settings in a json file, that you can edit and hot load in looping scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wrm3/wrm3_settings",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[],
)