import hashlib

# # Mot de passe
# password = "36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068"

# # Hachage du mot de passe

# hashed_password = hashlib.sha256(password.encode()).hexdigest()
# print("Mot de passe haché:", hashed_password)



# Mot de passe
password = input("Enter votre mots de passe: ")


# Hachage du mot de passe
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("Mot de passe haché:", hashed_password)

if password == hashed_password :
    print('Mots de passe exacte')
else : print('Mots de passe incorecte')