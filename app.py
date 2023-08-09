from selenium import webdriver
"""from selenium.webdriver.chrome.service import Service as ChromeService"""
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,1000', '--incognito', '--headless', '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome()
        """service=ChromeService(ChromeDriverManager().install()), options=chrome_options)"""

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )


    return driver, wait


while True:
    driver, wait = iniciar_driver()
    driver.get('https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fmynetwork%2F&fromSignIn=true&trk=cold_join_sign_in')
    driver.maximize_window()
    sleep(5)
    username = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'username')))
    email = input('Digite o E-MAIL: ')
    username.send_keys(email)
    password = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'password')))
    senha = input('Digite a SENHA: ')
    password.send_keys(senha)
    button_login = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    button_login.click()
    sleep(15)
    driver.execute_script('window.scrollTo(0,3500)')
    sleep(3)
    pessoas = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//span[text()='Conectar']")))
    total_conexoes = 0
    for pessoa in pessoas:
        pessoa.click()
        total_conexoes = total_conexoes + 1
        print('Clicado!')
        sleep(5)
    print(f'Foram feitas um total de {total_conexoes} conexões!')
    driver.close()
    sleep(3600)
