import smtplib
from email.message import EmailMessage

smtpServer = "sandbox.smtp.mailtrap.io"
smtpPort = 2525

smtpUser = "3d64a64ea6edde"
smtpPassword = "5124a9eeb31503"

msg = EmailMessage()

msg["From"] = "Neymar <neymardasilva@gmail.com>"
msg["To"] = "teteu <teteu@gmail.com>"
msg["Subject"] = "Projeto de Redes de Computadores 2"

msg.set_content(
    """Olá, é o Neymar!
 
 Estou esperando outro filho, será que você pode me ajudar fazendo um pix pra eu comprar 
 pampers e mamadeira?

"""
)

with smtplib.SMTP(smtpServer, smtpPort) as servidor:
    servidor.starttls()
    servidor.login(smtpUser, smtpPassword)
    servidor.send_message(msg)

print("E-mail enviado com sucesso!")