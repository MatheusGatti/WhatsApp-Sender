from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# EXTRAIR OS NÚMEROS
fileName = input("[?] Nome do arquivo com os números: ")

try:
    file = open(fileName, "r")
except Exception as e:
    exit("[X] Erro: " + e)

numbers = set()

for line in file.readlines():
    if 'TEL;type=CELL;type=VOICE;type=pref:' in line:
        numbers.add(line.replace(
            'TEL;type=CELL;type=VOICE;type=pref:', '').strip())

print("[!] {} números extraidos.".format(len(numbers)))

numbers = list(numbers)

# Ler mensagem
fileName = input("[?] Nome do arquivo com a mensagem: ")

try:
    file = open(fileName, "r")
except Exception as e:
    exit("[X] Erro: " + e)

message = file.read()

# Entrar no WhatsApp

chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--incognito")
browser = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chromeOptions)

browser.get("https://web.whatsapp.com/")

input("[?] Aperte <ENTER> após se conectar ao WhatsApp.")

JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.innerText += txt;
  elm.dispatchEvent(new Event('change'));
  """

# Enviar mensagens
for number in numbers:
    try:
        browser.find_element_by_xpath(
            '//*[@id="side"]/div[1]/div/label/div/div[2]').clear()
        browser.find_element_by_xpath(
            '//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(number)
        time.sleep(1)
        if 'Nenhuma conversa, contato ou mensagem foram encontradas' not in browser.page_source:
            print('[+] Enviando mensagem para {}'.format(number))
            browser.find_element_by_xpath(
                '//div[@class="_3m_Xw"][contains(@style, "z-index: 0")]').click()
            time.sleep(1)
            browser.execute_script(JS_ADD_TEXT_TO_INPUT, browser.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'), message)
            browser.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys('.')
            browser.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        else:
            print('[-] Número {} não encontrado.'.format(number))
        time.sleep(5)
    except:
        pass
