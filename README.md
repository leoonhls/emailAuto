# emailAuto

Script em Python que envia o currículo em PDF para uma lista de destinatários via SMTP do Gmail.

## Uso

1. Gere uma [senha de app](https://myaccount.google.com/apppasswords) no Gmail.
2. Defina as variáveis de ambiente (ver `.env.example`):

```bash
export EMAIL_ADDRESS=seu-email@gmail.com
export EMAIL_PASSWORD=senha-de-app
export CV_PATH=emailAttach/CV.pdf
```

3. Rode `python app.py`, digite os e-mails dos destinatários e `send` para enviar.
