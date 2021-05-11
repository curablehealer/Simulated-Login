from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def wechat():
    desired_caps = {
        "platformName": "Android",  # 操作系统
        "deviceName": "OnePlus5T",  # 设备 ID
        "platformVersion": "10",  # 设备版本号
        "appPackage": "com.tencent.mm",  # app 包名
        "appActivity": ".ui.LauncherUI",  # app 启动时主 Activity
        'noReset': True,  # 是否保留 session 信息，可以避免重新登录
        'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
        'resetKeyboard': True  # 将键盘给隐藏起来
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(5)
    wait = WebDriverWait(driver, 30)
    # 点击登录按钮
    # login_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/hi4")))
    # # login_btn = driver.find_element_by_id('com.tencent.mm:id/hi4').click()
    # login_btn.click()
    # # 获取手机号文本框
    # phone_text = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bxz")))
    # # 填写手机号文本框
    # phone_text.send_keys("")
    # sleep(2)
    # next_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/fz0")))
    # next_btn.click()
    # sleep(2)
    # pass_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/bxz")))
    # pass_btn.send_keys("")
    # login = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/fz0")))
    # login.click()
    # sleep(2)
    # sheng = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/fzg")))
    # 获取并点击第一个联系人
    sheng = driver.find_element_by_xpath(
        '//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView')
    # print(sheng, type(sheng))
    sheng.click()
    print('点击')
    sleep(2)
    # 定位发送文本框
    msg = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/auj")))
    n = 1
    while n < 5:
        # 输入发送的信息
        msg.send_keys("您好")
        # 定位发送按钮并点击
        sd = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/ay5")))
        sd.click()
        n += 1
        sleep(5)

if __name__ == '__main__':
    wechat()





