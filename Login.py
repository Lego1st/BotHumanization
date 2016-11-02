import selenium
from selenium import webdriver
# import DataInterac
# from DataInterac import BotDB

def login(drv, account, password) :
    drv.find_element_by_id("email").send_keys(account)
    drv.find_element_by_id("pass").send_keys(password)
    drv.find_element_by_id("loginbutton").click()

# def loginWithProfileName(drv,profile):
#     bot = BotDB.GetProfile(profile)
#     username = bot['username']
#     password = bot['password']
#     login(drv, username, password)