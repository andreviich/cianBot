from tkinter import *
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
import requests
import time
import telebot
import os
from selenium.webdriver.common.by import By
from threading import Thread
import selenium
from threading import Thread
counter = 0
bot = telebot.TeleBot('1628963451:AAHowBZdULmLzKhcgyXEhexgE1VxDeyCG4k')
cities = ['Санкт-Петербург', 'Мурино', 'Кудрово', 'Ленсоветовский', 'Бугры']
window = Tk()
window.title("Бот циан")
window.geometry('250x150')  
toParse = True
counter = 0
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
# def parse():
#     th2 = Thread(target=startParsing)
#     th2.start()
def startParsing(counter):
    try:
        captcha = browser.find_element_by_xpath('//*[@id="form_captcha"]')
        captcha.click()
        sort(browser)
        counter = 0
    except:
        pass
    button1.destroy()
    time.sleep(5)
    chromedriver = 'chromedriver'
    options = webdriver.ChromeOptions()
    # options.accept_untrusted_certs = True
    # options.assume_untrusted_cert_issuer = True
    options.add_experimental_option("debuggerAddress", "127.0.0.1:3020")
    browser = webdriver.Chrome(executable_path=chromedriver, options=options)
    sort(browser)
    while True:
        print(counter)
        try:
            captcha = browser.find_element_by_xpath('//*[@id="form_captcha"]')
            captcha.click()  
            sort(browser)
            # counter = 0
        except:
            pass
        
        if counter > 5:
            browser.refresh()
            time.sleep(1)
            try:
                captcha = browser.find_element_by_xpath('//*[@id="form_captcha"]')
                captcha.click()
                sort(browser)
                counter = 0
            except:
                sort(browser)
            counter = 0
        time.sleep(5)
        counter +=1
        sort(browser)
        try:
            browser.find_element_by_xpath('//*[@id="leads-listing-frontend"]/div/div/div/main/div[1]/div/div[3]/div/div[6]/button/span').click()
        except Exception as e:
            print(e)
        # requiredHtml = browser.page_source
        # soup = BeautifulSoup(requiredHtml, 'html5lib')
        try:
            threes = browser.find_elements_by_class_name('f341f0ad46--lead-item--AgRi4')
        except:
            threes = list()
        for three in threes:
            text = ''
            try:
                text = three.find_element_by_css_selector("[data-name='MainGeoHeader']")
                text = text.find_element_by_css_selector('span').text
            except:
                pass
            # print(text)
            if text in cities:
                time.sleep(1)
                btn = three.find_element_by_css_selector("button")
                try:
                    btn.click()
                except:
                    pass
                print(text)
                time.sleep(1)
            if len(browser.window_handles) > 1:
                for x in range(1, len(browser.window_handles)):
                    browser.switch_to.window(browser.window_handles[x])
                    try:
                        browser.find_element_by_xpath('//*[@id="lk-container"]/div/div/div/main/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/button').click()
                        time.sleep(2)
                        browser.find_element_by_xpath('//*[@id="lk-container"]/div/div/div/main/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/button').click()
                        time.sleep(1)
                        browser.save_screenshot('screen.png')
                        doc = open('screen.png', 'rb')
                        bot.send_document('-1001255448500', doc)
                        bot.send_message('-1001255448500', 'Новая заявка куплена')
                        time.sleep(1)
                    except Exception as e:
                        print(e)

                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
                    time.sleep(1)
def initChrome():
    comm = os.system('chrome --remote-debugging-port=3020  --user-data-dir="c:\selenium\AutomationProfile" "https://my.cian.ru/leads"') 
  
def startChrome():
    th1 = Thread(target=initChrome)
    th1.start() 
    button.destroy()
button = Button(window, text="Запустить циан", command=startChrome)
button.grid(column=1, row=0)
button1 = Button(window, text="Запустить бот", command= lambda:  startParsing(counter))
button1.grid(column=1, row=1)
window.mainloop()

# startParsing(counter)     

# eel.start('index.html')