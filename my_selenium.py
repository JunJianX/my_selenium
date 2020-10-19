# coding=utf-8
# 导入网页驱动软件
from selenium import webdriver
# 导入WebDriverWait等待模块
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
urls=["{\"board_upgrade\":\"http://121.89.198.81//d//0011\"}",
      "{\"board_upgrade\":\"http://121.89.198.81//d//0010\"}",
      "{\"board_upgrade\":\"http://121.89.198.81//d//0009\"}",
]
# try:
#     with open("./records.log" ,"wr") as f:
# except :
#     f= open("./records.log",'w')
# print(len(urls))
# print(random.randint(0,len(urls)-1))
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# 括号内为phantomjs安装位置
driver = webdriver.PhantomJS(executable_path="D:\\Softwares\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
# 访问的网址（以央视网为例）
chrome_options = Options()
prefs = {
   'profile.default_content_setting_values': {
    'images': 2,    # 禁用图片的加载
    }
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(5)
driver.set_page_load_timeout(15)
main_win = driver.current_window_handle
all_win = driver.window_handles
print('Opening page')

driver.get("https://signin.aliyun.com/login.htm#/login")
# 最大化浏览器

driver.maximize_window()
# 模拟点击登录按钮登录弹出登录框（后面有定位元素方法介绍）
ret = driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/span/input").clear()
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/span/input").send_keys("xujunjian@kingsmith-com.onaliyun.com")
driver.find_element_by_xpath("//*[text()='下一步']").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/span/input").clear()
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/span/input").send_keys("EvKutm@)1bNjQCl0Sy!MkQs6EZv4M!aT")
driver.find_element_by_xpath("//*[text()='登录']").click()
# 等待登录页面加载完成，WebDriverWait （后面有等待方法介绍）
# WebDriverWait(driver, 10, 0.5).until(lambda diver:driver.find_element_by_xpath('//a[@class="dl"]'),message="")
time.sleep(10)
# driver.implicitly_wait(25)
driver.get("https://iot.console.aliyun.com/lk/monitor/debug?pk=a1hiSOeUajy&pn=WalkingPad_R1S&dn=100801200831000002")
driver.implicitly_wait(25)
# time.sleep(16)
ret = driver.find_element_by_xpath("//*[text()='服务调用']").click()
ret = driver.find_element_by_xpath("//*[@placeholder='请选择']").click()
time.sleep(8)
ret = driver.find_element_by_xpath("//*[text()='8266升级 (board_upgrade)']").click()
time.sleep(4)
# driver.find_element_by_css_selector('textarea.ace_text-input').send_keys("{\"board_upgrade\":\"http://121.89.198.81//d//0011\"}")
# time.sleep(4)
times=1000

urls=["{\"board_upgrade\":\"http://121.89.198.81//d//0011\"}",
      "{\"board_upgrade\":\"http://121.89.198.81//d//0010\"}",
      "{\"board_upgrade\":\"http://121.89.198.81//d//0009\"}",
]
# with open("./records.log" ,"w") as f:

while(1):
    times=times-1
    driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(Keys.CONTROL+'a')
    driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(Keys.DELETE)
    driver.find_element_by_css_selector('textarea.ace_text-input').send_keys(urls[random.randint(0,len(urls)-1)])
    ret = driver.find_element_by_xpath("//*[text()='发送指令']").click()
    time.sleep(60)
    print(1000-times)
driver.quit()