
import getpass
import time

import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

matricula = input('Insira sua matrícula: ' )
senha = getpass.getpass('Insira sua senha: ')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get('https://portalth.algarnet.com.br/Algar/Produtos/SAAA/Principal2.aspx?amb_selecionado=0&abrir_nova_janela=N&eh_mdesigner=N&nome_portal=634C3649335370516551633D')
search = driver.find_element_by_id('txtLogin')
time.sleep(1)
search.send_keys(matricula)
search2 = driver.find_element_by_id('txtSenha')
time.sleep(1)
search2.send_keys(senha)
search2.send_keys(Keys.RETURN)
time.sleep(1)


time.sleep(1)
pg.moveTo(93, 477, 0)
pg.click(93, 477)
time.sleep(1)
pg.moveTo(498, 343, 0)
pg.click(498, 343)
time.sleep(1)
pg.moveTo(636, 475, 0)
pg.click(636, 475)
time.sleep(5)








