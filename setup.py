from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="stepped-augustus",
    version="0.0.0",
    description=(
        "A variation of the Augustus Cipher."
    ),
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="PureFunctor",
    author_email="purefunctor@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security :: Cryptography",
    ],
    keywords="augustus cipher",
    license="MIT",
    py_modules=["augustus"],
    entry_points={
        "console_scripts": ["augustus=augustus:main"]
    },
)
