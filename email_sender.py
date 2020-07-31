import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

content = Path('./index.html')
c = Template(content.read_text())
message = EmailMessage()
message['from'] = '<sender_name>'
message['to'] = '<receiver_email_id>'
message['subject'] = 'Greetings'
message.set_content(c.substitute(name = '<receiver_name>'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.ehlo()
    s.starttls()
    s.login('<sender_email_id>', '<sender_email_pass>')
    s.send_message(message)
    print('done')