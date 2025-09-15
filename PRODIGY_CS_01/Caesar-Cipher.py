def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # only letters
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # keep spaces/numbers/symbols same
    return result


# --- User Input Section ---
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

if choice == "encrypt":
    encrypted = caesar_cipher(message, shift, "encrypt")
    print("\nEncrypted Message:", encrypted)
elif choice == "decrypt":
    decrypted = caesar_cipher(message, shift, "decrypt")
    print("\nDecrypted Message:", decrypted)
else:
    print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
