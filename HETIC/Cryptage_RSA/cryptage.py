from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from SendMail import *
# Génération des clés RSA
key = RSA.generate(2048) #2048 bits
private_key = key.export_key()
public_key =b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtQBh4FnKi+CLBOrIQ0Eq\nbAOgIB9F2AgSbJ7gfjZnqU1sSaY7eoc5dZcbMBxpPmSnHT9DsPo7HTc5RorV9J5/\nJ/l9CaYbde2B2S9O7KaApAfh4XqMQlM7fRKRJHF3pVBMlTKtmxBDsZyDJ28Y6/XG\nH1Yz2uLl631+yIqAnZIAYnxTjNQbVJ7ouqr2jTDLgtAjU1BHhKWIeIgidbms2TiO\nx+JLXdvio0ARo+XsT55EtmUMou72DZJ8wBOMJ9Ie2zcGB9rHMJqJo3CoQsV33cFE\nbfCguSAK2nMl3ylPNqAYIh5w/jAfHUElezcwb3grE+R0JrhV30yruJblaosTxQQI\nrQIDAQAB\n-----END PUBLIC KEY-----'
# Chiffrement avec la clé publique

def encrypt_message(message, public_key):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode())
    return ciphertext
# Déchiffrement avec la clé privée
def decrypt_message(ciphertext, private_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    message = cipher.decrypt(ciphertext).decode()
    return message



# Exemple d'utilisation
message = "hello ça va Bertol??"
ciphertext = encrypt_message(message, public_key)
print("Message chiffré:", ciphertext)
# print("ma clé privé:" ,private_key)



send_email()