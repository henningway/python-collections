import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="threadable",
    version="0.0.1",
    author="Henning Schindler",
    author_email="mail@henningschindler.de",
    description="Fluency for compound data types.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henningway/python-collections",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
