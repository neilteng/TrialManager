import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TrialManager", # Replace with your own username
    version="0.0.1",
    author="Neil Deng",
    author_email="neilteng@gmail.com",
    description="A simple trial manager for experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neilteng",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)