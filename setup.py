from setuptools import find_packages, setup

setup(
    name="EcommerceChatBot",
    version="0.0.0",
    author="Omkar Singh",
    author_email="singhomkar20.1995@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)