"""
    @py:自动qndxx学习
    @author:iCdo_X.
    @注：本脚本仅为个人提供技术经验！
"""
import Auto_send_pic
import Auto_shots
import requests
import re
import os

def auto_lean(openid,id):
    url = 'http://stu.redrock.team/api/course/studyCourse?openid='+openid+'&id='+id
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307001d)'
    }
    result = requests.get(url=url,headers=headers).text
    result = re.findall('"status":(.*?),"message"',result)
    if result[0]=='200':
        print('自动学习成功!')
    elif result[0]=='201':
        print('该课程已学习!')
    else:
        print('Error!')
    
def get_new_course_id():
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
    print(result['data'][0]['id'])
    # 打印最新一期的课程 NAME
    print(result['data'][0]['name'])
    return id

def main():
    '''
        * 用户识别码 openid是一个长度为28个字符
        * 由数字、大小写字母与符号组成的串
    '''
    # o1Nb9jvaNIRgPj89csPTkhs5Hu1s
    openid = ''
    # 获取最新的课程 Id   
    id = get_new_course_id()
    auto_lean(openid,id)
main()
Auto_shots.run()
Auto_send_pic.main()
os.system('pause')
