from setuptools import setup, find_packages

setup(
    name="audio_recorder",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=0.84.2",
    ],
)