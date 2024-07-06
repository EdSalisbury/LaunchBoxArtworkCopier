from setuptools import setup, find_packages

setup(
    name="launchbox-artwork-copier",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'launchbox-artwork-copier=copy_launchbox_artwork:main',
        ],
    },
    author="Ed Salisbury",
    author_email="ed.salisbury@gmail.com",
    description="A script to copy artwork from LaunchBox to a structured directory",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/edsalisbury/launchbox-artwork-copier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
