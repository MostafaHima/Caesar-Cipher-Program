import string
import pyfiglet

# Display ASCII art for program title
ascii_art = pyfiglet.figlet_format("Caesar Cipher")
print(ascii_art)

def caesar_cipher_program():
    """
    Main function to run Caesar Cipher encoding and decoding.
    """
    # Prompt user to input text for encryption/decryption
    text_to_process = input("\nEnter the text to process: ")

    # Handle invalid shift input with a try-except block
    try:
        shift_amount = int(input("Enter shift value (integer only): "))
    except ValueError:
        print("\nError: You must enter a valid integer for the shift value.")
        return

    # Function to encrypt text using Caesar Cipher
    def encrypt_text(text, shift):
        """
        Encrypts the given text by shifting letters to the right.
        """
        alphabet = string.ascii_lowercase
        encrypted_result = ""
        for char in text:
            if char in alphabet:  # Only process lowercase letters
                new_index = (alphabet.index(char) + shift) % len(alphabet)
                encrypted_result += alphabet[new_index]
            else:
                encrypted_result += char  # Keep other characters unchanged
        return encrypted_result

    # Function to decrypt text using Caesar Cipher
    def decrypt_text(text, shift):
        """
        Decrypts the given text by shifting letters to the left.
        """
        alphabet = string.ascii_lowercase
        decrypted_result = ""
        for char in text:
            if char in alphabet:  # Only process lowercase letters
                new_index = (alphabet.index(char) - shift) % len(alphabet)
                decrypted_result += alphabet[new_index]
            else:
                decrypted_result += char  # Keep other characters unchanged
        return decrypted_result

    # Ask the user for the operation: Encode, Decode, or Exit

    user_choice = input("\nWould you like to Encode, Decode, or Exit? (Type encode/decode/exit): ").lower()
    if user_choice == "encode":
        encrypted_text = encrypt_text(text_to_process, shift_amount)
        print(f"\nEncrypted Text: {encrypted_text}")
    elif user_choice == "decode":
        decrypted_text = decrypt_text(text_to_process, shift_amount)
        print(f"\nDecrypted Text: {decrypted_text}")
    elif user_choice == "exit":
        print("\nThank you for using the Caesar Cipher program. Goodbye!")
    else:
        print("\nInvalid choice! Please type 'encode', 'decode', or 'exit'.")

# Run the program in a loop for continuous use
while True:
    caesar_cipher_program()
    print("\n---------------------------------------\n")
