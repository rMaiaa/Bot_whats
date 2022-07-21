from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(50)

contatos=['ENTER THE GROUP NAME AND CONTACT NUMBER OR DESIRED CONTACT NAME']
mensagem = 'INSERT YOUR MESSENGE'

#função responsável para fazer a busca dos contatos
def buscar_contato(contato):
    campo_pesquisa=driver.find_element(by=By.XPATH, value='//div[contains(@class,"YOUR_ID_SEARCH_TEXT_BOX")]') #FORMATO NOVO DO SELENIUM 4.3
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#função responsável para fazer o envio da mensagem
def enviarmensagem(mensagem):
    campo_mensagem=driver.find_element(by=By.XPATH, value='//div[contains(@class, "YOUR_ID")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)
    
for contato in contatos:
    buscar_contato(contato)
    enviarmensagem(mensagem)

time.sleep(20) #fechará o navegador utilizado em 20 segundos
pyautogui.hotkey('ctrl', 'w') 
