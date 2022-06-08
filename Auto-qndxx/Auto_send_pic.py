"""
    @py:自动qndxx学习
    @author:iCdo_X.
    @注：本脚本仅为个人提供技术经验！
"""
import win32gui
import win32con
import win32clipboard
from PIL import Image
from ctypes import *
import os
def main():
    msg = Image.open(input("输入图片地址："))
    msg.save("test.bmp")  # 转换格式为BMP
    msg = windll.user32.LoadImageW(0, "test.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
    if msg != 0:  # 由于图片编码问题  图片载入失败的话  aString 就等于0
        # 复制消息到剪切板
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_BITMAP, msg)
        win32clipboard.CloseClipboard()
        # 删除转换后的BMP文件（不影响源文件）
        os.remove("test.bmp")
        # 窗口名字
        name = input("窗口名：")
        # 康瀚文等139个会话
        # 获取窗口句柄
        handle = win32gui.FindWindow(None, name)
        # 将窗口调到前台
        win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
        # 将剪贴板消息发送到窗体
        win32gui.SendMessage(handle, win32con.WM_PASTE, 0,0)
        # 模拟按下回车键
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)