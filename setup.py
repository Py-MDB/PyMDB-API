from setuptools import setup, find_packages

setup(
    name="pymdbapi",
    version="1.0.0",
    description="Python API built in flask for PyMDB",
    url="https://github.com/Py-MDB/PyMDB-API",
    packages=find_packages(),
    package_data={"": ["ts_configs/*"]},
    install_requires=[
        "flask",
        "pymongo",
        "flask-cors",
        "cerberus",
        "requests",
        "scapy",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pymdbapi=pymdbapi.__main__:main",
        ],
    },
)
