import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Configuration de l'email
EMAIL_ADDRESS = "rdout2022@gmail.com"
EMAIL_PASSWORD = "zbor blxq dzxb ivor"
DESTINATION_EMAIL = "berolbertindjomo@gmail.com"
SUBJECT = "ENcryptage avec aes"
BODY = " hello t'as le message et la cle"

# Chemin du fichier à envoyer
files_to_send = ["key.bin", "message.enc"]

def send_email():
    # Créer l'objet email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = DESTINATION_EMAIL
    msg['Subject'] = SUBJECT

    # Ajouter le corps du message
    msg.attach(MIMEText(BODY, 'plain'))

    # Attacher le fichier
    for file_path in files_to_send:
        if os.path.exists(file_path):
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(file_path)}'
                )
                msg.attach(part)
        else:
            print(f"Le fichier {file_path} n'existe pas.")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
    # Connexion au serveur SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

