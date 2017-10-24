#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import commands, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

FROM = 'CronTab@controlook.com'
USER = 'apikey'
PASS = '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'
TO = sys.argv[2]
subject = 'Logs da CronTab [controlook.com]'
texto = commands.getoutput('cat %s' % sys.argv[1])
texto += "\n Teste de construcao do corpo do e-mail com mais caracteres.\n Tentativa #01 de burlar o Spam-Score, veremos se produz resultado.\n Aparentemente funcionou, agora tem que ver a quantidade minima de caracteres pra ele considerar como uma mensagem 'padrao'\n do sistema e nao considerar mais como spamm, sera que funciona?"
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
