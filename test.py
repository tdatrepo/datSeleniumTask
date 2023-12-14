from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options as fOptions
from selenium.webdriver.chrome.options import Options as cOptions
from selenium.webdriver.edge.options import Options as eOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import sys
import time
import schedule
import threading
from seleN import reo

def selectBrowser(name):
    if name == 'c':
        options = cOptions()
        options.headless = True
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif name == 'f':
        options = fOptions()
        options.headless = True
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif name == 'e':
        options = eOptions()
        options.headless = True
        return webdriver.Edge('msedgedriver.exe')

def detectEle(driver, className):
    ignored_exceptions=(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException,)
    while 1:
        try:
            element = WebDriverWait(driver, 60*58, ignored_exceptions=ignored_exceptions).until(
                                    EC.element_to_be_clickable((By.CLASS_NAME, className)))
            time.sleep(0.1)
            element.click()
            break
        except TimeoutException:
            print("TimeoutException")
            return

def bamLiXi(tk):
    # if datetime.now().hour in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    #     return
    ran = 3
    driver = selectBrowser(tk[2])
    time.sleep(5)
    driver.get('https://loto567.com')
    time.sleep(5)
    driver.maximize_window()
    time.sleep(ran)
    login = driver.find_element_by_xpath("//button[@class='el-button login el-button--default']")
    login.click()
    time.sleep(ran)
    taikhoan = driver.find_element_by_xpath("//input[@class='el-input__inner']")
    taikhoan.send_keys(tk[0])
    time.sleep(ran)
    matkhau = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/form/div[2]/div/div/input")
    matkhau.send_keys(tk[1])
    time.sleep(ran)
    login2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/span/button")
    login2.click()
    
    # time.sleep(ran)
    # driver.refresh()
    # time.sleep(ran)
    # driver.find_element_by_class_name("chatRoomButton").click()
    # time.sleep(ran)
    # mo = driver.find_element_by_class_name("openBtn") xoso8822

    time.sleep(ran)
    driver.get('https://loto567.com/mobile')
    driver.set_window_size(550, 1300)
    time.sleep(ran)
    driver.get('https://loto567.com/mobile/#/chatRoom?firstBackPath=%2F')
    # https://loto567.com/mobile/#/chatRoom?firstBackPath=%2F
    # getRedPackImgCon
    # redBagAniBox redBagImg {red_id: "3404"} https://loto567.com/server/chat/grabred
    # redBagWrap
    # collar
    # <div data-v-457ec524="" data-v-352a1e2a="" class="redBagAniBox"><div data-v-457ec524="" class="aniBox"><img data-v-457ec524="" src="/mobile/static/img/fireworks.b6830e2f.png" alt="" class="fireworks fireworksAni"><img data-v-457ec524="" src="/mobile/static/img/redBagBg.9d158740.png" alt="" class="redBagBg redBagBgAni"><img data-v-457ec524="" src="/mobile/static/img/redBag.7c73557f.png" alt="" class="redBag redBagAni2"><div data-v-457ec524="" class="redBagTxt1 redBagTxtLoopAni"><div data-v-457ec524="" class="mask"></div></div><div data-v-457ec524="" class="redBagTxt2 redBagTxtLoopAni"><div data-v-457ec524="" class="mask"></div></div></div><div data-v-457ec524="" class="closeBtn"><i data-v-457ec524="" class="iconfont icon-icon_close_24"></i></div></div>
    job1 = threading.Thread(target=detectEle, args=(driver,'redBagAniBox',))
    job2 = threading.Thread(target=detectEle, args=(driver,'getRedPackImgCon',))

    job1.start()
    job2.start()
    while job1.is_alive():
        continue
    reo()
    time.sleep(10)
    print('thanhcong '+tk[0])
    print(datetime.now())
    return

def run_threaded(str):
    while datetime.now().minute in range(59):
        try:
            print(str)
        except:
            continue

if __name__ == '__main__':
    schedule.every().hour.at('59:40').do(bamLiXi, [sys.argv[1], 'Kiemtie99n', sys.argv[2]])
    while True:
        schedule.run_pending()
        time.sleep(1)
