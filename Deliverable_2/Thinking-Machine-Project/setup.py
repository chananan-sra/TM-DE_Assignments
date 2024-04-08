from setuptools import find_packages, setup

setup(
    name="Thinking_Machine_Project",
    packages=find_packages(exclude=["Thinking_Machine_Project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
