#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "stay_sun"



from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def send_all_mail(from_addr,password,to_addr,smtp_server,email_text,message_Header,file_name):
    """
    发送带附件的邮件
    :param from_addr:  发送者邮箱
    :param password:  发送者邮箱面
    :param to_addr:  发送给谁
    :param smtp_server: smtp 邮箱地址
    :param email_text: 邮件内容
    :param message_Header: 邮件主题
    :return: 0 成功  1 失败
    """
    try:
        # 考虑到编码的原因，这里统一将name属性值改成utf-8，地址的话一定是统一的邮箱地址结构，所以不考虑
        def __format_addr(s):
            name, addr = parseaddr(s)
            return formataddr((Header(name, 'utf-8').encode(), addr))

        # 邮件定义
        msg = MIMEMultipart()
        # 定义发送人，接收人，以及描述信息（主题）
        msg['From'] = __format_addr('管理员 <%s>' % from_addr)
        msg['To'] = __format_addr('亲爱的顾客 : : <%s>' % to_addr)
        msg['Subject'] = Header(message_Header, 'utf-8').encode()


        with open(file_name, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename='test.png')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)

        server = smtplib.SMTP(smtp_server, 25)
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        return 0
    except:
        return 1


def send_txt_mail(from_addr,password,to_addr,smtp_server,email_text,message_Header):
    """
    发送纯文本邮件  函数
    :param from_addr:  发送者邮箱
    :param password:  发送者邮箱面
    :param to_addr:  发送给谁
    :param smtp_server: smtp 邮箱地址
    :param email_text: 邮件内容
    :param message_Header: 邮件主题
    :return: 0 成功  1 失败
    """
    # 考虑到编码的原因，这里统一将name属性值改成utf-8，地址的话一定是统一的邮箱地址结构，所以不考虑
    def __format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    try:
        #定义纯文本格式发送邮件'plain' ， 改为html 可以发送html 代码
        msg = MIMEText(email_text, 'plain', 'utf-8')
        # 定义发送人，接收人，以及描述信息（主题）
        msg['From'] = __format_addr('管理员 : <%s>' % from_addr)
        msg['To'] = __format_addr('亲爱的顾客 : <%s>' % to_addr)
        msg['Subject'] = Header(message_Header, 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        #server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        return 0
    except:
        return 1





if __name__ == '__main__':
    send_all_mail("zhangxu@che001.com","xxxxxx","zhangxu@che001.com","mail.che001.com","内容","主题","111.png")
    send_txt_mail("zhangxu@che001.com","xxxxxx","zhangxu@che001.com","mail.che001.com","内容","主题")
    pass