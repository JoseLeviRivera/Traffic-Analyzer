import logging
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def send_email(recipient, subject, body, smtp_server, smtp_port, sender_email, sender_password):
    # Build the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Login to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient, message.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# Función actualizada para adjuntar archivos
def send_email_attach(recipient, subject, body, smtp_server, smtp_port, sender_email, sender_password, attachment_file=None):
    # Build the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    if attachment_file:
        # Adjuntar el archivo al mensaje
        attachment = open(attachment_file, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {attachment_file}")
        message.attach(part)

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Login to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient, message.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


def send_email_attach_file(username, password, recipient, attachment_file=None):
    # Build the email message
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = recipient
    message["Subject"] = "Report Traficc Analyzer Services"

    body = "This email contains every services is running to the server and network"

    message.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    if attachment_file:
        # Adjuntar el archivo al mensaje
        attachment = open(attachment_file, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {attachment_file}")
        message.attach(part)

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Login to the email account
            server.login(username, password)

            # Send the email
            server.sendmail(username, recipient, message.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# Ejemplo de llamada a la función con datos específicos
def main():
    recipient = "user@gmail.com"
    subject = "Report Traficc Analyzer Services"
    body = "This email contains every services is running to the server and network"

    # Configura los detalles del servidor SMTP y credenciales
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("EMAIL_USERNAME")
    sender_password = os.getenv("EMAIL_PASSWORD")

    # Llama a la función con los datos proporcionados
    send_email(recipient, subject, body, smtp_server, smtp_port, sender_email, sender_password)


# Configura el registro según tus necesidades
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    main()
