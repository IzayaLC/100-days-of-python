#The user will if they want to encrypt or decrypt
#-create a encrypt and decrypt function

def encryption(plaintext, key):
    for character in plaintext:
        character_index = alphabet.index(character)
        encrypted_index = character_index + key
        
        cipher_character = alphabet[encrypted_index]
        
        print(f"Plaintext character: {character} ")
        print(f"Ciphertext character: {cipher_character}")

#The user will enter the key (shift number)
#THe user will enter the word they wish to encrypt or decrypt

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m",
            "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Welcome to the Ceasar Cipher!")
decision = input("Type 'e' to encrypt, type 'd' to decrypt: ")

if decision == "e":
    encryption('a', 3)