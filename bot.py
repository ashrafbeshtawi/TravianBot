from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def add_comment(driver):

    ## clicking add comment button
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="video-content-metadata"]/div[2]/div[2]/a[1]')
    elem.click()
    ## clicking show form  button
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="tabComments"]/div/div[8]/a[3]')
    elem.click()


    ##adding value to the input
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="post_user"]')
    elem.send_keys("Testing some ")

    elem=driver.find_element_by_xpath('//*[@id="post_text"]')
    elem.send_keys("who wants to suck my cock")

    ## sending comment
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="post"]/div[3]/div/button')
    elem.click()

    ## going to next video
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="video_28079007"]/div[1]/div/a')
    elem.click()
    
    ## close ad
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="ad_3959997"]/div/div[1]/div')
    elem.click()



option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

driver = webdriver.Chrome("C:/chrome_driver/chromedriver.exe",chrome_options=option)
driver.get('https://www.xnxx.com/video-whe6rc0/bangbros_-_pretty_pawg_getting_fucked_in_pov')
## clicking up 18
time.sleep(3)
elem=driver.find_element_by_xpath('//*[@id="disclaimer-content"]/button')
elem.click()
for i in range(5):
    add_comment(driver)
    time.sleep(10)
