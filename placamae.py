
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

ValoresAvista_Mae = {}
ValoresParcelado_Mae = {}



Url_Mae= ['https://www.kabum.com.br/produto/113870/placa-mae-asus-prime-b550m-a-amd-am4-matx-ddr4-preto-90mb14i0-m0eay0?utm_id=22429436060&gad_source=1&gad_campaignid=22429436060&gbraid=0AAAAADx-HyFmKTafhCoIcMaBp0h2lJNVS&gclid=Cj0KCQjw5ubABhDIARIsAHMighayIeWig2RS9eau94_QXmHN8eyYnl7SiK3hm39BKs3DhJ2Ld1FEgmsaArqyEALw_wcB',
          'https://www.pichau.com.br/placa-mae-msi-b550m-a-pro-ddr4-socket-am4-chipset-amd-b550?gad_source=1&gad_campaignid=22184670223&gbraid=0AAAAADvAK92f_JYuNOcoqEaI4BG8sG8K4&gclid=Cj0KCQjw5ubABhDIARIsAHMighYalBVFvPHgVGArmXEIeer1xqf-UYzhHAlc9t01wxJR5-yE6J6Kw0QaAjqkEALw_wcB',
          'https://www.terabyteshop.com.br/produto/25499/placa-mae-biostar-b550mxc-pro-chipset-b550-amd-am4-matx-ddr4']


UrlsEncurtada = {}

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


def IncluirDic(chaveA,valorA,chaveP,ValorP):
    ValoresAvista_Mae[chaveA] = valorA
    ValoresParcelado_Mae[chaveP] = ValorP

def IncluirUrl(Urlchave,Urltiny):
     UrlsEncurtada[Urlchave] = Urltiny



for url in Url_Mae:

    try:
        if 'kabum' in url:
            KabumMae_Short = EncurtaUrl(url)
            nav(KabumMae_Short)
            time.sleep(2)
            Precos = KabumScrap()
            IncluirDic('Avis_MaeKabum', Precos[0], 'Parc_MaeKabum', Precos[1])
            IncluirUrl('KabumMae_Short', KabumMae_Short)
    except:
        IncluirDic('Avis_MaeKabum', 'erro', 'Parc_MaeKabum', 'erro')
        pass
        

    try:    
        if 'pichau' in url:
            time.sleep(2)
            PichauMae_Short = EncurtaUrl(url)
            nav(PichauMae_Short)
            time.sleep(2)
            Precos = PichauScrap()
            IncluirDic('Avis_MaePichau',Precos[0],'Parc_MaePichau',Precos[1])
            IncluirUrl('PichauMae_Short',PichauMae_Short)
    except:
        IncluirDic('Avis_MaePichau','erro','Parc_MaePichau','erro')
        pass   

    try:
        if 'terabyte' in url:
            time.sleep(2)
            TerabyteMae_Short = EncurtaUrl(url)
            nav(TerabyteMae_Short)
            time.sleep(2)
            Precos = TerabyteScrap()
            IncluirDic('Avis_MaeTerabyte',Precos[0],'Parc_MaeTerabyte',Precos[1])
            IncluirUrl('TerabyteMae_Short',TerabyteMae_Short)
    except:
        IncluirDic('Avis_MaeTerabyte','erro','Parc_MaeTerabyte','erro')
        pass
    



# print(f'A vista - {ValoresAvista_Mae}')
# print(f'Parcelado - {ValoresParcelado_Mae}')
# print(UrlsEncurtada)
