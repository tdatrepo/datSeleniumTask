from datetime import datetime
from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import schedule
import threading
import undetected_chromedriver as uc

def reo():
    import winsound
    duration = 1000  # milliseconds
    freq = 400  # Hz
    winsound.Beep(freq, duration)

def detectEle(driver, className):
    ignored_exceptions=(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException,)
    try:
        element = WebDriverWait(driver, 60*59, ignored_exceptions=ignored_exceptions).until(
                                EC.element_to_be_clickable((By.CLASS_NAME, className)))
        time.sleep(0.1)
        # reo()
        element.click()
        print('CLick DUOC', className)
    except TimeoutException:
        print("TimeoutException")
        return


def detectXpath(driver, XPATH):
    ignored_exceptions=(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException,)
    try:
        element = WebDriverWait(driver, 60*59, ignored_exceptions=ignored_exceptions).until(
                                EC.element_to_be_clickable((By.XPATH, XPATH)))
        time.sleep(0.1)
        element.click()
    except TimeoutException:
        print("TimeoutException")
        return

def click(driver, classname):
    while datetime.now().minute != 58:
        try:
            driver.find_element_by_class_name(classname).click()
            break
        except:
            continue

def run_threaded(ele):
    print("***************************************************")
    print("bat dau")
    for i in ele:
        job = threading.Thread(target=bamLiXi, args=(i,))
        job.start()
        time.sleep(15)

def bamLiXi(tk):
    if datetime.now().hour in range(9):
        return
    ran = 1
    options = Options()
    options.headless = True
    # options.add_argument('--proxy-server=49.0.2.242:8090')
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    # driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(ran)
    driver.get('https://loto567.com/mobile')
    driver.set_window_size(550, 1300)
    detectEle(driver, "loginBox")
    taikhoan = driver.find_element_by_xpath("//*[@id=\"app\"]/div[4]/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/input")
    # driver.find_element_by_class_name
    taikhoan.send_keys(tk[0])
    matkhau = driver.find_element_by_xpath("//*[@id=\"app\"]/div[4]/div[2]/div[2]/div/form/div[2]/div[2]/div[1]/input")
    matkhau.send_keys(tk[1])
    detectXpath(driver, "//*[@id=\"app\"]/div[4]/div[2]/div[2]/div/form/div[4]/button")  #dang nhap
    detectXpath(driver, "//*[@id=\"app\"]/div[4]/div[2]/div[6]/i")                      #tat slide
    detectXpath(driver, "//*[@id=\"app\"]/div[5]/div[3]")

    # job1 = threading.Thread(target=click, args=(driver,'aniBox',))
    job2 = threading.Thread(target=detectEle, args=(driver,'redBagAniBox',))
    job3 = threading.Thread(target=detectEle, args=(driver,'getRedPackImgCon',))

    # job1.start()
    job2.start()
    job3.start()

    # while datetime.now().minute != 59:
    while job2.is_alive() or job3.is_alive():
        continue
    reo()
    time.sleep(20)
    print('thanhcong ', tk[0], 'nhan dc', driver.find_element_by_xpath("//*[@id=\"app\"]/div[4]/div[5]/div/div/div[1]/div[2]").text, datetime.now())
    return

if __name__ == '__main__':
    taikhoan = [['buibappp', 'Kiemtie99n'], ['buibapppp', 'Kiemtie99n']]
    # schedule.every().hour.at('59:00').do(run_threaded, [['lun123', 'Kiemtie99n']])
    schedule.every().hour.at('59:00').do(run_threaded, [['lun123', 'Kiemtie99n']])
    while True:
        schedule.run_pending()
        time.sleep(1)

