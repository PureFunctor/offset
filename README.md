# stepped-augustus
A variation of the Augustus Cipher that offsets space-separated words based on the position of each character. This package is still in development.

# Usage
Invoke with the following commands:
```bash
# To encode
> python augustus.py --message "Hello, World" --direction r --steps 1
> Igopt, Xqupi

# To decode
> python augustus.py --message "Igopt, Xqupi" --direction l --steps 1
> Hello, World
```
