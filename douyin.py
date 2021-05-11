from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Actions():

    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",  # 操作系统
            "deviceName": "OnePlus5T",  # 设备 ID
            "platformVersion": "10",  # 设备版本号
            "appPackage": "com.ss.android.ugc.aweme.lite",  # app 包名
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",  # app 启动时主 Activity
            'noReset': True,  # 是否保留 session 信息，可以避免重新登录
            # 'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
            # 'resetKeyboard': True  # 将键盘给隐藏起来
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

        self.x = 500
        self.y = 1500
        self.z = 1300

    def comments(self):
        sleep(3)
        self.driver.tap([(500, 1200)], 500)

    def scroll(self):
        while True:
            self.driver.swipe(self.x, self.y, self.x, self.y-self.z)
            sleep(2)
            text = self.driver.find_element_by_id('com.ss.android.ugc.aweme.lite:id/a90').text
            print(text)
            sleep(4)

    def main(self):
        self.comments()
        self.scroll()

if __name__ == '__main__':
    action = Actions()
    action.main()