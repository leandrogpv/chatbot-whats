# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from time import sleep
from threading import Thread
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import bot_whats
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-extensions")


browser = webdriver.Chrome(options=options)

#iniciando arquivo que contem a ultima mensagem enviada pelo cliente
iniciaarquivo = open('mensagenswhats.txt', 'a').close()

##############################################################################
#Bot Watsapp               
urlwhats = 'https://web.whatsapp.com/'
#iniciando o driver para chamar o firefox
option = Options()
option.headless = False
#iniciando o firefox
#browser = webdriver.Firefox(options=option)
#chamando a URL a ser pesquisada
browser.get(urlwhats) 
#aguardando 20 segundos para carregar a pagina e liberar o codigo
sleep(20)


def mensagens_whatsapp():
    mensagem = ''
    response = ''
    ##########################################################################
    #iniciando o chatbot
    chatbot = ChatBot('Meu Bot',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    )
    
    ##########################################################################
    #iniciando as funçoes do whatsapp
    botwhats = bot_whats.WhatsappBot()
    mensagem = botwhats.pegar_novas_mensagens(browser)
    if mensagem != '':
        print(f'Mensagem enviada pelo cliente {mensagem}')
        response = chatbot.get_response(mensagem).text   
        print(f'BOT respondeu {response}')
        botwhats.enviarmensagens(response, browser)
    

##############################################################################
#loop principal do chatbot
while True:
    
    mensagens_whatsapp()
		
    sleep(0.05)
    
    
    
