from setuptools import setup, find_packages

setup(
    name="TheMonumenstDomodedovo",  # Replace with your project name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # Add your libraries here
        "os",
        "tkintermapview",
        "builtins",
        "tkinter",
        "monument",
        "webbrowser"

    ],
    entry_points={
        "console_scripts": [
            "my_project=main:main",  # Allows running with `my_project` command
        ],
    },
)