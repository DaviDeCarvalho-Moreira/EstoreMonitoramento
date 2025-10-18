
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


ValoresAvista_Video = {}
ValoresParcelado_Video = {}


        
Url_Video= ['https://www.kabum.com.br/produto/522531/placa-de-video-rtx-4060-asus-dual-8g-evo-oc-nvidia-geforce-8gb-gddr6-g-sync-ray-tracing-90yv0jc7-m0na00?utm_id=22429436057&gad_source=1&gad_campaignid=22429436057&gbraid=0AAAAADx-HyG8PrngVBBi9RDnqiYW2mW9C&gclid=Cj0KCQjw5ubABhDIARIsAHMighZygR44AIhCppkijfQ7ILjdiYEzYF2M26PUOaR5UvA_3jy3jAfC-vQaAoi5EALw_wcB',
                'https://www.pichau.com.br/placa-de-video-gigabyte-geforce-rtx-4060-windforce-oc-8gb-gddr6-128-bit-gv-n4060wf2oc-8gd?srsltid=AfmBOorDk_h7qeH_x631DkN_3Zpnl5h6CqJXngVhqRLZVfqb4YfYl-C-',
                'https://www.terabyteshop.com.br/produto/28514/placa-de-video-asus-dual-nvidia-geforce-rtx-4060-evo-oc-8gb-gddr6-dlss-ray-tracing-dual-rtx4060-o8g-evo?gad_source=1&gad_campaignid=16138806718&gbraid=0AAAAADm8AXRBanWsqn1Dwasps5KAAgLFx&gclid=Cj0KCQjw5ubABhDIARIsAHMigha2GJ1EQKwIhszc7R_c_WxLJHrOAuLX5Z32tI2M1zmS39KoTED7xk8aAif1EALw_wcB'
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
    ValoresAvista_Video[chaveA] = valorA
    ValoresParcelado_Video[chaveP] = ValorP

def IncluirUrl(Urlchave,Urltiny):
     UrlsEncurtada[Urlchave] = Urltiny


for url in Url_Video:

    try:
            
        if 'kabum' in url and 'video' in url:
                
                
            time.sleep(2)
            KabumVideo_Short = EncurtaUrl(url)
            nav(KabumVideo_Short)
            time.sleep(2)
            Pr = KabumScrap()
            IncluirDic('Avis_VideoKabum',Pr[0],'Parc_VideoKabum',Pr[1])
            IncluirUrl('KabumVideo_Short',KabumVideo_Short)
    except:
            IncluirDic('Avis_VideoKabum','erro','Parc_VideoKabum', 'erro')
            pass

    
    try:   
        
        if 'pichau' in url and 'video'  in url:

                
            time.sleep(2)
            PichauVideo_Short = EncurtaUrl(url)
            nav(PichauVideo_Short)
            time.sleep(2)
            Pd = PichauScrap()
            IncluirDic('Avis_VideoPichau',Pd[0],'Parc_VideoPichau',Pd[1])
            IncluirUrl('PichauVideo_Short',PichauVideo_Short)
    except:
       IncluirDic('Avis_VideoPichau','erro','Parc_VideoPichau','erro')
       pass

    
    try:
        
        if 'terabyte' in url and 'video' in url:

            time.sleep(2)
            TerabyteVideo_Short = EncurtaUrl(url)
            nav(TerabyteVideo_Short)
            time.sleep(2)
            Precos = TerabyteScrap()
            IncluirDic('Avis_VideoTerabyte',Precos[0],'Parc_VideoTerabyte',Precos[1])
            IncluirUrl('TerabyteVideo_Short',TerabyteVideo_Short)
    
    except:
        IncluirDic('Avis_VideoTerabyte','erro','Parc_VideoTerabyte','erro')
        pass
        
                 
 
        
# print(f'A vista - {ValoresAvista_Video}')
# print(f'Parcelado - {ValoresParcelado_Video}')
# print(UrlsEncurtada)