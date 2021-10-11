# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.common.keys import Keys

'''
Bugs identificados a serem corrigios:
    
    *_Caso houver mensagens diferentes do mesmo remetente que chegaram no mesmo
    minuto ele nao considera como duas mensagens e acaba nao lendo a ultima
    
    *_Caso nao haja mensagens novas o bot ficara esperando na tela inicial,
    porem caso o usuario click em um chat qualquer o bot ira ler a ultima 
    mensagem da conversa e caso esta seja diferente da que esta no arquivo 
    de log ele começara uma conversa com o usuario clicado
'''


#############################################################################
#Classe Whatsapp
class WhatsappBot:
    
    def enviarmensagens(self, mensagem, browser):
        self.mensagem = mensagem
        self.browser = browser#.find_element_by_xpath('./../../../..')
        barra_envio = self.browser.find_element_by_class_name('_1SEwr')
        chat_box = barra_envio.find_element_by_class_name('_13NKt')
        #chat_box = self.browser.find_element_by_class_name('_13mgZ')
        sleep(0.5)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        botao_enviar = barra_envio.find_element_by_class_name('_4sWnG')
                #"//span[@data-icon='send']")
        sleep(0.5)
        botao_enviar.click()
        

    
    def pegar_novas_mensagens(self, browser):
        mensagem  = ''
        pegardono = ''
        ultimamensagem = ''
        mensagensclicado = 0 #verifica se o chat selecionado no momento possui
        #novas mensagens
        
        #pegando lista de chats lateral esquerda
        listaremetentes = browser.find_elements_by_class_name('_3m_Xw')
        remetente_arquivo = ''
        horaultima_arquivo = ''
        mensagem_arquivo = ''
        #pegando cada remetente e checando quais tem novas mensagens
        for item in listaremetentes:
            mensagensclicado = 0
            msgnova = ''
            remetente = ''
            horaultima = ''
            #pegando o remetente da conversa
            remetente = item.find_element_by_class_name('zoWT4').text
            #pegando a hora da ultima conversa
            horaultima = item.find_element_by_class_name('_1i_wG').text
            #variavel temporaria para armazenar o componente pai do numero de mensagens
            temp = item.find_element_by_class_name('_37FrU')
            #pegando o numero de novas mensagens na notificaçao
            msgnova = temp.find_element_by_class_name('_1i_wG').text
            try:
                msgnova = int(msgnova)
            except:
                msgnova = 0
            
            if msgnova > 0:
                #clicando no chat que possui nova mensagem
                item.find_element_by_class_name('zoWT4').click()
                #aguardando alguns segundos para as mensagens serem carregadas
                #time.sleep(2)
                #subindo niveis no DOM para acessar todas as mensagens do chat
                #selecionado acima com click
                conversas = item.find_element_by_xpath('./../../../../../../..')
                #pegando as conversas do remetente selecionado
                conversas = conversas.find_elements_by_xpath("//div[@class='y8WcF']")
                sleep(1)
                
                for conversa in conversas:
                    mensagemteste = conversa.text.split('\n')
                    mensagem = str(mensagemteste[-2:-1]).strip('[]')
                    
                
                #adicionando a ultima mensagem a ser gravada no arquivo
                remetente_arquivo = remetente
                horaultima_arquivo = horaultima
                mensagem_arquivo = mensagem
                print(f'{remetente} enviou a seguinte mensagem {mensagem}')
               
            else:
                mensagensclicado = 1
        
        if mensagensclicado == 1:
            file = open('mensagenswhats.txt', 'r')
            ultimamensagem = file.readline().split(',')
            #tratando quando o arquivo de logs de mensagens esta vazio
            #caso vazio nao sera lido pois possivelmente e a primeira vez
            #que o script esta sendo executado
            if len(ultimamensagem) > 1:
                conversas = item.find_element_by_xpath('./../../../../../../..')
                conversas = conversas.find_elements_by_xpath("//div[@class='y8WcF']")
                for conversa in conversas:
                    pegardono = ''
                    #pegardono = conversa.find_element_by_xpath("//div[@class='_2F01v']")
                    pegardono = conversa.get_attribute('innerHTML').split('class="_2wUmf')
                    mensagemfull = conversa.text.split('\n')
                    mensagem = str(mensagemfull[-2:-1]).strip('[]')
                    
                                         
                    
                if mensagem != ultimamensagem[2] and remetente == ultimamensagem[0]:
                    #print(pegardono[-1:])       
                    if '<div class="_2F01v">' in str(pegardono[-1:]):
                        mensagem = ''
                    else:
                        #adicionando a ultima mensagem a ser gravada no arquivo
                        remetente_arquivo = remetente
                        horaultima_arquivo = horaultima
                        mensagem_arquivo = mensagem
                        print(f'{remetente} enviou a seguinte mensagem {mensagem} estou aqui')
                else:
                    mensagem = ''
                    print('Não há novas mensagens1')
            else:
                mensagem = ''
                print('Não há novas mensagens2')
                    
            file.close()
            
            
        if remetente_arquivo != '':
            file = open('mensagenswhats.txt', 'w')
            file.write(f"{remetente_arquivo},{horaultima_arquivo},{mensagem_arquivo}")
            file.close()
            
        return mensagem        
        
