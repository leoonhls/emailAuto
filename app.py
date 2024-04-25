from functions import *

dest = []


while True:
        newEmail = input('E-mail do destinatário (Digite "send" para enviar todos): ')
        if newEmail == 'send':
            break

        if newEmail not in dest:
                dest.append(newEmail)
        print(dest)
    
    

for email in dest:
    emailAuto(Dest=email)
    print('Enviado para: ', email)