This is a Crypter written in Python 3. It is a demonstration of how a program can be obfuscated to bypass an antivirus. The obfuscated python code is loaded into memory where it is deobfuscated and run before touching the SSD.

## Required Modules
- Crypto
- random
- string

## Usage
- Create a file with the malicious code to be crypted
- Run ```python3 crypter.py```
- Type in the name of the malicious file you created
- Run ```python3 payload.py``` on the target machine (which must have the Crypto module)