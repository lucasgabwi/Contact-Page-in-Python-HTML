from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configurações do e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = "contatolucasgab.wi@gmail.com"
PASSWORD = "dsof bouy juse rcet"

@app.route("/")
def index():
 return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
 nome = request.form["nome"]
 email = request.form["email"]
 mensagem = request.form["mensagem"]
 
 # Enviar e-mail de confirmação para o usuário
 msg = MIMEText("Recebemos sua mensagem! Em breve, entraremos em contato.")
 msg["Subject"] = "Confirmação de Contato"
 msg["From"] = FROM_EMAIL
 msg["To"] = email
 
 server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 server.starttls()
 server.login(FROM_EMAIL, PASSWORD)
 server.sendmail(FROM_EMAIL, email, msg.as_string())
 server.quit()
 
 # Enviar e-mail com a mensagem para o administrador
 msg = MIMEText(f"Mensagem de {nome} ({email}):\n\n{mensagem}")
 msg["Subject"] = "Mensagem de Contato"
 msg["From"] = FROM_EMAIL
 msg["To"] = FROM_EMAIL
 
 server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 server.starttls()
 server.login(FROM_EMAIL, PASSWORD)
 server.sendmail(FROM_EMAIL, FROM_EMAIL, msg.as_string())
 server.quit()
 
 return "Mensagem enviada com sucesso!"

if __name__ == "__main__":
 app.run(debug=True)