from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os



load_dotenv()

def send_email(subject, body, to_email, attachment_path):
    remitente = os.getenv('EMAIL_USER')
    codigo = os.getenv('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = remitente
    msg['To'] = to_email
    msg.set_content(body)

    # Adjuntar el archivo
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(remitente, codigo)
        smtp.send_message(msg)