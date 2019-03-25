import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='pysgs',
    version='0.1',
    author="Esteban Solorzano",
    author_email="estebansolorzano27@gmail.com",
    description="Send messages through SendGrid using SMTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/estebansolo/pysgs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ]
)