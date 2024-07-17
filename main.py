# Importação - requests
import requests


# Pegar informação que você quer (Valor do Dólar)
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()

cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)


# Alerta de E-mail
import smtplib
import email.message

def enviar_email(cotacao):  
    corpo_email = f"""
    <p>A cotação do Dolar está a R$ {cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cotação do Dolar abaixo de R$ 5.50" # Preenchido
    msg['From'] = 'remetente' # Preencher
    msg['To'] = 'destinatario' # Preencher
    password = 'senha' # Preencher
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


if cotacao < 5.50:
    enviar_email(cotacao)


# Deploy
