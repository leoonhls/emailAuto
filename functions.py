import os
import smtplib
from email.message import EmailMessage
from segredos import senha
import re





def emailAuto(Dest):

    #config Email
    EMAIL_ADDRESS = 'leonardohenriq123@gmail.com'
    EMAIL_PASSWORD = senha

    msg = EmailMessage()
    msg['Subject'] = 'VAGA DE EMPREGO'
    msg['From'] = 'leonardo@c3i.com.br'
    msg['To'] = Dest
    msg.set_content('Segue em anexo meu curriculum vitae.')

    with open('D:\python\emailAuto\emailAttach\CV2.pdf', 'rb') as content_file:
        content = content_file.read()
        msg.add_attachment(content, maintype='application', subtype='pdf', filename='Leonardo_Henrique_Lemos_Silva_-_Currículo.pdf')


    #send Email

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)


'''def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if(re.search(regex,email)):  
        print("\nValid Email\n")  
          
    else:  
        invalid = f'INVALID EMAIL! [{email}]'
        print(len(invalid)* '-')
        print(invalid)
        print(len(invalid)* '-')'''

def check(email):
    from validate_email import validate_email
    is_valid = validate_email(email_address=email, check_smtp=False)
    if is_valid == True:
        print("\nValid Email\n") 
        return True

    else:  
        invalid = f'INVALID EMAIL! [{email}]'
        print(len(invalid)* '-')
        print(invalid)
        print(len(invalid)* '-')
        return False