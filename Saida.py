import processador
import placaVideo
import monitor
import placamae

from selenium import webdriver
import pyshorteners 
import pandas as pd 
from selenium.webdriver.common.by import By
import locale
import time
import webbrowser as wb
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import openpyxl
from types import MappingProxyType

driver = webdriver.Chrome()
Action = ActionChains(driver)

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def JuntarDic (dic1,dic2):
    all = {**dic1,**dic2}
    return all

def listaAvis(ident1,ident2):
    for an in Analise:
        Analise[an] = float(Analise[an])
        if ident1 in an:
            if Analise[an] < ident2:
                ident2 = Analise[an]
                key = an
                
    ListaAvista[key] = ident2
        
    
def listaParc(ident1,ident2):
    for an in Analise:
        Analise[an] = float(Analise[an])
        if ident1 in an:
              if Analise[an] < ident2:
                ident2 = Analise[an]
                key = an
    
    
    ListaParcelado[key] = ident2

def SaidaAvista(hard,terabyte,pichau,kabum):
    for item in ListaAvista:
        if (hard) in item and (terabyte) in item:
            saida = f'{hard.upper()} - {terabyte} com o  valor de R$ {ListaAvista[item]}'
        elif(hard) in item and (pichau) in item:
            saida = f'{hard.upper()} - {pichau} com o  valor de R$ {ListaAvista[item]}'
        elif(hard) in item and (kabum) in item:
            saida = f'{hard.upper()} - {kabum} com o  valor de R$ {ListaAvista[item]}'
    
    return saida


def SaidaParcelado(hard,terabyte,pichau,kabum):
    for item in ListaParcelado:
        if (hard) in item and (terabyte) in item:
            saida = f'{hard.upper()} - {terabyte} com o  valor de R$ {ListaParcelado[item]}'
        elif(hard) in item and (pichau) in item:
            saida = f'{hard.upper()} - {pichau} com o  valor de R$ {ListaParcelado[item]}'
        elif(hard) in item and (kabum) in item:
            saida = f'{hard.upper()} - {kabum} com o  valor de R$ {ListaParcelado[item]}'
    
    return saida

def AddPlanilha(hard,row,col):
    if hard in chave:
        detalhamento.loc[[row],[col]] = Analise[chave]


All = {}
Analise = {}
ListaAvista = {}
ListaParcelado = {}

url = {**processador.UrlsEncurtada,**placaVideo.UrlsEncurtada,**monitor.UrlsEncurtada}
print(url)

Processador_A = processador.ValoresAvista_Processador 
Processador_P = processador.ValoresParcelado_Processador

placaVideo_A = placaVideo.ValoresAvista_Video
placaVideo_P = placaVideo.ValoresParcelado_Video

monitor_A = monitor.ValoresAvista_Monitor
monitor_P = monitor.ValoresParcelado_Monitor

Mae_A = placamae.ValoresAvista_Mae
Mae_P = placamae.ValoresParcelado_Mae

All = {**Processador_A,**Processador_P,**placaVideo_A,**placaVideo_P,**monitor_A,**monitor_P,**Mae_A,**Mae_P}
VisaoGeral = MappingProxyType(All)

Analise = {}


print(All)
print('---------------------------------------------------------')
for valor in All:
    if 'R$' and '.' and ',' in All[valor]:
        All[valor] = All[valor].replace('R$','').replace('.','').replace(',','.').strip()
        Analise[valor] = All[valor]
    else:
        All[valor] = "OutDefault"

print(All)     
print('-------------------------------------------------------------------------------------------------------')
 
ProcessadorAvista = 1000000.00
videoAvista = 10000000.00
monitorAvista = 1000000.00
maeAvista = 1000000.00

ProcessadorParcelado = 1000000.00
videoParcelado = 10000000.00
monitorParcelado = 1000000.00
maeParcelado = 1000000.00


listaAvis('Avis_Processador',ProcessadorAvista)
listaAvis('Avis_Video',videoAvista)
listaAvis('Avis_Monitor',monitorAvista)
listaAvis('Avis_Mae',maeAvista)

listaParc('Parc_Processador',ProcessadorParcelado)
listaParc('Parc_Video',videoParcelado)
listaParc('Parc_Monitor',monitorParcelado)
listaParc('Parc_Mae',maeParcelado)


davi  = 'davicarvalho425@gmail.com'
senha = 'aufd ohmd ikku vxhv'

detalhamento = pd.read_excel('DETALHAMENTO.xlsx')
detalhamento = detalhamento.set_index('HARD')

for chave in Analise:
    if 'Avis' in chave and 'Kabum' in chave:
        AddPlanilha('Processador','A_KABUM','PROCESSADOR')
        AddPlanilha('Video','A_KABUM','PLACA_VIDEO')
        AddPlanilha('Mae','A_KABUM','PLACA_MAE')
        AddPlanilha('Monitor','A_KABUM','MONITOR')

    elif 'Avis' in chave and 'Pichau' in chave:
        AddPlanilha('Processador','A_PICHAU','PROCESSADOR')
        AddPlanilha('Video','A_PICHAU','PLACA_VIDEO')
        AddPlanilha('Mae','A_PICHAU','PLACA_MAE')
        AddPlanilha('Monitor','A_PICHAU','MONITOR')
    elif 'Avis' in chave and 'Terabyte' in chave:
        AddPlanilha('Processador','A_TERABYTE','PROCESSADOR')
        AddPlanilha('Video','A_TERABYTE','PLACA_VIDEO')
        AddPlanilha('Mae','A_TERABYTE','PLACA_MAE')
        AddPlanilha('Monitor','A_TERABYTE','MONITOR')

for chave in Analise:
    if 'Parc' in chave and 'Kabum' in chave:
        AddPlanilha('Processador','P_KABUM','PROCESSADOR')
        AddPlanilha('Video','P_KABUM','PLACA_VIDEO')
        AddPlanilha('Mae','P_KABUM','PLACA_MAE')
        AddPlanilha('Monitor','P_KABUM','MONITOR')

    elif 'Parc' in chave and 'Pichau' in chave:
        AddPlanilha('Processador','P_PICHAU','PROCESSADOR')
        AddPlanilha('Video','P_PICHAU','PLACA_VIDEO')
        AddPlanilha('Mae','P_PICHAU','PLACA_MAE')
        AddPlanilha('Monitor','P_PICHAU','MONITOR')

    elif 'Parc' in chave and 'Terabyte' in chave:
        AddPlanilha('Processador','P_TERABYTE','PROCESSADOR')
        AddPlanilha('Video','P_TERABYTE','PLACA_VIDEO')
        AddPlanilha('Mae','P_TERABYTE','PLACA_MAE')
        AddPlanilha('Monitor','P_TERABYTE','MONITOR')
     

detalhamento.to_excel('DETALHAMENTO.xlsx')
DETALHAMENTO = openpyxl.load_workbook('DETALHAMENTO.xlsx')
aba = DETALHAMENTO.active

for column_cells in aba.columns:
    max_length = 0
    column = column_cells[0].column_letter  
    for cell in column_cells:
        try:
            if cell.value:
        
                max_length = max(max_length, len(str(cell.value)))
        except:
            pass
    
    adjusted_width = max_length + 2  
    aba.column_dimensions[column].width = adjusted_width



DETALHAMENTO.save('DETALHAMENTO.xlsx')



msg = MIMEMultipart()
msg['From'] = davi  
msg['To'] = davi  
msg['Subject'] = "RELACAO DE PRECOS PARA PC"


body = (
    "MELHORES VALORES AVISTA\n"
    "\n"
    f"{SaidaAvista('Processador','Terabyte','Pichau','Kabum')}\n"
    f"{SaidaAvista('Video','Terabyte','Pichau','Kabum')}\n"
    f"{SaidaAvista('Monitor','Terabyte','Pichau','Kabum')}\n"
    f"{SaidaAvista('Mae','Terabyte','Pichau','Kabum')}\n"
    "\n\n"
    "MELHORES VALORES PARCELADO\n"
    "\n\n"
    f"{SaidaParcelado('Processador','Terabyte','Pichau','Kabum')}\n"
    f"{SaidaParcelado('Video','Terabyte','Pichau','Kabum')}\n"
    f"{SaidaParcelado('Monitor','Terabyte','Pichau','Kabum')}\n"
    f"{SaidaParcelado('Mae','Terabyte','Pichau','Kabum')}\n"
)


msg.attach(MIMEText(body, 'plain'))


filename = "DETALHAMENTO.xlsx"  
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())


encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


msg.attach(part)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    connection.login(user=davi, password=senha)
    connection.sendmail(from_addr=davi,
                        to_addrs=davi,
                        msg=msg.as_string())  


