# -*- coding: utf-8 -*-
"""NT pro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FuSLUdUuGd1FFyomaBhJOxLFEu2mKsmd
"""

import urllib.request
import smtplib, ssl
import time

# раз в сколько секунд проверять работу сайта
X = 10

# сайт для проверки
web_page = "https://google.com"
#получение кода
code = urllib.request.urlopen(web_page).getcode()

#параметры для подключения к почтовому сервису
port = 465  # For SSL
smtp_server = "smtp.yandex.com"
sender_email = "waldopittgreen@ya.ru"       # почта отправителя
receiver_email = "asker-kakhramanov@ya.ru"  # почта получателя
password = input("Введите пароль от почты и нажмите enter: ")
message = """\
Subject: Alert

Alert"""

# булевое значение для отправки 1-го раза за "падение"
flag = False

while True:
  if code != 200:
    if flag == False:
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email, message)
          flag = True
  else:
    print('succes')
    flag = False
    time.sleep(X)