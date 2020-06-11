# offset
Caesar Cipher variation that offsets space-separated words based on the position of each character.

# Usage
Invoke with the following commands:
```bash
# To encode
> python offset.py --message "Hello, World" --direction r --steps 1
> Igopt, Xqupi

# To decode
> python offset.py --message "Igopt, Xqupi" --direction l --steps 1
> Hello, World
```
