# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes

# # Générer une clé AES de 256 bits
# key = get_random_bytes(32)

# # Chiffrement du message
# def encrypt_message(message, key):
#     cipher = AES.new(key, AES.MODE_CBC)
#     ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
#     return cipher.iv + ciphertext

# # Déchiffrement du message
# def decrypt_message(ciphertext, key):
#     iv = ciphertext[:16]
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size).decode()
#     return plaintext

# # Exemple d'utilisation
# message = "Voici un message crypté avec AES!"
# ciphertext = encrypt_message(message, key)
# print("Message chiffré:", ciphertext)

# decrypted_message = decrypt_message(ciphertext, key)
# # print("Message déchiffré:", decrypted_message)
# # print("Voici la cle ", key)

# liste = [key , decrypted_message]

# fichier = open("key.bin", "rb+")
# fichier.write(key)
# fichier.close()
# fichier = open("message.enc", "rb")
# fichier.write(cipher.iv + ciphertext)
# fichier.close()

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from SendMail import *

# Générer une clé AES de 256 bits
key = get_random_bytes(32)

# Chiffrement du message
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Déchiffrement du message
def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size).decode()
    return plaintext

# Exemple d'utilisation
message = "Voici un message crypté avec AES!"
ciphertext = encrypt_message(message, key)
print("Message chiffré:", ciphertext)

decrypted_message = decrypt_message(ciphertext, key)
# print("Message déchiffré:", decrypted_message)
# print("Voici la cle ", key)

# Sauvegarde de la clé et du message chiffré dans des fichiers
# Sauvegarder la clé
with open("key.bin", "wb") as fichier:
    fichier.write(key)

# Sauvegarder le message chiffré
with open("message.enc", "wb") as fichier:
    fichier.write(ciphertext)

# Pour vérifier que le message peut être déchiffré correctement
# print("Message déchiffré:", decrypted_message)
send_email()