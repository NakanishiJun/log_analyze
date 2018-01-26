# -*- coding:utf-8 -*-
import datetime, sys, re, smtplib, glob
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

#日付の設定
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday

POST = 0
GET = 0
path = './*-access_log'
file_name = []
file_name = glob.glob(path)

# output_logs = str(yesterday)+ "の出力ログ数 : "+str(POST+GET)
# output_post = "POST =" + str(POST)
# output_get = "GET =" + str(GET)
FROM_ADDRESS = 'admin@elmstarz.com'
MY_PASSWORD = 'xxxxxxxxxxxxx'
TO_ADDRESS = 'j.nakanishi@gingerapp.co.jp'
BCC = ''
SUBJECT = '昨日のログの出力数'
BODY = ''
print(file_name)

for f_n in file_name:
    BODY += '\n' + str(yesterday)+ 'の' + str(f_n) + 'の出力ログ数：'
    f = open(str(f_n), 'r')
    GET = 0
    POST = 0 
    for line in f:
        line = line.strip()
        if "GET" in line:
            GET += 1
        if "POST" in line:
            POST += 1
        out_put_logs = GET + POST
    BODY += str(out_put_logs) + '\n'
    f.close()
print (out_put_logs)

def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.elmstarz.com', 587)
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg)

