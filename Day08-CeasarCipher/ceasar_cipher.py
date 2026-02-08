
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m",
            "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encryption(plaintext, key=3):
    encrypted_characters = []
    for character in plaintext:
        if character.lower() not in alphabet:
            encrypted_characters.append(character)
            continue
         
        if character.isupper():
            character = character.lower()
            
            character_index = alphabet.index(character)
            encrypted_index = (character_index + key) % 26
        
            cipher_character = alphabet[encrypted_index].upper()
            encrypted_characters.append(cipher_character)
        else:
            character_index = alphabet.index(character)
            encrypted_index = (character_index + key) % 26
        
            cipher_character = alphabet[encrypted_index]
            encrypted_characters.append(cipher_character)
            
            
        
    ciphertext = "".join(encrypted_characters)
    return ciphertext

def decryption(ciphertext, key=3):
    decrypted_characters = []
    for character in ciphertext:
        if character.lower() not in alphabet:
            decrypted_characters.append(character)
            continue
        
        if character.isupper():
            character = character.lower()
            
            character_index = alphabet.index(character)
            decrypted_index = (character_index - key) % 26
        
            cipher_character = alphabet[decrypted_index].upper()
            decrypted_characters.append(cipher_character)
        else:
            character_index = alphabet.index(character)
            decrypted_index = (character_index - key) % 26
        
            cipher_character = alphabet[decrypted_index]
            decrypted_characters.append(cipher_character)
        
    plaintext = "".join(decrypted_characters)
    return plaintext

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print("Welcome to the Ceasar Cipher!")
decision = input("Type 'e' to encrypt, type 'd' to decrypt: ")

if decision == "e":
    text = input("Type your message: ")
    shift_number = int(input("Type the shift number: "))
    ciphertext = encryption(text, shift_number)
    
    print(f"Ciphertext generated:\"{ciphertext}\" ")
elif decision == "d":
    text = input ("Type your message: ")
    shift_number = int(input("Type the shift number: "))
    plaintext = decryption(text, shift_number)
    
    print(f"Plaintext generated:\"{plaintext}\"")
    
    
