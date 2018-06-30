import setuptools

if __name__ == "__main__":
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="w7py",
        version="0.0.1a",
        description="w7py",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/yuliu2016/w7py",
        packages=setuptools.find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ),
        install_requires=[
            "numpy",
            "pandas",
            "requests"
        ],
        entry_points={
            'console_scripts': ['w7=w7py.cli:cli_main']
        }
    )
