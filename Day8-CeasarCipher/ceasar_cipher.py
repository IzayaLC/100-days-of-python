#The user will if they want to encrypt or decrypt
#-create a encrypt and decrypt function

def encryption(plaintext, key):
    encrypted_characters = []
    for character in plaintext:
        
        character_index = alphabet.index(character)
        encrypted_index = (character_index + key) % 26
        
        cipher_character = alphabet[encrypted_index]
        encrypted_characters.append(cipher_character)
        
    ciphertext = "".join(encrypted_characters)
    return ciphertext

def decryption(ciphertext, key):
    decrypted_characters = []
    for character in ciphertext:
        
        encrypted_index = alphabet.index(character)
        decrypted_index = (encrypted_index - key) % 26
        
        plaintext_char = alphabet[decrypted_index] 
        decrypted_characters.append(plaintext_char)
        
    plaintext = "".join(decrypted_characters)
    return plaintext

#THe user will enter the word they wish to encrypt or decrypt

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m",
            "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Welcome to the Ceasar Cipher!")
decision = input("Type 'e' to encrypt, type 'd' to decrypt: ")

if decision == "e":
    print(encryption("day", 3))