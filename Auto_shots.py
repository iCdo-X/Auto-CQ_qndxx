"""
    @py:自动截屏
    @author:iCdo_X.
    @使用前需安装 pillow 库
    @注：本脚本仅为个人提供技术经验！
"""
import requests
import re
from PIL import Image, ImageDraw, ImageFont

def get_url():  # 获取最新一期大学习的url
    html = requests.get('http://news.cyol.com/gb/channels/vrGlAKDl/index.html').text
    url = re.findall('href="(.*?)" target', html)[0]
    return url

def get_title(the_id):  # 获取期数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30'
    }
    html = requests.get('https://h5.cyol.com/special/daxuexi/%s/index.html' % the_id,headers=headers)
    html.encoding='utf-8'
    html=html.text
    title = re.findall('<title>(.*?)</title>',html)[0]
    return title
    
def get_id(url):  # 从url中提取本期的id
    the_id = url.split('/')[-2]
    return the_id

def get_icon(the_id):  # 根据id获取本期的分享缩略图
    addr = 'http://h5.cyol.com/special/daxuexi/%s/images/icon.jpg' % the_id
    
    icon = requests.get(addr).content
    with open('icon.jpg', 'wb') as f:
        f.write(icon)


def get_end(the_id):  # 根据id获取本期的完成图片
    addr = 'http://h5.cyol.com/special/daxuexi/%s/images/end.jpg' % the_id
    end = requests.get(addr).content
    with open('end.jpg', 'wb') as f:
        f.write(end)


def change(info,raw='raw.png', icon='icon.jpg', touxiang='touxiang.jpg'):  # 以raw为底图制作图片result
    result = Image.open(raw)
    icon = (Image.open(icon)).resize((80, 80), resample=0)
    touxiang = (Image.open(touxiang)).resize((80, 80), resample=0)
    result.paste(icon, (123, 330))
    result.paste(touxiang, (13, 132))

    '''========================以下为加文字部分==========================='''
    font = ImageFont.truetype('C:/windows/fonts/Simhei.ttf', size=32)
    draw = ImageDraw.Draw(result)
    draw.text((215, 355), info['title'], fill='black', font=font)  # 期数
    draw.text((116, 135), info['nickname'], fill=(87, 107, 149), font=font)  # 微信昵称
    draw.text((116, 230), info['text'], fill='black', font=font)  # 信息
    result.save('result.png')

def run():
    url = get_url()
    Id = get_id(url)
    title_info = get_title(Id)
    get_icon(Id)
    get_end(Id)
    info = {'nickname':'weix.','text':'网络201 从陈明','title':title_info}
    change(info)
run()
