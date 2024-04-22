def caesar_cipher(text, shift):
  """
  Decrypts a text using a Caesar cipher with a given shift.

  Args:
      text: The text to decrypt.
      shift: The number of positions to shift the letters (positive value).

  Returns:
      The decrypted text.
  """
  # Ensure positive shift for decryption
  if shift < 0:
    raise ValueError("Shift value must be positive for decryption.")

  cipher_text = ""
  for char in text:
    # Check if it's a lowercase letter
    if char.islower():
      new_index = (ord(char) - ord('a') - shift) % 26  # Adjust for decryption by subtracting shift
      new_char = chr(new_index + ord('a'))
      cipher_text += new_char
    # Check if it's an uppercase letter
    elif char.isupper():
      new_index = (ord(char) - ord('A') - shift) % 26  # Adjust for decryption by subtracting shift
      new_char = chr(new_index + ord('A'))
      cipher_text += new_char
    # Keep other characters unchanged
    else:
      cipher_text += char
  return cipher_text

# Get user input for text
text = input("Enter the text to decrypt: ")

# Get user input for shift value (handle potential errors)
while True:
  try:
    shift = int(input("Enter the shift value (1-25): "))
    if shift > 0:  # Only accept positive shifts
      break
    else:
      print("Shift value must be positive for decryption.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Decrypt the text
decrypted_text = caesar_cipher(text, shift)

# Print the decrypted text
print("Decrypted text:", decrypted_text)
