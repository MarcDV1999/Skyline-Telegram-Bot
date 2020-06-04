# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from interpret import Interpret


class Bot():

    # Constructor
    def __init__(self):
        # declara una constant amb el access token que llegeix de token.txt
        TOKEN = open('token.txt').read().strip()
        self.file = 'Imatges/FigActual.png'

        # crea objectes per treballar amb Telegram
        self.updater = Updater(token=TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher

        # Enllaça les comandes amb les funcions
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CommandHandler('help', self.help))
        dispatcher.add_handler(CommandHandler('author', self.author))
        dispatcher.add_handler(CommandHandler('lst', self.lst))
        dispatcher.add_handler(CommandHandler('clean', self.clean))
        dispatcher.add_handler(CommandHandler('save', self.save_id))
        dispatcher.add_handler(CommandHandler('load', self.load_id))
        # Enllaça un missatge normal de text amb la funció interpret
        dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self.interpret))

        # Engega el bot
        self.updater.start_polling()

    # Defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
    # update i context contenen informació interessant del bot
    def start(self, update, context):
        # Creem el objecte Interpret
        context.user_data['antlr'] = Interpret()
        nom = update.message.from_user.first_name
        nomBot = 'Bob l\'Arquitecte'
        text = '''
Hola {}. Sóc en `{}` 🤖, un Bot que t\'ajuda a crear Skylines.

Pots escriure les següents *comandes* per a obtenir *més informació* 🤙🏻


-> */start*: Inicia la conversa amb el Bot.

-> */help*: Llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.

-> */author*: Autor del projecte

-> */lst*: Mostra els identificadors definits i la seva corresponent àrea.

-> */clean*: Esborra tots els identificadors definits.

-> */save id*: Guarda un Skyline per a que puguis fer-lo servir quan vulguis.

-> */load id*: Carrega un skyline que tenies guardat.
        '''.format(nom, nomBot)

        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Defineix la funció que dona informació sobre les operacions.
    def help(self, update, context):
        text = '''
    🤖 *Aquestes són totes les coses que puc fer*:

    Per a crear un nou edifici cal saber:

    *[Inici]:* Posicio on comença l\'edifici

    *[Alçada]:* L\'Alçada del edifici

    *[Fi]:* Posicio on acaba l\'edifici

        -> `Exemple: (1,2,3)`

En aquest cas estariem creant un edifici que comença en `x = 1`, acaba en `x = 3` i té una alçada de `2`. _(Inici,Alçada,Fi)_


A més puc operar amb aquest edifici i crear tants Skylines com jo vulgui:

*Crear Skyline Simple:* Puc crear Skyline amb un edifici que tu em diguis -> `Exemple: (6,7,8)`

*Crear Skyline Compost:* Puc crear Skyline amb diversos edificis a la vegada -> `Exemple: [(1,2,3),(4,5,6),(7,8,9)]`

*Crear Skyline Aleatori:* Puc crear un Skyline amb *[n]* edificis, cadascun d’ells amb una alçada aleatòria entre *[0 i h]*, amb una amplada aleatòria entre *[1 i w]*, i una posició d’inici i de final aleatòria entre *[xmin i xmax]*. `{n, h, w, xmin, xmax}` -> `Exemple: {200,50,10,1,200}`


*Assignació:* Etiquetar Skyline -> `Exemple: miEdificio :=(6,7,8)`

*Unio:* Exemple: Uneix els 2 Skylines `(1,2,3) + (4,5,6)`

*Intersecció:* Només es queda amb les parts comunes -> `Exemple: (1,2,3) * (4,5,6)`

*Repetir:* Replica el Skyline n cops -> `Exemple (1,2,3) * 4`

*Desplaçar a la dreta:* -> `Exemple (1,2,3) + 4)`

*Desplaçar a l\'esquerra:* -> `Exemple (1,2,3) - 4)`

*Mirall:* Calcula el Skyline invertit -> `Exemple - (1,2,3)`

*Nota:* Tots els Skylines que facis servir s'esborraràn al acabar la sessió, utilitza les comandes /load i /save per a mantenir-los
            '''
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Defineix una funció que mostra l'autor del Bot (Comanda /author)
    def author(self, update, context):
        text = '''
El meu autor és en *Marc Domènech* 🙃

Pots posar-te en contacte amb ell via mail a:

`marc.domenech.vila@est.fib.upc.edu`'''
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Defineix la funció que mostra el llistat de variables
    def lst(self, update, context):
        # Descarreguem la taula de simbols
        taula = self.antlr.getTaulaSimbols()
        text = 'Aqui tens els Skylines que tens guardats:\n\n'

        # Si la taula no està buida, extreiem els simbols
        if(len(taula) > 0):
            for key, valor in taula.items():
                area = valor.getArea()
                text += '*{}* ----> Àrea = *{}*\n\n'.format(key, area)
        else:
            text += '''
        Encara no tens cap Skyline guardat.

        Pots consultar com guardar-ne amb la comanda */help*
            '''
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Defineix la funció que Reseteja el llistat de variables
    def clean(self, update, context):
        self.antlr.setTaulaSimbols({})
        text = 'Esborro tots els Skylines que tenies guardats\n\n'
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Defineix la funció que guarda un Skyline en un fitxer .sky
    def save_id(self, update, context):
        print(len(context.args))
        if (len(context.args) == 0):
            text = 'T\'has deixat dir-me quin Skyline vols que et guardi'
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)
        else:
            id = str(context.args[0])
            username = str(update.message.from_user.id)

            # Si tenim l'ID en la taula de simbols, el guardarem, sino mostrarem un missatge d'error
            if (id in context.user_data['antlr'].getTaulaSimbols()):
                print('Tens el Sk: ', id)
                context.user_data['antlr'].saveSkyline(id, username)
                print('Guardat: ', id)

                text = 'He guardat l\'edifici ' + id
            else:
                text = 'No tinc cap edifici que es digui ' + id
                print(text)
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Defineix la funció que carrega un Skyline d'un fitxer .sky
    def load_id(self, update, context):
        try:
            # Extraiem el ID i carreguem el Skyline
            id = str(context.args[0])
            username = str(update.message.from_user.id)
            newSk = context.user_data['antlr'].loadSkyline(id, username)

            # Extreiem l'area i l'altura
            area = str(newSk.getArea())
            alçada = str(newSk.getAltura())

            context.bot.send_message(chat_id=update.effective_chat.id, text='Area: {}\nalçada: {}'.format(area, alçada))
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
        # Si no podem mostrarem un missatge d'error
        except Exception as _:
            text = 'No tinc l\'imatge de ' + context.args[0]
            print(text)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    # Defineix la funció que interpreta les operacions que va escribint el usuari per teclat
    def interpret(self, update, context):
        input = update.message.text
        print('Instruccio', input)
        try:
            # Provem d'extreure el resultat de executar l'instrucció
            # Si ens retorna dos valors, es que el resultat ha estat
            # un Skyline
            area, altura = context.user_data['antlr'].executarInstruccio(input)

            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
            context.bot.send_message(chat_id=update.effective_chat.id, text='Area: {}\nalçada: {}'.format(str(area), str(altura)))
        # En aquest cas el resultat no ha estat un Skyline, pot ser un
        # nombre o que l'expressió no era vàlida
        except Exception as _:
            result = context.user_data['antlr'].executarInstruccio(input)
            if result is None:
                text = 'No entenc el que em vols dir. Intenta-ho un altre cop'
                print(text)
            else:
                text = result
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=text)


bot = Bot()
