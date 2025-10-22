from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from app.database.db_insert import db_insert
from app.database.data_treatment import price_float
import time
from app.components.constants import KABUM_AVISTA_CSS_SELECTOR,KABUM_PARCELADO_CSS_SELECTOR,PICHAU_AVISTA_CLASS_NAME, PICHAU_PARCELADO_CLASS_NAME,TERABYTE_AVISTA_ID,TERABYTE_PARCELADO_XPATH, KABUM_TITLE_PRODUCT_XPATH,PICHAU_TITLE_PRODUCT_CSS,TERABYTE_TITLE_PRODUCT_XPATH


service = Service(ChromeDriverManager().install())
class ScrapPrices():
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.valores_vista = []
        self.valores_parcelado = {}
       
 
    def kabum_scrap(self,url):
        
        self.driver.get(url)
        product_title = self.driver.find_element(By.XPATH,KABUM_TITLE_PRODUCT_XPATH)
        title = product_title.text
        time.sleep(2)
        
        element_cash = self.driver.find_element(By.CSS_SELECTOR,KABUM_AVISTA_CSS_SELECTOR)
        cash = element_cash.text
        time.sleep(2)
        
        element_installment = self.driver.find_element(By.CSS_SELECTOR,KABUM_PARCELADO_CSS_SELECTOR)
        installment = element_installment.text
        
        float_cash = price_float(cash)
        float_installment = price_float(installment)
        
        db_insert(float_cash,float_installment,title,url,store_id=1)
        
        return cash,installment,title
    
    def pichau_scrap(self,url):
       
        self.driver.get(url)
        product_title = self.driver.find_element(By.CSS_SELECTOR,PICHAU_TITLE_PRODUCT_CSS)
        title = product_title.text
        element_cash = self.driver.find_element(By.CLASS_NAME, PICHAU_AVISTA_CLASS_NAME)
        cash = element_cash.text
        element_installment = self.driver.find_element(By.CLASS_NAME, PICHAU_PARCELADO_CLASS_NAME)
        installment = element_installment.text
        
        float_cash = price_float(cash)
        float_installment = price_float(installment)
        
        db_insert(float_cash,float_installment,title,url,store_id=2)
        
        return cash,installment,title
    
    def terabyte_scrap(self,url):
        
        self.driver.get(url)
        
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="bannerPop"]/div/div/button/span').click() 
            time.sleep(5)
        except:
            pass
        
        product_title = self.driver.find_element(By.XPATH,TERABYTE_TITLE_PRODUCT_XPATH)
        title = product_title.text
        time.sleep(2)
        element_cash = self.driver.find_element(By.ID,TERABYTE_AVISTA_ID)
        cash = element_cash.text
        time.sleep(2)
        
        try:
            element_installment = self.driver.find_element(By.XPATH,TERABYTE_PARCELADO_XPATH)
            installment = element_installment.text
        except:
            element_installment = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div/div[3]/div/div/div[11]/div[2]/div[3]/div[1]/p/span[1]')
            installment = element_installment.text
            
        float_cash = price_float(cash)
        float_installment = price_float(installment)
            
        db_insert(float_cash,float_installment,title,url,store_id=3)
            
        return float_cash, float_installment,title
    