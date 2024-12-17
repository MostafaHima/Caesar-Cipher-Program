# Caesar Cipher Program

This program implements the **Caesar Cipher**, a simple encryption and decryption technique that shifts letters in the text by a given number of positions. The program allows users to encode or decode messages interactively.

## Features
- **Encryption**: Shift text letters to the right.
- **Decryption**: Shift text letters to the left.
- Handles only lowercase letters; other characters remain unchanged.
- Interactive user interface with options to encode, decode, or exit the program.
- Validates user input for shift values.

## Requirements
The program uses the following Python libraries:
- `pyfiglet`: To display ASCII art for the program title.
- `string`: To process the lowercase alphabet.

To install the `pyfiglet` library, run:
```bash
pip install pyfiglet
```

## How to Run the Program
1. Ensure Python is installed on your system.
2. Install required dependencies.
3. Run the script:
   ```bash
   python main.py
   ```

## Usage
- **Step 1**: Enter the text you want to encode or decode.
- **Step 2**: Enter the shift value (an integer).
- **Step 3**: Choose one of the following options:
   - `encode`: Encrypt the text.
   - `decode`: Decrypt the text.
   - `exit`: Exit the program.

### Example
**Input**:
```
Enter the text to process: hello
Enter shift value (integer only): 3
Would you like to Encode, Decode, or Exit? (Type encode/decode/exit): encode
```
**Output**:
```
Encrypted Text: khoor
```

**Decoding Example**:
```
Would you like to Encode, Decode, or Exit? (Type encode/decode/exit): decode
Decrypted Text: hello
```

## Notes
- Only lowercase letters are processed.
- Non-alphabetical characters remain unchanged.
- The program runs in a loop until you choose to exit.

## Program Flow
1. Displays ASCII art.
2. Prompts the user for input text and a shift value.
3. Encrypts or decrypts the text based on user choice.
4. Repeats the process until the user exits.

