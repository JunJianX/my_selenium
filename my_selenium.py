# coding=utf-8
# 导入网页驱动软件
from selenium import webdriver
# 导入WebDriverWait等待模块
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random

def smart_wait(element_id):
    for i in range(60):
        if i>=59 :
            print("timeout")
        try:
            if driver.find_element_by_xpath(element_id) :
                break
        except:
            print("waitting for element")
            time.sleep(1)

def smart_wait_and_click(element_id):
    for i in range(60):
        if i>=59 :
            print("timeout")
        try:
            if driver.find_element_by_xpath(element_id) and driver.find_element_by_xpath(element_id).click():
                break
        except:
            print("waitting for element")
            time.sleep(1)
# urls=["{\"board_upgrade\":\"http://121.89.198.81//d//0011\"}",
#       "{\"board_upgrade\":\"http://121.89.198.81//d//0010\"}",
#       "{\"board_upgrade\":\"http://121.89.198.81//d//0009\"}",
# ]
#1为模组 0为mcu
define_mcu_or_board = 0

dn = '100801201106000001'

urls=["{\"board_upgrade\":\"http://121.89.198.81/d/v0002linkkitapp@esp32devkitc_sign.bin\"}",
      "{\"board_upgrade\":\"http://121.89.198.81/d/v0002linkkitapp@esp32devkitc_sign.bin\"}",
]
mcu_urls=[
    #   "{\"mcu_upgrade\":\"http://121.89.198.81/d/R1-ble-wifi_v3_20200911.bin\"}",
      "{\"mcu_upgrade\":\"http://49.232.142.246/d/R1-ble-wifi_v6_20201106_no_safety_error.bin\"}",
    #   "{\"mcu_upgrade\":\"http://121.89.198.81/d/v0002linkkitapp@esp32devkitc_sign.bin\"}",
]
driver = webdriver.PhantomJS(executable_path="D:\\Softwares\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
chrome_options = Options()
prefs = {
   'profile.default_content_setting_values': {
    'images': 2,    # 禁用图片的加载
    }
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.set_page_load_timeout(60)
main_win = driver.current_window_handle
all_win = driver.window_handles
print('Opening page')

driver.get("https://signin.aliyun.com/login.htm#/login")
# 最大化浏览器

driver.maximize_window()
# 
ret = driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/span/input").clear()
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/span/input").send_keys("xujunjian@kingsmith-com.onaliyun.com")
driver.find_element_by_xpath("//*[text()='下一步']").click()

# smart_wait_and_click("//*[text()='登录']")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/span/input").clear()
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/span/input").send_keys("EvKutm@)1bNjQCl0Sy!MkQs6EZv4M!aT")
driver.find_element_by_xpath("//*[text()='登录']").click()
# 
# WebDriverWait(driver, 10, 0.5).until(lambda diver:driver.find_element_by_xpath('//a[@class="dl"]'),message="")
# time.sleep(10)
smart_wait("//*[text()='费用']")

driver.get("https://iot.console.aliyun.com/lk/monitor/debug?pk=a1hiSOeUajy&pn=WalkingPad_R1S&dn="+dn)

driver.implicitly_wait(25)

# time.sleep(6)
smart_wait("//*[text()='服务调用']")
smart_wait_and_click("//*[text()='服务调用']")    
    
# ret = driver.find_element_by_xpath("//*[text()='服务调用']").click()
smart_wait("//*[@placeholder='请选择']")  
ret = driver.find_element_by_xpath("//*[@placeholder='请选择']").click()
time.sleep(1)

if(define_mcu_or_board == 1):
    ret = driver.find_element_by_xpath("//*[text()='8266升级 (board_upgrade)']").click()
elif (define_mcu_or_board == 0):
    ret = driver.find_element_by_xpath("//*[text()='升级mcu (mcu_upgrade)']").click()

# driver.find_element_by_css_selector('textarea.ace_text-input').send_keys("{\"board_upgrade\":\"http://121.89.198.81//d//0011\"}")
# time.sleep(4)
times=1000

while(1):
    times=times-1
    driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(Keys.CONTROL+'a')
    driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(Keys.DELETE)
    if define_mcu_or_board== 1 :
        driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(urls[random.randint(0,len(urls)-1)])
    elif define_mcu_or_board == 0 :
        driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(mcu_urls[random.randint(0,len(mcu_urls)-1)])
    ret = driver.find_element_by_xpath("//*[text()='发送指令']").click()
    time.sleep(60)
    print(1000-times)
driver.quit()