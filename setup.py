from setuptools import setup, find_packages

setup(
    name="kcorrect",
    packages=find_packages(),
    include_package_data=True,  # Ensures non-Python files are included
    package_data={"": ["data/seds/*"]},  # Include all files in data/seds/
)

