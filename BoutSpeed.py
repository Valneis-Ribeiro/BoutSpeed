from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore
from random import randint

# Bot-Votação
resultado = {'Paulo': 0}

while True:
    print(Fore.CYAN,'Acessando painel de votação....')

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    eleitor = webdriver.Chrome(options=options)

    eleitor.get('https://docs.google.com/forms/d/e/1FAIpQLSfBz4thY6pNLBekL7d0cCNMRF8KNatZwfAXNmqliCv-4CF5LA/viewform')

    # Votação garota CDC
    votar = eleitor.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    votar.click()

    # proxima votação
    proximo = eleitor.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    proximo.click()

    # Votação garoto CDC
    votar = eleitor.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    votar.click()

    # proxima votação
    proximo = eleitor.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
    proximo.click()

    # Mister Simpatia
    votar = eleitor.find_element(By.XPATH, '//*[@id="i5"]/div[3]/div')
    votar.click()

    # proxima votação
    proximo = eleitor.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    proximo.click()

    # Miss Simpatia
    votar = eleitor.find_element(By.XPATH, '//*[@id="i17"]/div[3]/div')
    votar.click()

    # Enviar formulario
    proximo = eleitor.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
    proximo.click()

    # Enviar
    proximo = eleitor.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    proximo.click()

    eleitor_aleatorio = randint(100,800000000000)

    sg = 'CDC'

    resultado['Paulo'] += 1

    print('---------------------------------------------------------------------------------')
    print(Fore.RED + '----BoultPress----')

    print(Fore.GREEN, 'O Colaborador: {}{} acabou de votar!!!!'.format(sg,eleitor_aleatorio))

    print(Fore.WHITE, 'Candidato: Paulo  votos: {} '.format(resultado['Paulo']))
    print('---------------------------------------------------------------------------------')

    eleitor.close()
