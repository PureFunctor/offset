from setuptools import setup

setup(
    name="offset",
    version="1.0",
    description=(
        "Caesar Cipher variation that offsets space-separated words based on"
        "the position of each character."
    ),
    author="PureFunctor",
    author_email="purefunctor@gmail.com",
    license="MIT",
    py_modules=["offset"],
    entry_points={
        "console_scripts": ["offset=offset:main"]
    },
)
