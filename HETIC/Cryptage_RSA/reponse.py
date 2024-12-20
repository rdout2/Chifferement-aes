from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
# Générer une clé AES de 256 bits
key = get_random_bytes(32)
key = "key.bin"


# Déchiffrement du message
def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]),
AES.block_size).decode()
    return plaintext

# Lecture de la clé et du message chiffré à partir des fichiers
with open("key.bin", "rb") as fichier:
    key_read = fichier.read()

with open("message.enc", "rb") as fichier:
    ciphertext_read = fichier.read()

# Déchiffrement du message
decrypted_message = decrypt_message(ciphertext_read, key_read)

print("Message déchiffré:", decrypted_message)