import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
