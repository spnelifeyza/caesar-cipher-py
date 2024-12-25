def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the final message
        if not char.isalpha():
            final_message += char
        else:
            # Find the correct key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# Ask user to enter the text and key
text = input("Enter the text: ")
custom_key = input("Enter the key: ")

# Ask user to choose encryption or decryption
action = input("Do you want to encrypt or decrypt? (e/d): ").lower()

if action == 'e':
    encrypted_text = encrypt(text, custom_key)
    print(f'\nEncrypted text: {encrypted_text}')
elif action == 'd':
    decrypted_text = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decrypted_text}')
else:
    print("\nInvalid option. Please choose 'e' for encryption or 'd' for decryption.\n")
