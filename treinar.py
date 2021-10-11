# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

'''
como instalar 
pip install chatterbot
pip install ChatterBotCorpusTrainer
'''


chatbot = ChatBot('Meu Bot')

#######################################
#treinando com os dados do corpus
trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
    "conversas-treinamento/"
)