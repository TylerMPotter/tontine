from selenium import webdriver
from discord_webhook import DiscordWebhook
import time
import os

email = os.environ['EMAIL']
passw = os.environ['PASSW']

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ["GOOGLE_CHROME_BIN"]
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-ahm-usage")
chrome_options.add_argument("--no-sandbox")

url = 'https://tontine.cash/'

while True:

    try:

        driver = webdriver.Chrome(executable_path=os.environ["CHROMEDRIVER_PATH"], chrome_options=chrome_options)

        driver.get(url)

        data = {
            'email': '//*[@id="__layout"]/div/div/div[4]/div[2]/div/input[1]',
            'passw': '//*[@id="__layout"]/div/div/div[4]/div[2]/div/input[2]',
        }

        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[1]/div[2]/button/div').click()

        time.sleep(2)

        for key in data.keys():
            info = "Placeholder"
            if key == 'email':
                info = email
            if key == 'passw':
                info = passw

            driver.find_element_by_xpath(data.get(key)).send_keys(info)

        driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[4]/div[2]/div/button/div').click()

        text = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[1]/div[1]/div[2]/div/div[1]').text

        print("people left: " + text)

        time.sleep(2)

        driver.quit()
    except:
        webhook = DiscordWebhook(url=os.environ['LOGINHOOK'], content="something is broken")
        response = webhook.execute()
        driver.quit()
'''
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
///////////////WHO AM I/////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
///////////////////////***//*///////*///*//*///////*/******/*///////////////////
///////////////////*######(/////////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*///////######/*///////*######//////////////////////
///////////////////*######(/*//////*######/////////*######//////////////////////
////////////////////***//*//////////******/////////////***//////////////////////
////////////////////****////////////*****///////////**/***//////////////////////
////////////////*//*#######*////*//*#######*//////*/######(/////////////////////
/////////////////**########////////########*//////*########*////////////////////
/////////////////////#####*/*////////#####*/////////(#####**////////////////////
/////////////////////**//////////////*//*///////////////*/**////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////WHO AM I NOT///////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
'''