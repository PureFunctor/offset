from setuptools import setup

setup(
    name="stepped-augustus",
    version="1.0",
    description=(
        "A variation of the Augustus Cipher that offsets space-separated words based on"
        "the position of each character in that word."
    ),
    author="PureFunctor",
    author_email="purefunctor@gmail.com",
    license="MIT",
    py_modules=["augustus"],
    entry_points={
        "console_scripts": ["augustus=augustus:main"]
    },
)
