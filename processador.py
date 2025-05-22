
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
import time

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

ValoresAvista_Processador = {}
ValoresParcelado_Processador = {}

Url_Processador = ['https://www.kabum.com.br/produto/320798/processador-amd-ryzen-5-5600-3-5ghz-4-4ghz-max-turbo-cache-35mb-am4-sem-video-100-100000927box?utm_id=21733851091&gad_source=1&gclid=CjwKCAiArva5BhBiEiwA-oTnXTUlQCiyOsfvKH-uxWrVPrlAafIlVE9lykvxbw-JTCzBH4lt4leWgRoCBjcQAvD_BwE',
            'https://www.pichau.com.br/processador-amd-ryzen-5-5600-6-core-12-threads-3-5ghz-4-4ghz-turbo-cache-35mb-am4-100-100000927box',
            'https://www.terabyteshop.com.br/produto/20788/processador-amd-ryzen-5-5600-35ghz-44ghz-turbo-6-cores-12-threads-cooler-wraith-stealth-am4-100-100000927box?gad_source=1&gclid=CjwKCAiArva5BhBiEiwA-oTnXWyzSupXeHv_uLTF0ASzt8HiyX5KoHNhvKW4_xahbsWhpaaCO7F73xoCiXoQAvD_BwE',
         ] 


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
    ValoresAvista_Processador[chaveA] = valorA
    ValoresParcelado_Processador[chaveP] = ValorP
    

def IncluirUrl(Urlchave,Urltiny):
     UrlsEncurtada[Urlchave] = Urltiny
     
     


for url in Url_Processador:

    try:
            
         if 'kabum' in url and 'processador':

                KabumProcessador_Short = EncurtaUrl(url)
                nav(KabumProcessador_Short)
                time.sleep(2)
                Precos = KabumScrap()
                IncluirDic('Avis_ProcessadorKabum',Precos[0],'Parc_ProcessadorKabum',Precos[1])
                IncluirUrl('KabumProcessador_Short',KabumProcessador_Short)
    except:
            IncluirDic('Avis_ProcessadorKabum','erro','Parc_ProcessadorKabum','erro')
            pass
        

        
    try:    
            
        if 'pichau' in url and 'processador':
                
            time.sleep(2)
            PichauProcessador_Short = EncurtaUrl(url)
            nav(PichauProcessador_Short)
            time.sleep(2)
            Precos = PichauScrap()
            IncluirDic('Avis_ProcessadorPichau',Precos[0],'Parc_ProcessadorPichau',Precos[1])
            IncluirUrl('PicPichauProcessador_Short',PichauProcessador_Short)
    except:
            IncluirDic('Avis_ProcessadorPichau','erro','Parc_ProcessadorPichau','erro')
            pass      

    try:
        if 'terabyte' in url and 'processador':

            time.sleep(2)
            TerabyteProcessador_Short = EncurtaUrl(url)
            nav(TerabyteProcessador_Short)
            time.sleep(2)
            Precos = TerabyteScrap()
            IncluirDic('Avis_ProcessadorTerabyte',Precos[0],'Parc_ProcessadorTerabyte',Precos[1])
            IncluirUrl('TerabyteProcessador_Short',TerabyteProcessador_Short)
    except:
            IncluirDic('Avis_ProcessadorTerabyte','erro','Parc_ProcessadorTerabyte','erro')
            pass
            
            
# print(f'A vista - {ValoresAvista_Processador}')
# print(f'Parcelado - {ValoresParcelado_Processador}')
# print(UrlsEncurtada)