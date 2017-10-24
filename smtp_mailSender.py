#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import commands, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

USER = 'user'
PASS = 'password'
FROM = 'user@example.com'
TO = sys.argv[2]
subject = 'Title of subject...'

# Adding content of a file and appending to body of the message
texto = commands.getoutput('cat %s' % sys.argv[1])
# Adding plain text to the body
texto += "\n Conteúdo do e-mail em texto puro, adicionando qualquer coisa...\n Assinado: Joao Spammer"

msg = MIMEMultipart()
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = subject
msg.attach(MIMEText(texto))

try:
    gm = smtplib.SMTP('smtp.sendgrid.net:587')
    gm.ehlo()
    gm.starttls()
    gm.login(USER, PASS)
    gm.sendmail(FROM, TO, msg.as_string())
    gm.close()
except Exception, erro:
    errorMsg = "Não foi possível enviar o e-mail.\n Erro: %s" % erro
    print '%s' % errorMsg
else:
    print 'E-mail enviado.'

# USAGE: python ./smtp_mailSender.py /home/file.log user@email.com
