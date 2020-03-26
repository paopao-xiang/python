import smtplib

from class_0326.conf import emailname, emailpwd
from email.mime.text import MIMEText#用来解析邮件格式
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication#添加附件文件

# 总的邮件内容，分为不同的模块
msg_total = MIMEMultipart()#总模块
msg_total['Subject'] = 'hello'

# 正文模块
msg_raw = """<p style="color:red">你好</p>
"""
msg = MIMEText(msg_raw, 'html')#原始格式解析为HTML
msg_total.attach(msg)

# 附件模块
mfile = MIMEApplication(open('demo.txt', 'rb').read())
# 添加附件的头信息
mfile.add_header('Content-Disposition', 'attachment', filename='demo')
# 附件摸快添加到总的里面
msg_total.attach(mfile)

with smtplib.SMTP_SSL('smtp.163.com', 25) as server:
    # 登录
    server.login(emailname, emailpwd)
    # msg = '''\\
    # From: yuze
    # Subject: test
    #
    # This is a test'''

    # 发送邮件
    server.sendmail(emailname, emailpwd, msg_total.as_string())# msg_total.as_string()转换msg格式，因为msg现在是HTML格式


    # 作业：新建一个类 class MyEmail, 完成带有附件的邮件发送。