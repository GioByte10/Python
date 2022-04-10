import smtplib, ssl
from random import shuffle

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "devtestcyb@gmail.com"  # Enter your address
password = "TestAndDevelop10#"

people = ["Giovanni", "Camila", "Rocio", "Daniela", "Misael", "Thiana", "Arantza", "Ximena", "Josue", "Cesar"]
emails = ["gvanni.bernal10@gmail.com", "chelseahumbert@yahoo.com.mx", "rociocantu4@gmail.com", "danichavezhdez@hotmail.com",
          "misaeltorres940@gmail.com", "thianagrave@gmail.com", "arantza.raiz29@yahoo.com", "ximenacovantes@hotmail.com",
          "josuemanjarrez1994@gmail.com", "cesar_humbertg@outlook.com"]

temp = list(zip(people, emails))
shuffle(temp)
people, emails = zip(*temp)

message = """\
Subject: Intercambio

Saludos cordiales, le informo que le toco regalarle a """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    for i in range(len(people)):
        # print(people[i - 1] + " -> " + people[i])
        server.sendmail(sender_email, emails[i - 1], message + people[i] + "\nNo responder a este correo")
