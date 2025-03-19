from setuptools import setup, find_packages

setup(
    name="3D-bin-packing",
    version="0.1.0",
    description="3D bin packing implementation",
    packages=find_packages(),
    install_requires=[
        "numpy==1.19.5",
        "matplotlib==3.3.4",
    ],
)
