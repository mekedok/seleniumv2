from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests

browser = webdriver.Firefox()
time.sleep(2)
browser.get("https://www.instagram.com/")
html =browser.page_source

soup = BeautifulSoup(html,'html.parser')

#//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a              -------- xpath link
time.sleep(5)
gir = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")

gir.click()

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
time.sleep(1)
username.send_keys("leconre09")
password.send_keys("Deldel12")
time.sleep(5)
#xpath giriş--------    //*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div
giris = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
giris.click()
time.sleep(3)

browser.get("https://www.instagram.com/")
time.sleep(2)

anaekran = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
anaekran.click()
time.sleep(2)
anasayfayagecis = browser.find_element_by_css_selector(".glyphsSpriteUser__outline__24__grey_9")
anasayfayagecis.click()
time.sleep(2)
arama = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
arama.send_keys("therock")
arama.click()
time.sleep(1)
rock = browser.find_element_by_css_selector("a.yCE8d:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
rock.click()
time.sleep(2)
takip = browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a")
takip.click()
time.sleep(1)

isimler = browser.find_element_by_class_name('wFPL8 ')
for isimleri in isimler:
         listeler = []
         (isimler.append(listeler))
         print(listeler)

"""
data = soup.find_all('div' , attrs ={'class':'wFPL8'})
text = data.get('content').split()
user = '%s%s%s'%(text[-3],text[-2],text[-1])
print ('User:', user)                                  
"""
