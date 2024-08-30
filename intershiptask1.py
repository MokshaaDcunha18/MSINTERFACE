def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Normalize the shift to be within 0-25
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetical characters are not changed
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with negative shift

def main():
    print("Caesar Cipher Encryption/Decryption")
    mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if mode == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif mode == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid option. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()