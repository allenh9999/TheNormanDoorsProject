from setuptools import setup

setup(
    name="NormanDoors",
    version="0.1.0",
    packages=["NormanDoors"],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    python_requires='>=3.6',
)
