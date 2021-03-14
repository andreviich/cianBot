from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
import requests
import time
import telebot
import os
# import eel
from selenium.webdriver.common.by import By
from threading import Thread
import selenium
# eel.init('web')
# @eel.expose
counter = 0
bot = telebot.TeleBot('1628963451:AAHowBZdULmLzKhcgyXEhexgE1VxDeyCG4k')
cities = ['Санкт-Петербург', 'Мурино', 'Кудрово']
def reBrowse():
    browser = webdriver.Chrome(executable_path=chromedriver, options=options)
    return browser
def initChrome():
    comm = os.system('chrome --remote-debugging-port=3000 --user-data-dir="c:\selenium\AutomationProfile"')    
# @eel.expose
th1 = Thread(target=initChrome)
th1.start()
def sort(browser):
    try:
        browser.find_element_by_xpath('//*[@id="leads-listing-frontend"]/div/div/div/main/div[1]/div/div[3]/div/div[2]').click()
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div').click()
        browser.find_element_by_xpath('//*[@id="leads-listing-frontend"]/div/div/div/main/div[1]/div/div[3]/div/div[3]').click()
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div').click()
        browser.find_element_by_xpath('//*[@id="leads-listing-frontend"]/div/div/div/main/div[1]/div/div[3]/div/div[6]/button/span').click()
        time.sleep(0.5)
    except Exception as e:
        print(e)
def startParsing(counter):
    time.sleep(3)
    chromedriver = 'chromedriver'
    options = webdriver.ChromeOptions()
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    options.add_experimental_option("debuggerAddress", "127.0.0.1:3000")
    # options.add_argument('headless') 
    browser = webdriver.Chrome(executable_path=chromedriver, options=options)
    try:
        browser.get('https://my.cian.ru/leads')
    except:
        pass
    sort(browser)
    while True:
        try:
            browser.get('https://cian.ru')
            time.sleep(0.5)
            browser.get('https://cian.ru/novostrojki/')
            time.sleep(0.5)
            browser.get('https://my.cian.ru/leads')
            sort(browser)
        except:
            pass
        # browser.find_element_by_xpath('//*[@id="leads-listing-frontend"]/div/div/div/main/div[1]/div/div[3]/div/div[6]/button/span').click()
        requiredHtml = browser.page_source
        soup = BeautifulSoup(requiredHtml, 'html5lib')
        try:
            threes = browser.find_elements_by_class_name('f341f0ad46--lead-item--AgRi4')
        except:
            threes = list()
        time.sleep(3)
        for three in threes:
            text = ''
            try:
                text = three.find_element_by_css_selector("[data-name='MainGeoHeader']")
                text = text.find_element_by_css_selector('span').text
            # except selenium.common.exceptions.StaleElementReferenceException:
            #     time.sleep(2)
            #     browser = reBrowse()

            #     text = three.find_element_by_css_selector("[data-name='MainGeoHeader']").find_element_by_css_selector('span').text
            except:
                pass
            if text in cities:
                time.sleep(2)
                btn = three.find_element_by_css_selector("button")
                try:
                    btn.click()
                except:
                    pass
                print(text)
                time.sleep(1)

            # time.sleep(1)

            if len(browser.window_handles) > 1:
                for x in range(1, len(browser.window_handles)):
                    browser.switch_to.window(browser.window_handles[x])
                    browser.find_element_by_xpath('//*[@id="lk-container"]/div/div/div/main/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/button').click()
                    time.sleep(2)
                    browser.find_element_by_xpath('//*[@id="lk-container"]/div/div/div/main/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/button').click()
                    time.sleep(2)
                    counter = counter + 1
                    print(f'Куплено {counter} заявок')
                    bot.send_message('-588015907', 'Новая заявка куплена')
                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
                    time.sleep(2)
startParsing(counter)     

# eel.start('index.html')