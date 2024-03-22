from setuptools import setup, find_packages

setup(
    name = 'improbs',      
    version = '0.0.2',  
    description = "A trivial numpy computation for 1D arrays",
    url='https://github.com/GMorandi98',
    license='MIT',
    author = 'Gabriele Morandi',
    author_email = 'g.morandi1@campus.unimib.it',
    packages = find_packages(), 
    install_requires = ['numpy']
)
