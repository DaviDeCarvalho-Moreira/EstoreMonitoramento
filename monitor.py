
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

ValoresAvista_Monitor = {}
ValoresParcelado_Monitor = {}

Url_I7 = ['https://www.kabum.com.br/produto/614879/monitor-gamer-lg-ultragear-24-fhd-ips-180hz-1ms-gtg-hdr10-displayport-e-hdmi-amd-freesync-nvidia-g-sync-preto-24gs60f-b?utm_id=22422865812&gad_source=1&gad_campaignid=22422865812&gbraid=0AAAAADx-HyFruzmyFQhTHMulgqvJaaaEy&gclid=Cj0KCQjw5ubABhDIARIsAHMighbWtbf_Yysd14OFnO6-TmZYoIzDtq5q9R93Gv54LupWaylSKYA9pXMaAh3JEALw_wcB',
            'https://www.pichau.com.br/monitor-gamer-redragon-azur-23-8-pol-ips-fhd-1ms-165hz-freesync-hdmi-dp-gm24x5ips?gad_source=1&gad_campaignid=17417836924&gbraid=0AAAAADvAK936rdnrt_cPZBlBs4rbTD4s4&gclid=Cj0KCQjw5ubABhDIARIsAHMighbFQtALie9oDUsmWCxsGxFtPK-GOZesu9qX778MJ0DTlBDpO1IrcEEaAqRWEALw_wcB',
            'https://www.terabyteshop.com.br/produto/31035/monitor-gamer-lg-ultragear-24-pol-full-hd-180hz-ips-1ms-freesyncg-sync-hdmidp-24gs60f-bawzm?gad_source=1&gad_campaignid=16147136125&gbraid=0AAAAADm8AXTUPH8-DA87HxdDq0weaKigr&gclid=Cj0KCQjw5ubABhDIARIsAHMighZL82mivN3bG_mX2qoG03t9fU_qYi14GyFvkjSkt_wxt_8JAImCCy4aAj2YEALw_wcB',
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
    ValoresAvista_Monitor[chaveA] = valorA
    ValoresParcelado_Monitor[chaveP] = ValorP

def IncluirUrl(Urlchave,Urltiny):
     UrlsEncurtada[Urlchave] = Urltiny


for url in Url_I7:

    try:
        if 'kabum' in url and 'monitor':

            KabumMonitor_Short = EncurtaUrl(url)
            nav(KabumMonitor_Short)
            time.sleep(2)
            Precos = KabumScrap()
            IncluirDic('Avis_MonitorKabum',Precos[0],'Parc_MonitorKabum',Precos[1])
            IncluirUrl('KabumMonitor_Short',KabumMonitor_Short)
    except:
        IncluirDic('Avis_MonitorKabum','erro','Parc_MonitorKabum','erro')

    try:
        if 'pichau' in url and 'monitor':

                time.sleep(2)
                PichauMonitor_Short = EncurtaUrl(url)
                nav(PichauMonitor_Short)
                time.sleep(2)
                Precos = PichauScrap()
                IncluirDic('Avis_MonitorPichau',Precos[0],'Parc_MonitorPichau',Precos[1])
                IncluirUrl('PichauMonitor_Short',PichauMonitor_Short)      
    except:
        IncluirDic('Avis_MonitorPichau','erro','Parc_MonitorPichau','erro')

    try:
                time.sleep(2)
                TerabyteMonitor_Short = EncurtaUrl(url)
                nav(TerabyteMonitor_Short)
                time.sleep(2)
                Precos = TerabyteScrap()
                IncluirDic('Avis_MonitorTerabyte',Precos[0],'Parc_MonitorTerabyte',Precos[1])
                IncluirUrl('TerabyteMonitor_Short',TerabyteMonitor_Short)
    except:
          IncluirDic('Avis_MonitorTerabyte','erro','Parc_MonitorTerabyte','erro')
         

            
            
# print(f'A vista - {ValoresAvista_Monitor}')
# print(f'Parcelado - {ValoresParcelado_Monitor}')
# print(UrlsEncurtada)