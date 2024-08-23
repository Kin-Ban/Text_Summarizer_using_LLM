#if you want to publish this package 

import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.0.1'

REPO_NAME = 'Text-Summerization-using-LLM'
AUTHOR_USER_NAME = 'Kinjal Bandopadhyay'
SRC_REPO = 'TextSummarizer_llm'
AUTHOR_EMAIL = "kinjalspeak@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    description="A small package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)