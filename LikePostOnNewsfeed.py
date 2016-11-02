from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

#hàm để check xem có hiện lên cửa sổ xác nhận like bằng bàn phím
def ConfirmLike(drv):
    try:
        confirmButton = drv.find_element_by_class("layerConfirm")
        time.sleep(2)
        confirmButton.click()
    except:
        pass

#hàm để like
def Like(drv):
    random.seed()
    try:
        if (1 == random.randint(0,1)):
            action = ActionChains(drv)
            action.send_keys('l')
            action.perform()
            ConfirmLike(drv)
    except:
        pass

#hàm để cmt với cmtList đc truyền vào
#cần làm thêm thủ tục thoát ra khỏi ô cmt sau khi cmt
def Comment(drv, commentList):
    random.seed()
    try:
        if(1 == random.randint(1,4)):
            action = ActionChains(drv)
            action.send_keys('c')
            action.perform()
            time.sleep(2)
            action = ActionChains(drv)
            action.send_keys(random.choice(commentList))
            action.perform()
            time.sleep(0.5)
            action = ActionChains(drv)
            action.send_keys(Keys.ENTER)
            action.perform()
    except:
        pass