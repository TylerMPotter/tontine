from selenium import webdriver
from fake_useragent import UserAgent
from discord_webhook import DiscordWebhook
import time
import os

email = os.environ['EMAIL']
passw = os.environ['PASSW']

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ["GOOGLE_CHROME_BIN"]
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1100,1000")
chrome_options.add_argument("--disable-dev-ahm-usage")
chrome_options.add_argument("--no-sandbox")]
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

url = 'https://tontine.cash/'

while True:

    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)

    chrome_options.add_argument("--user-agent=" + userAgent)

#try:

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
        time.sleep(2)
        info = "Placeholder"
        if key == 'email':
            info = email
        if key == 'passw':
            info = passw

        driver.find_element_by_xpath(data.get(key)).send_keys(info)
    
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[4]/div[2]/div/button/div').click()

    time.sleep(3)

#try:
    #driver.find_elements_by_xpath('//*[@id="__layout"]/div/div/div[5]/div[2]/div[1]/div')
    #ac = ActionChains(driver)
    #ac.move_to_element(elem).move_by_offset(1, 1).click().perform()
    #driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[5]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div/div[2]/button/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div/div[2]/button/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div/div[2]/button/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div/div[2]/button/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div/div[2]/button/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div/div[2]/button/div').click()
    webhook = DiscordWebhook(url=os.environ['STREAKHOOK'], content="You've survived...for today...")
    response = webhook.execute()
#except:
    text = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[1]/div[1]/div[2]/div/div[1]').text
    print("people left: " + text)


    time.sleep(2)

    driver.quit()
#except:
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