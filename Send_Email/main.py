import smtplib
import ssl
import json
import sys


def cleanArgv(argv):
    return argv.replace("_SPC_", " ")


if len(sys.argv) == 4:
    recipient = cleanArgv(sys.argv[1])
    subject = cleanArgv(sys.argv[2])
    body = cleanArgv(sys.argv[3])

else:
    sys.exit("Invalid number of arguments. Please provide the recipient, subject and body of the email.")

message = f"""\
Subject: {subject}
{body}"""

if len(sys.argv) == 4:
    with open('data.json') as f:
        data = json.load(f)

    smtp_server = "smtp.gmail.com"
    port = 465

    sender = data["sender"]
    password = data["password"]

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, message)
            print("Email sent successfully")

    except Exception as e:
        print(f"An error occurred: {e}")
