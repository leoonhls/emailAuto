import os
import smtplib
from email.message import EmailMessage
import re





def emailAuto(Dest):

    #config Email
    EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
    EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

    msg = EmailMessage()
    msg['Subject'] = 'VAGA DE EMPREGO'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = Dest
    msg.set_content('Segue em anexo meu curriculum vitae.')

    with open(os.environ.get('CV_PATH', 'emailAttach/CV.pdf'), 'rb') as content_file:
        content = content_file.read()
        msg.add_attachment(content, maintype='application', subtype='pdf', filename=os.environ.get('CV_FILENAME', 'Curriculo.pdf'))


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