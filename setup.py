from setuptools import setup, find_packages

setup(
    name="pypedrive",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0",
        "pydantic>=1.8.0,<2.0.0",
        "python-dotenv>=0.19.0"
    ],
    author="Michael Stansky",
    description="A Python client for the Pipedrive API v2",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/michaelstansky/pypedrive",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
) 