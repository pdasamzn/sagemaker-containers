import os
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='sagemaker_container_support',
    version='1.0',
    description='Open source library for creating containers to run on Amazon SageMaker.',

    packages=find_packages(where='src', exclude=('test',)),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    data_files=[('etc', ['etc/nginx.conf', 'etc/telegraf.conf', 'etc/print_gpu_info.py'])],
    long_description=read('README.rst'),
    author='Amazon Web Services',
    url='https://github.com/aws/sagemaker-container-support/',
    license='Apache License 2.0',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=['numpy>=1.13.3', 'requests>=2.18', 'boto3>=1.4.8', 'six>=1.11.0', 'gevent>=1.2.2',
                      'gunicorn>=19.7.1', 'flask>=0.11'],
    extras_require={
        'test': ['tox', 'flake8', 'pytest', 'pytest-cov', 'pytest-xdist', 'mock', 'Flask', 'boto3']
    }
)