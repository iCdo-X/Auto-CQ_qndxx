"""
    @py:自动qndxx学习
    @author:iCdo_X.
    @注：本脚本仅为个人提供技术经验！
"""

import requests
import re

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
    

def main():
    '''
        * 用户识别码 openid是一个长度为28个字符
        * 由数字、大小写字母与符号组成的串
    '''
#     微信OpenID
    openid = ['']
#     接受邮箱地址
    email_user = ['']
    # 获取最新的课程 Id   
    id = get_new_course_id(1)
    name = get_new_course_id(2)
    for i in range(0,len(openid)):
        # id = '142'
        status_info = auto_lean(openid[i],id)
        send_mail(status_info,name,email_user[i])
main()
