from selenium import webdriver
import pyshorteners 
import pandas as pd 
from selenium.webdriver.common.by import By
import locale
import time
import webbrowser as wb
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
Action = ActionChains(driver)

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')




def nav(adress):
    driver.get(adress)


def EncurtaUrl(Url):
    s = pyshorteners.Shortener()
    short = s.tinyurl.short(Url)
    return short 


def KabumScrap ():
    ElementsB = driver.find_element(By.CLASS_NAME,'regularPrice')
    Parcelado = ElementsB.text
    Avista = driver.find_element(By.TAG_NAME,'h4').text
    return Avista , Parcelado


def PichauScrap ():
   elementsAvista = driver.find_element(By.CSS_SELECTOR,'.mui-1q2ojdg-price_vista') 
   elementsParcelado = driver.find_element(By.CSS_SELECTOR,'.mui-7ie9un-price_total')
   Avista = elementsAvista.text
   Parcelado = elementsParcelado.text
   return Avista , Parcelado


def TerabyteScrap ():
     
    try:
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="bannerPop"]/div/div/button/span').click()
        time.sleep(2)
    except:
        pass
    
    time.sleep(2)
    AVista = driver.find_element(By.ID,'valVista').text
    des = driver.find_element(By.CLASS_NAME,'valorPromRelac').text
    integral = driver.find_element(By.TAG_NAME,'del').text
    integral = float(integral.replace('R$','').replace(".","").replace(",","").strip()) /100
    des = float(des.replace("%","").strip()) /100

    Parcelado =  integral - (integral * des) + 10
    Parcelado = locale.format_string("%.2f",Parcelado,grouping = True)
    Parcelado = 'R$ ' + str(Parcelado)
    
    return  AVista ,Parcelado




