import pyautogui
import pyperclip
import os
import time
import win32api

class WeChat():
    pass
    def __init__(self, path):
        self.path = path

    # 打开微信
    def open_wechat(self):
        pyautogui.hotkey('win', 'd')
        time.sleep(1)
        win32api.ShellExecute(1, 'open', self.path, '', '', 1)

        # cmd = self.path+' '
        # file = os.popen(cmd)
        # file.close()
        # time.sleep(2)


    def shot(self):
        # 截图功能
        # im = pyautogui.screenshot()
        pyautogui.screenshot('./image/test.png')


    def locate(self):
        # 定位功能  定位微信搜索框
        # print(pyautogui.locateCenterOnScreen('./image/lan.png'))
        # 阻塞2秒，防止过快而检测不到搜索框的坐标
        time.sleep(2)
        x, y = pyautogui.locateCenterOnScreen('./image/lan.png')
        print(x, y)
        pyautogui.click(x=x, y=y, clicks=1, button='left')
        return (x, y)

    def send_msg_obj(self):
        # 找到好友对象
        x, y = self.locate()
        pyperclip.copy('传输')
        pyautogui.hotkey('Ctrl', 'v')
        time.sleep(2)
        # pyautogui.moveRel(0, 70)
        pyautogui.click(x, 70+y)

    def send_msg(self):
        print('输入信息')
        n = 5
        while n:
            pyperclip.copy('你好')
            pyautogui.hotkey('Ctrl', 'v')
            time.sleep(1.4)
            pyautogui.hotkey('enter')
            n -= 1
        print('end')

if __name__ == '__main__':
    path = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'
    wechat = WeChat(path)
    wechat.open_wechat()
    wechat.send_msg_obj()
    wechat.send_msg()
