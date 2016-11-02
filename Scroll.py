import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import LikePostOnNewsfeed

#truyền list cmt và drv vào để cmt và like trong khi scrool
def Scroll(drv,commentList) :
    random.seed()
    scroll_times = random.randint(5,10)
    while (scroll_times > 0):
        sleepTime = random.randint(10,20)
        time.sleep(sleepTime)
        action = ActionChains(drv)
        action.send_keys('j')
        action.perform()
        LikePostOnNewsfeed.Like(drv)
        LikePostOnNewsfeed.Comment(drv,commentList)        
        scroll_times = scroll_times - 1            
        
