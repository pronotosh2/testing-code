#for testing of alphabets value shifting in Python bracket is not allowed.
def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a text using a Caesar cipher with a given shift.

    Args:
        text: The text to encrypt or decrypt.
        shift: The number of positions to shift the letters.

    Returns:
        The encrypted or decrypted text.
    """
    cipher_text = ""
    for char in text:
        # Check if it's a lowercase letter
        if char.islower():
            new_index = (ord(char) - ord('a') + shift) % 26
            new_char = chr(new_index + ord('a'))
            cipher_text += new_char
        # Check if it's an uppercase letter
        elif char.isupper():
            new_index = (ord(char) - ord('A') + shift) % 26
            new_char = chr(new_index + ord('A'))
            cipher_text += new_char
        # Keep other characters unchanged
        else:
            cipher_text += char
    return cipher_text


# Get user input for text and shift value
def get_input_and_encrypt():
    text = input("Enter the text to encrypt or decrypt: ")
    while True:
        try:
            shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted/Decrypted text:", encrypted_text)


# Main function
def main():
    get_input_and_encrypt()


if __name__ == "__main__":
    main()

