from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
from winotify import Notification, audio

import json
import time
from random import randint


def notify():
    toast = Notification(app_id="ECE 15",
                         title="Vote",
                         msg="At least 60 students have voted",
                         duration="long",
                         icon=r"C:\Users\super\Desktop\Giovanni\Programacion\Resources\CheckmarkIcon.webp")

    toast.set_audio(audio.Mail, loop=False)
    toast.show()


def getVoteCount():
    vote_element = driver.find_element(By.XPATH, "//li[@class='MuiListItem-root MuiListItem-gutters']/div[@class='MuiListItemText-root MuiListItemText-multiline']/p[@class='MuiTypography-root MuiListItemText-secondary MuiTypography-body2 MuiTypography-colorTextSecondary MuiTypography-displayBlock']")
    vote_string = vote_element.text
    print(vote_string)

    nList = [int(s) for s in vote_string.split(" ") if s.isdigit()]

    if nList:
        return nList[0]
    else:
        return -1


def vote(n):

    if n == 1:
        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedOutlined MuiButtonGroup-groupedOutlinedHorizontal MuiButtonGroup-groupedOutlined']/span[@class='MuiButton-label']").click()
        time.sleep(2)
    elif n == 2:
        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedOutlined MuiButtonGroup-groupedOutlinedHorizontal MuiButtonGroup-groupedOutlined']/span[contains(text(), 'B')]").send_keys(chr(10))
        time.sleep(2)
    elif n == 3:
        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedOutlined MuiButtonGroup-groupedOutlinedHorizontal MuiButtonGroup-groupedOutlined']/span[contains(text(), 'C')]").click()
        time.sleep(2)
    elif n == 4:
        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedOutlined MuiButtonGroup-groupedOutlinedHorizontal MuiButtonGroup-groupedOutlined']/span[contains(text(), 'C')]").send_keys('\n')
        time.sleep(2)
    elif n == 5:
        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButtonGroup-grouped MuiButtonGroup-groupedHorizontal MuiButtonGroup-groupedOutlined MuiButtonGroup-groupedOutlinedHorizontal MuiButtonGroup-groupedOutlined']/span[contains(text(), 'E')]").click()


with open('info.json') as json_file:
    data = json.load(json_file)

'''
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
'''

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

link = "https://webclicker.web.app/login/"
driver.get(link)

element = driver.find_element(By.XPATH, "//input[@type='email']")
element.send_keys(data['email'])
time.sleep(2)

element = driver.find_element(By.XPATH, "//input[@type='password']")
element.send_keys(data['password'])
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined jss2 MuiButton-fullWidth']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//div[@class='MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button']").click()

while True:
    votes = getVoteCount()
    print(votes)

    if votes > 60:
        notify()
        temp = votes

        while True:
            votes = getVoteCount()
            print(votes)

            if votes < temp:
                break

            time.sleep(10)
    else:
        time.sleep(10)
