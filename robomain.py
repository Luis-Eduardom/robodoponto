import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def bater_ponto():
    matricula = '0336126'
    senha = 'Profano123@'

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get(
        'https://portalth.algarnet.com.br/Algar/Produtos/SAAA/Principal2.aspx?amb_selecionado=0&abrir_nova_janela=N'
        '&eh_mdesigner=N&nome_portal=634C3649335370516551633D')

    if driver.get('https://portalth.algarnet.com.br/Algar/Produtos/SAAA/Principal2.aspx?amb_selecionado=0&abrir_nova_janela=N'
        '&eh_mdesigner=N&nome_portal=634C3649335370516551633D')
        search = driver.find_element_by_id('txtLogin')

    time.sleep(1)
    search.send_keys(matricula)

    search2 = driver.find_element_by_id('txtSenha')
    time.sleep(1)
    search2.send_keys(senha)
    search2.send_keys(Keys.RETURN)
    driver.get('https://portalth.algarnet.com.br/Algar/ASS_MDADOS_CONTROLEJORNADA.aspx')
    time.sleep(2)

    search3 = driver.find_element_by_id('imagem0')
    search3.click()
    time.sleep(5)
    driver.get('https://portalth.algarnet.com.br/WebPonto/just_user/IncluirMarcacaoOnLine.asp')

    search4 = driver.find_element_by_id('Button1')
    search4.click()
    driver.quit()


schedule.every().monday.at('06:00').do(bater_ponto)
schedule.every().monday.at('12:00').do(bater_ponto)
schedule.every().monday.at('13:30').do(bater_ponto)
schedule.every().monday.at('15:00').do(bater_ponto)
schedule.every().wednesday.at('06:00').do(bater_ponto)
schedule.every().wednesday.at('12:00').do(bater_ponto)
schedule.every().wednesday.at('13:33').do(bater_ponto)
schedule.every().wednesday.at('15:00').do(bater_ponto)
schedule.every().thursday.at('05:00').do(bater_ponto)
schedule.every().thursday.at('11:30').do(bater_ponto)
schedule.every().thursday.at('12:30').do(bater_ponto)
schedule.every().thursday.at('14:00').do(bater_ponto)
schedule.every().friday.at('05:00').do(bater_ponto)
schedule.every().friday.at('11:30').do(bater_ponto)
schedule.every().friday.at('12:30').do(bater_ponto)
schedule.every().friday.at('14:00').do(bater_ponto)

while 1:
    schedule.run_pending()
    time.sleep(1)
