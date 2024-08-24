from setuptools import find_packages
from setuptools import setup

__version__ = "0.1"

setup(
    name="RPA_APP",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "python-dotenv"
    ]
)
