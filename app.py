from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep


def iniciar_driver():

    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito', '--disable-notifications']
    for argument in arguments:
        chrome_options.add_argument(argument)


    # Inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options
    )

    return driver

driver = iniciar_driver()
# Passo a passo para criar um bot de postagem no Facebook

# 1 - Entrar no site facebook.com
driver.get('https://www.facebook.com/')
sleep(7)

# 2 - Encontrar o campo onde digita o e-mail para o login
campo_email = driver.find_element(By.XPATH, "//input[@id='email']")
sleep(5)
# 3 - Digitar o e-mail
campo_email.send_keys("seuemail@email.com")
sleep(5)

# 4 - Encontrar o campo onde digita a senha para o login
campo_senha = driver.find_element(By.XPATH, "//input[@id='pass']")
sleep(5)
# 5 - Digitar a senha
campo_senha.send_keys("suasenha")
sleep(5)

# 6 - Encontrar o botão "Entrar"
botao_entrar = driver.find_element(By.XPATH, "//button[@name='login']")
sleep(5)

# 7 - Clicar no botão "Entrar"
botao_entrar.click()
sleep(5)

# 8 - Encontrar o botão com a logo do Facebook
botao_logo = driver.find_element(By.XPATH, "//a[@aria-label='Facebook']")
sleep(5)

# 9 - Clicar no botão com a logo do facebook
botao_logo.click()
sleep(5)

# 10 - Encontrar o campo "No que você está pensando ..."
campo_no_que_esta_pensando = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
sleep(5)

# 11 - Clicar no campo "No que você está pensando..."
campo_no_que_esta_pensando.click()
sleep(5)

# 12 -  Encontrar o campo para digitar o que estou pensando
campo_digitar_pensamento = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
sleep(5)

# 13 - Clicar no campo para digitar o que estou pensando
campo_digitar_pensamento.click()
sleep(5)

# 14 - Digitar no campo "Digitar o que você está pensando"
campo_digitar_pensamento.send_keys("Digite aqui o que você está pensando")
sleep(5)

# 15 - Encontrar o botão "Publicar"
botao_publicar = driver.find_element(By.XPATH, "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
sleep(5)

# 16 - Clicar no botão "Publicar"
botao_publicar.click()
sleep(5)
