from setuptools import setup

setup(
    name="WorkoutBuddies",
    version="0.1.0",
    packages=["WorkoutBuddies"],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    python_requires='>=3.6',
)
