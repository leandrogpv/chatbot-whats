# chatbot-whats

Bugs identificados a serem corrigios:
    
    *_Caso houver mensagens diferentes do mesmo remetente que chegaram no mesmo
    minuto ele nao considera como duas mensagens e acaba nao lendo a ultima
    
    *_Caso nao haja mensagens novas o bot ficara esperando na tela inicial,
    porem caso o usuario click em um chat qualquer o bot ira ler a ultima 
    mensagem da conversa e caso esta seja diferente da que esta no arquivo 
    de log ele começara uma conversa com o usuario clicado
