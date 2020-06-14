import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

content = Path('./index.html')
c = Template(content.read_text())
message = EmailMessage()
message['from'] = 'No name'
message['to'] = '<email id>'
message['subject'] = 'Greetings'
message.set_content(c.substitute(name = '<name>'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.ehlo()
    s.starttls()
    s.login('<email id>', '<password>')
    s.send_message(message)
    print('done')