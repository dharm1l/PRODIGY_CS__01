def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            shift_value = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) + shift_value - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            shift_value = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) + shift_value - 97) % 26 + 97)
        
        # Leave non-alphabet characters as is
        else:
            result += char
    
    return result

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

# Encrypt or Decrypt based on mode
output = caesar_cipher(message, shift, mode)
print(f"The {mode}ed text is: {output}")
