def caesar_encrypt(text, shift):
    """
    Encrypts the text using Caesar Cipher with the given shift value.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    """
    Decrypts the text using Caesar Cipher with the given shift value.
    """
    return caesar_encrypt(text, -shift)

def main():
    """
    Main function to run the Caesar Cipher encryption and decryption.
    """
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    text = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'e':
        encrypted_text = caesar_encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
