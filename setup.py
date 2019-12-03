# coding: utf-8

"""
    Brainrex General Sentiment API

    Runs the price sentiment service of api.brainrex.com/sentiment/  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "brainrex-client"
VERSION = "0.9.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Brainrex General Sentiment API",
    author_email="",
    url="",
    keywords=["Swagger", "Brainrex General Sentiment API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Runs the price sentiment service of api.brainrex.com/sentiment/  # noqa: E501
    """
)