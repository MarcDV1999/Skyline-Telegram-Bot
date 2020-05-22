# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from testCompilador import Interpret

class Bot():

    def __init__(self):
        # declara una constant amb el access token que llegeix de token.txt
        TOKEN = open('token.txt').read().strip()
        self.file = 'Imatges/FigActual.png'

        # crea objectes per treballar amb Telegram
        updater = Updater(token=TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        # indica que quan el bot rebi la comanda /start s'executi la funció start
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CommandHandler('help', self.help))
        dispatcher.add_handler(CommandHandler('author', self.author))
        dispatcher.add_handler(CommandHandler('lst', self.lst))
        dispatcher.add_handler(CommandHandler('clean', self.clean))
        dispatcher.add_handler(CommandHandler('save', self.save_id))
        dispatcher.add_handler(CommandHandler('load', self.load_id))
        dispatcher.add_handler(CommandHandler('suma', self.suma))
        dispatcher.add_handler(CommandHandler('compilador', self.compilador))
        dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self.compilador))

        self.antlr = Interpret()

        # Engega el bot
        updater.start_polling()

    # Defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
    # update i context contenen informació interessant del bot
    def start(self, update, context):

        text = '''
Hola amic. Sóc en `Coby` 🤖, un Bot que t\'ajuda a crear Skylines.

Pots escriure les següents *comandes* per a obtenir *més informació* 🤙🏻

  
-> */start*: Inicia la conversa amb el Bot.
    
-> */help*: Llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.
    
-> */author*: Autor del projecte
    
-> */lst*: Mostra els identificadors definits i la seva corresponent àrea.
    
-> */clean*: Esborra tots els identificadors definits.
    
-> */save id*: Guarda un Skyline per a que puguis fer-lo servir quan vulguis.
    
-> */load id*: Carrega un skyline que tenies guardat.
        '''
        #context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
        context.bot.send_message(chat_id=update.effective_chat.id,parse_mode='Markdown',text=text)
        #context.bot.send_message(chat_id=update.effective_chat.id, text="🎗")


    def help(self, update,context):
        text = '''
    🤖 *Aquestes són totes les coses que puc fer*:
    
    Per a crear un nou edifici cal saber:
    
    *[Inici]:* Posicio on comença l\'edifici
    
    *[Altura]:* L\'altura del edifici
    
    *[Fi]:* Posicio on acaba l\'edifici
    
        -> `Exemple: (1,2,3)`
    
En aquest cas estariem creant un edifici que comença a 1, acaba en 3 i té una altura de 2. _(Inici,Altura,Fi)_
    
    
A més puc operar amb aquests edificis i crear Skylines:
    
*Crear Skyline Simple:* Crear Skyline amb un edifici predefinit -> `Exemple: (6,7,8)`
    
*Crear Skyline Compost:* Crear Skyline amb diversos edificis predefinits -> `Exemple: [(1,2,3),(4,5,6),(7,8,9)]`
    
*Crear Skyline Aleatori:* Construeix [n] edificis, cadascun d’ells amb una alçada aleatòria entre *[0 i h]*, amb una *amplada aleatòria* entre *[1 i w]*, i una posició d’inici i de final aleatòria entre *[xmin i xmax]*. `{n, h, w, xmin, xmax}` -> `Exemple: {200,50,10,1,200}`
    
    
*Assignació:* Etiquetar Skyline -> `Exemple: miEdificio :=(6,7,8)`
    
*Unio:* Exemple: Uneix els 2 Skylines `(1,2,3) + (4,5,6)`
    
*Intersecció:* Només es queda amb les parts comunes -> `Exemple: (1,2,3) * (4,5,6)`
    
*Repetir:* Replica el Skyline n cops -> `Exemple (1,2,3) * 4`
    
*Desplaçar a la dreta:* -> `Exemple (1,2,3) + 4)`
    
*Desplaçar a l\'esquerra:* -> `Exemple (1,2,3) - 4)`
    
*Mirall:* Calcula el Skyline invertit -> `Exemple - (1,2,3)`

*Nota:* Tots els Skylines que facis servir s'esborraràn al acabar la sessió, utilitza les comandes /load i /save per a mantenir-los
            '''
        context.bot.send_message(chat_id=update.effective_chat.id,parse_mode='Markdown',
                                 text=text)


    # defineix una funció que mostra l'autor del Bot (Comanda /author)
    def author(self, update, context):
        text = '''
    El meu autor és en *Marc Domènech* 🙃
    
Pots posar-te en contacte amb ell via mail a:
        
`marc.domenech.vila@est.fib.upc.edu`'''
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',text=text)


    def lst(self, update, context):
        taula = self.antlr.getTaulaSimbols()
        text = 'Aqui tens els Skylines que tens guardats:\n\n'
        if(len(taula) > 0):
            for key,valor in taula.items():
                area = valor.getArea()
                text += '*{}* ----> Àrea = *{}*\n\n'.format(key,area)
        else:
            text += '''
        Encara no tens cap Skyline guardat.
            
        Pots consultar com guardar-ne amb la comanda */help*
            '''
        context.bot.send_message(chat_id=update.effective_chat.id,parse_mode='Markdown',text=text)


    def clean(self, update, context):
        text = 'Esborro tots els Skylines que tenies guardats\n\n'
        self.antlr.setTaulaSimbols({})
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)


    def save_id(self, update, context):
        try:
            id = str(context.args[0])
            if (id in self.antlr.getTaulaSimbols()):
                self.antlr.saveSkyline(id)
            else:
                print('No tinc cap edifici amb aquest ID')
        except:
            print('No he pogut guardar l\'imatge de',context.args[0])


    def load_id(self, update, context):
        try:
            id = str(context.args[0])
            newSk = self.antlr.loadSkyline(id)
            area = str(newSk.getArea())
            altura = str(newSk.getAltura())

            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Area: {}\nAltura: {}'.format(area, altura))
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
        except:
            print('No tinc l\'imatge de', context.args[0])



    # defineix una que s'executa quan arriba un text sense comanda
    def compilador(self, update, context):
        input = update.message.text
        #instruccio =''.join(input)
        print('Instruccio',input)
        try:
            area,altura = self.antlr.executarInstruccio(input)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Area: {}\nAltura: {}'.format(str(area), str(altura)))
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
        except:
            result = self.antlr.executarInstruccio(input)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=result)




    def suma(self, update, context):
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



bot = Bot()


