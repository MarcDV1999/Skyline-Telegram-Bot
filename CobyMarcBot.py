# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
from testCompilador import Interpret



# Defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
# update i context contenen informació interessant del bot
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, pequeño Timmy.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="🎗")

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
    text = 'Sóc en Coby, un Bot que t\'ajuda a crear Skylines. Aquestes són totes les coses que puc fer:\n' \
           'Per a crear un nou edifici cal que l\'especifiquis aixi -> (xmin.altura,xmax) on:\n' \
           'xmin: Posicio on comença l\'edifici\n' \
           'altura: L\'altura del edifici\n' \
           'xmax: Posicio on acaba l\'edifici\n' \
           'Pots guardar els teus Skylines en variabls, per exemple pots fer:\n' \
           'a := (1,2,3) per a guardarte un Skyline amb l\'etiqueta \'a\'\n' \
           'Disposes de les següents operacions per a treballar amb Skylines:\n' \
           'Unio: Skyline + Skyline ( (1,2,3) + (4,5,6) )\n' \
           'Intersecció: Skyline * Skyline ( (1,2,3) * (4,5,6) )\n' \
           'Repetir: Skyline * numero ( (1,2,3) * 4 )\n' \
           'Desplaçar a la dreta: Skyline + numero ( (1,2,3) + 4) )\n' \
           'Desplaçar a l\'esquerra: Skyline - numero ( (1,2,3) - 4) )\n' \
           'Mirall: - Skyline ( -(1,2,3) )\n' \
           'Assignació: etiqueta := Skyline ( (miEdificio := (6,7,8)) )'
    context.bot.send_message(chat_id=update.effective_chat.id,
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