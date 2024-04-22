#this is for testing a new idea.
def caesar_cipher(text, shift=1):
  """
  Encrypts a text using a Caesar cipher with a given shift.

  Args:
      text: The text to encrypt.
      shift: The number of positions to shift the letters (default: 1).

  Returns:
      The encrypted text.
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

# Get user input for text
text = input("Enter the text to encrypt: ")

# Get user input for shift value (handle potential errors)
while True:
  try:
    shift = int(input("Enter the shift value (1-25): "))
    if 1 <= shift <= 25:
      break
    else:
      print("Shift value must be between 1 and 25.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)

# Print the encrypted text
print("Encrypted text:", encrypted_text)

