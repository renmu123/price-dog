import os

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class Mail:
    def __init__(self):
        self.my_sender = os.getenv("SMTP_USER")
        self.my_pass = os.getenv("SMTP_PASSWORD")

    def _send(self, text: str, receiver: str) -> bool:
        ret = True
        try:
            msg = MIMEText(text, 'plain', 'utf-8')
            msg['From'] = formataddr([self.my_sender, self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr([receiver, receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "玛莎多拉"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()
        except Exception as e:
            ret = False
        return ret

    def send(self, text: str, receiver: str) -> bool:
        ret = self._send(text, receiver)
        return ret
