import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_sender(remetente, senha, destinatario, assunto, mensagem,):
    try:
        # Cria objeto MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto

        # Corpo do email
        msg.attach(MIMEText(mensagem, 'plain'))

        
        # if caminho_anexo and os.path.isfile(caminho_anexo):
        #     with open(caminho_anexo, "rb") as f:
        #         parte = MIMEBase('application', 'octet-stream')
        #         parte.set_payload(f.read())
            
        #     encoders.encode_base64(parte)
        #     parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(caminho_anexo)}')
        #     msg.attach(parte)

        # Conexão com Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Criptografia
            server.login(remetente, senha)  # senha = senha de app do Gmail
            server.sendmail(remetente, destinatario, msg.as_string())

        print("E-mail enviado com sucesso!")

    except Exception as e:
        print("Erro ao enviar e-mail:", e)