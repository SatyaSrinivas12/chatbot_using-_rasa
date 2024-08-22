from setuptools import setup

setup(
    name='chatbot',
    version='0.1.0',
    description='car showroom',
    author='satya srinivas',
    author_email='bokkasatyasrinivas@gmail.com',
    packages=['actions'],
    install_requires=[
        'rasa','mysql-connector-python','transformers'
    ],
    python_requires='>=3.10.0',  # Specify the Python version here
)
