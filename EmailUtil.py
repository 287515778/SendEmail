import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def send_email(to=None, msg_body=None, msg_body_type='html'):

    if msg_body is None:
        return

    if to is None:
        to = "xxx.com"

    server = smtplib.SMTP('smtp.sina.com')
    # server.set_debuglevel(1)
    server.starttls()
    me = "xxx@sina.com"

    # Next, log in to the server
    server.login(me, "xxx")

    msg = MIMEMultipart()
    msg['Subject'] = Header('报警邮件', 'utf-8')
    # Envolope sender mismatch with header from 错误解决方式
    # msg[‘From’]的内容要与发件人保持一致，可能新浪在检查一致性时，判断过于简单，msg[‘From’]的Header不能添加第2个参数”utf-8”，否则检查不能通过
    msg['From'] = Header(me)
    msg.attach(MIMEText(msg_body, msg_body_type))
    server.sendmail(me, to, msg.as_string())
    server.close()


def build_msg_body(err_msg, url, params):
    msg_body = '''
    <html>
      <head></head>
      <body>
        <p>err_msg: %s<br>
           url: %s<br>
           params: %s
        </p>
      </body>
    </html>
    ''' % (err_msg, url, params)
    return msg_body
