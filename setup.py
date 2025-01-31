from setuptools import setup, find_packages

setup(
    name="kcorrect",
    version="5.1.4",
    packages=find_packages(include=["kcorrect", "kcorrect.*"]),  # Ensure it finds sub-packages
    include_package_data=True,  # Important: This allows data files to be included
    package_data={"kcorrect": ["data/seds/*"]},  # Explicitly include data/seds/
)

