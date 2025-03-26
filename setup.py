from setuptools import setup, find_packages
from pathlib import Path

def readme():
    """Функція для читання вмісту файлу README.md"""
    return Path('README.md').read_text()

setup(
    name='py_olx_test',
    version='0.0.2',
    author='its_bohdan',
    author_email='harysh.bogdan@gmail.com',
    description='Python client for interacting with the OLX API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Bogdangarantov/py-olx',
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.3',
        'setuptools>=68.2.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='olx api olxapi',
    project_urls={
        'GitHub': 'https://github.com/Bogdangarantov/py-olx',
    },
    python_requires='>=3.11',
)
