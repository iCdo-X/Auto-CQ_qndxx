"""
    @py:自动qndxx学习
    @author:iCdo_X.
    @注：本脚本仅为个人提供技术经验！
"""

import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def auto_lean(openid,id):
    url = 'http://stu.redrock.team/api/course/studyCourse?openid='+str(openid)+'&id='+str(id)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307001d)'
    }
    result = requests.get(url=url,headers=headers).text
    result = re.findall('"status":(.*?),"message"',result)
    if result[0]=='200':
        return '自动学习成功!'
    elif result[0]=='201':
        return '该课程已学习!'
    else:
        return 'Error!'

    
def get_new_course_id(flag):
    import time
    time = round(time.time()*1000)
    url = 'http://stu.redrock.team/new_course.json?time='+str(time)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307001d)'
    }
    result = requests.get(url=url,headers=headers).text
    result = result.replace('null','"null"')
    result = eval(result)
    # 打印最新一期的课程 ID
    # print(result['data'][0]['id'])
    # 打印最新一期的课程 NAME
    # print(result['data'][0]['name'])
    if flag==1:
        return result['data'][0]['id']
    else:
        return result['data'][0]['name']
    
def send_mail(text,course_name,my_user):
    my_sender = '2101543615@qq.com'  # 发件人邮箱账号
    my_pass = 'emoxacplyrwdccaj'  # 发件人邮箱授权码，第一步得到的
    ret = True
    try:
        # msg=MIMEText('填写邮件内容','plain','utf-8')
        mail_msg = f"""
                        <p>{course_name}{text}</p>
                        <p>该交截图了!!!</p>
                    """
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(["托马斯提醒你", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["呜呜呜", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "老年大学习来了"  # 邮件的主题，也可以说是标题
        '''
        QQ邮箱使用下面这种方式才成功
        '''
        # 发件人邮箱中的SMTP服务器，端口是25
        # server=smtplib.SMTP("smtp.qq.com", 25)
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465，固定的，不能更改 使用SSL模式
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.set_debuglevel(1)
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件信息
        server.quit()  # 关闭连接
    except Exception as err:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(err)
        ret = False
    return ret

def main():
    '''
        * 用户识别码 openid是一个长度为28个字符
        * 由数字、大小写字母与符号组成的串
    '''
    # o1Nb9jvaNIRgPj89csPTkhs5Hu1s 明
    # o1Nb9ju13Y9oiOGR75WxhgEMjd5s 康
    # o1Nb9jr1AHTk3YdyryAHxs6v9NQg 周逼
    # o1Nb9jr1AHTk3YdyryAHxs6v9NQg 张航
    openid = ['o1Nb9jvaNIRgPj89csPTkhs5Hu1s','o1Nb9ju13Y9oiOGR75WxhgEMjd5s','o1Nb9jr1AHTk3YdyryAHxs6v9NQg','o1Nb9jr1AHTk3YdyryAHxs6v9NQg']
    email_user = ['2101543615@qq.com','2089221335@qq.com','2579507340@qq.com','1610753015@qq.com']
    # 获取最新的课程 Id   
    id = get_new_course_id(1)
    name = get_new_course_id(2)
    for i in range(0,len(openid)):
        # id = '142'
        status_info = auto_lean(openid[i],id)
        send_mail(status_info,name,email_user[i])
main()