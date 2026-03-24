import telebot

CHAVE_API = 'digite aqui a chave da api do seu bot'

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['engenharia'])
def opcao2(msg):
    bot.send_message(msg.chat.id, 'show, otima escolha vou preparar a carta de proposta com todos os valores.')

@bot.message_handler(commands=['administracao'])
def opcao2(msg):
    bot.send_message(msg.chat.id, 'infelizmente estamos com as tumas lotadas no momento, mas se você quiser eu deixo voçê na fila de espera..')

@bot.message_handler(commands=['medvet'])
def opcao2(msg):
   bot.send_message(msg.chat.id, 'legal, otima escolha, vou preparar uma carta de proposta e uma visita tecnica para você conhecer o compus.')






#quando vai criar uma commands tipo a opão tenque sempre vim antes do def para qualquer reposta
@bot.message_handler(commands=['opcao1'])
def opcao1(msg):
    laura = bot.reply_to(msg, 'eu sou a laura,muito prazer e irei te ajudar a fazer um orçamento.\n ' \
    'escolha uma das opções\n' \
    '/engenharia\n' \
    '/administracao\n' \
    '/medvet')
    return laura

@bot.message_handler(commands=['opcao2'])
def opcao2(msg):
    bot.send_message(msg.chat.id, 'para fazer rematricula entre em contato com este email: uniaudi@gmiail.com')

@bot.message_handler(commands=['opcao3'])
def opcao3(msg):
    print(msg)
    bot.send_message(msg.chat.id , 'valou por me chamar em que posso ajudar ?')
    






def verificar(msg):
    if msg.text == 'olá':
        return True
    else: 
        False

@bot.message_handler(func=verificar)
def resposta1(msg):
    bot.reply_to(msg, 'olá aqui e o audimir, como posso ajudar?')
    #replay_to e usado para repsonder aquela mensagem da pessoa e aquela junção que marca a msg encima
    #o @bot sempre tenque ter um em cada def, ele e usando para ler as mensagem e decidir quando essa def vai ser usada 

def verificar2(msg):
    return True

@bot.message_handler(func=verificar2)
def resposta1(msg):
    text = '''escolha uma das opções para continuar(e click nela\n
    /opcao1 orçamento
    /opcao2 rematricula
    /opcao3 falar com um atendente
    responder qualque outra coisa não vai funcionar'''
    bot.reply_to(msg, text)




#isso le as mensagem data e horario etc
bot.polling()