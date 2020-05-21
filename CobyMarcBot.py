# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
from testCompilador import Interpret



# Defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
# update i context contenen informació interessant del bot
def start(update, context):

    text = '''
Hola amic. Sóc en Coby 🤖, un Bot que t\'ajuda a crear Skylines.
    
Pots escriure les següents comandes per a obtenir més informació🤙🏻

*/start*: Inicia la conversa amb el Bot.

*/help*: Llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.

*/author*: Autor del projecte

*/lst*: Mostra els identificadors definits i la seva corresponent àrea.

*/clean*: Esborra tots els identificadors definits.

*/save id*: Guarda un skyline definit amb el nom id.sky.

*/load id*: Carrega un skyline de l’arxiu id.sky.
    '''
    #context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(file, 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id,parse_mode='Markdown',text=text)
    #context.bot.send_message(chat_id=update.effective_chat.id, text="🎗")

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def info(update, context):
    text = "El meu autor és en Marc Domènech"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def hora(update, context):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(current_time))

# defineix una que s'executa quan arriba un text sense comanda
def compilador(update, context):
    input = update.message.text
    file = 'image.png'
    #instruccio =''.join(input)
    print('Instruccio',input)
    try:
        area,altura = antlr.executarInstruccio(input)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Area: {}\nAltura: {}'.format(str(area), str(altura)))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(file, 'rb'))
    except:
        result = antlr.executarInstruccio(input)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=result)

def help(update,context):
    text = '''
Aquestes són totes les coses que puc fer:

Per a crear un nou edifici cal saber:

*Inici:* Posicio on comença l\'edifici

*Altura:* L\'altura del edifici

*Fi:* Posicio on acaba l\'edifici

_Exemple: (1,2,3)_ 

En aquest cas estariem creant un edifici que comença a 1, acaba en 3 i té una altura de 2


A més puc operar amb aquests edificis i generar Skylines:

*Unio:* _Exemple: (1,2,3) + (4,5,6)_

*Intersecció:* _Exemple: (1,2,3) * (4,5,6)_

*Repetir:* _Exemple (1,2,3) * 4_

*Desplaçar a la dreta:* _Exemple (1,2,3) + 4)_

*Desplaçar a l\'esquerra:* _Exemple (1,2,3) - 4)_

*Mirall:* _Exemple (1,2,3)_

*Assignació:* _Exemple: miEdificio := (6,7,8)_
        '''
    context.bot.send_message(chat_id=update.effective_chat.id,parse_mode='Markdown',
                             text=text)



def suma(update, context):
    try:
        x = float(context.args[0])
        y = float(context.args[1])
        s = x + y
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(s))
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')





# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('info', info))
dispatcher.add_handler(CommandHandler('hora', hora))
dispatcher.add_handler(CommandHandler('suma', suma))
dispatcher.add_handler(CommandHandler('compilador', compilador))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=compilador))

antlr = Interpret()


# Engega el bot
updater.start_polling()