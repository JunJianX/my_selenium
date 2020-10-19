# coding=utf-8
# 导入网页驱动软件
from selenium import webdriver
# 导入WebDriverWait等待模块
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
 
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# 括号内为phantomjs安装位置
driver = webdriver.PhantomJS(executable_path="D:\\Softwares\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
# 访问的网址（以央视网为例）
# driver.get("https://iot.console.aliyun.com/lk/monitor/debug?pk=a1hiSOeUajy&pn=WalkingPad_R1S&dn=100801200831000002")
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
# driver.find_elements_by_xpath('//span[@class="btn_icon"]')[1].click()
ret = driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/span/input").clear()
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/span/input").send_keys("xujunjian@kingsmith-com.onaliyun.com")
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[3]/div/button").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/span/input").clear()
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[2]/div[2]/span/input").send_keys("EvKutm@)1bNjQCl0Sy!MkQs6EZv4M!aT")
driver.find_element_by_xpath("//*[@id=\"--aliyun-xconsole-app\"]/div/div[1]/div[2]/div[3]/div/form/div[3]/div/button/span").click()
# 等待登录页面加载完成，WebDriverWait （后面有等待方法介绍）
# WebDriverWait(driver, 10, 0.5).until(lambda diver:driver.find_element_by_xpath('//a[@class="dl"]'),message="")
time.sleep(2)
# driver.find_element_by_class_name('物联网平台').click()
# driver.find_element_by_link_text('物联网平台').click()
# driver.get("https://iot.console.aliyun.com")
driver.implicitly_wait(0)
driver.get("https://iot.console.aliyun.com/lk/monitor/debug?pk=a1hiSOeUajy&pn=WalkingPad_R1S&dn=100801200831000002")
# driver.implicitly_wait(20)
time.sleep(8)
# ret = driver.find_element_by_xpath("//*[@id=\"linkplatform\"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/label[2]").click()
# print(ret)
# time.sleep(20)
# driver.implicitly_wait(60)
# driver.find_element_by_xpath("//*[@id=\"linkplatform\"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/label[2]/span[2]").click()
# driver.find_element_by_xpath("//*[text()='服务调用']").click()
# driver.implicitly_wait(60)
# time.sleep(5)
# mypath='//*[@id="linkplatform"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/header/div[1]/span[1]/div/div/div/ul/li[5]/div'
# WebDriverWait(driver,timeout=60,poll_frequency=1,ignored_exceptions=None).until(EC.visibility_of_element_located((By.XPATH,mypath)))
# while(1):
#     try:
time.sleep(8)
ret = driver.find_element_by_xpath("//*[text()='服务调用']").click()
print(62)
    #     break
    # except:
    #     print('error')
    #     time.sleep(3)

# time.sleep(20)
# ret = driver.find_element_by_xpath("//*[@class='next-select-trigger-search']").click()
ret = driver.find_element_by_xpath("//*[@placeholder='请选择']").click()
print("67")

time.sleep(8)
ret = driver.find_element_by_xpath("//*[text()='8266升级 (board_upgrade)']").click()
print("71")
print(ret)
time.sleep(4)

driver.find_element_by_css_selector('textarea.ace_text-input').send_keys("{\"board_upgrade\":\"http://121.89.198.81//d//0011\"}")
time.sleep(4)
i=1000
while(1):
    i=i-1
    ret = driver.find_element_by_xpath("//*[text()='发送指令']").click()
    time.sleep(60)
    print(1000-i)
# 截取登录框的页面保存到相应位置
# driver.save_screenshot('demo\\img\\login1.png')
# # 定位登录页面用户名和密码元素并模拟填入用户名和密码
# driver.find_element_by_name("username").send_keys('xxxxxxxxxxx')
# driver.find_element_by_name("passwd_view").send_keys('xxxxxxxxxxx')
# # 模拟点击登录按钮登录
# driver.find_element_by_link_text('登录').click()
#
# WebDriverWait(driver, 10, 0.5).until(lambda diver:driver.find_elements_by_xpath('//span[@class="btn_icon"]'),message="")
# time.sleep(2)
# # 截取登录后的页面保存到相应位置
# driver.save_screenshot('demo\\img\\login2.png')
#
# # 模拟点击按钮跳转体育页面
# driver.find_element_by_link_text('体育').click()
# WebDriverWait(driver, 10, 0.5).until(lambda diver:driver.find_element_by_link_text('CBA'),message="")
# time.sleep(2)
#
# # 截取体育页面保存到相应位置
# driver.save_screenshot('demo\\img\\sport.png')

# 退出驱动关闭所有窗口
driver.quit()