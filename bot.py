# importem l'API de Telegram i Interpret
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from interpret import Interpret


class Bot():

    # Constructor
    def __init__(self):
        # Declara una constant amb el access token que llegeix de token.txt
        TOKEN = open('token.txt').read().strip()

        # Imatge que anirà enviant el Bot amb el Skyline del moment
        self.file = 'Imatges/FigActual.png'

        # Crea objectes per treballar amb Telegram
        self.updater = Updater(token=TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher

        # Enllaça les comandes amb els metodes
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

    # Metode que es linkarà amb la comanda /start. S'inicia el bot  i mostrem
    # totes les possibles comandes que podem demanra-li
    # update i context contenen informació interessant del bot
    def start(self, update, context):
        # Cada usuari tindrà un interpre amb la seva taula de Skylines
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

    # Metode que es linkarà amb la comanda /help.
    # Es dona tota l'informació de com crear Skylines i explica totes les
    # operacions que es poden aplicar sobre ells
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

    # Metode que es linkarà amb la comanda /author.
    # Dona l'informació de qui ha estat el seu author
    def author(self, update, context):
        text = '''
El meu autor és en *Marc Domènech* 🙃

Pots posar-te en contacte amb ell via mail a:

`marc.domenech.vila@est.fib.upc.edu`'''
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Metode que es linkarà amb la comanda /lst.
    # Mostra al usuari el llistat de variables que te fins al moment
    def lst(self, update, context):
        # Descarreguem la taula de simbols del usuari
        taula = context.user_data['antlr'].getTaulaSimbols()
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

    # Metode que es linkarà amb la comanda /clean.
    def clean(self, update, context):
        # Carreguem al usuari una taula de simbols buida
        context.user_data['antlr'].setTaulaSimbols({})
        text = 'Acabo de esborrar totes els Skylines que tenies guardats\n\n'
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Metode que es linkarà amb la comanda /save.
    # Guarda el Skyline que es passa per parametre per a que pugui ser
    # accessible desde l'usuari en qualsevol moment en format .sky
    def save_id(self, update, context):
        # Si l'usuari no ha introduit el ID del Skyline a guardar...
        if (len(context.args) == 0):
            text = 'T\'has deixat dir-me quin Skyline vols que et guardi'
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)
        else:
            # Extraiem el ID del Skyline i el ID del usuari
            id = str(context.args[0])
            username = str(update.message.from_user.id)

            # Si tenim l'ID en la taula de simbols, el guardarem, sino mostrarem un missatge d'error
            if (id in context.user_data['antlr'].getTaulaSimbols()):
                context.user_data['antlr'].saveSkyline(id, username)
                text = 'He guardat l\'edifici ' + id
            else:
                text = 'No tinc cap edifici que es digui ' + id
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

    # Metode que es linkarà amb la comanda /load.
    # Descarrega el Skyline que te guardat el usuari en format .sky
    def load_id(self, update, context):
        # Si l'usuari no ha introduit el ID del Skyline a guardar...
        if (len(context.args) == 0):
            text = 'T\'has deixat dir-me quin Skyline vols que et guardi'
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)
        else:
            # Extraiem el ID i descarreguem el Skyline
            id = str(context.args[0])
            username = str(update.message.from_user.id)
            # Intentem descarregar el Skyline que ens demana
            try:
                # Descarreguem el Skyline demanat
                newSk = context.user_data['antlr'].loadSkyline(id, username)

                # Extreiem l'area i l'altura
                area = str(newSk.getArea())
                alçada = str(newSk.getAltura())

                text = 'Area: {}\nalçada: {}'.format(area, alçada)
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            # No s'ha pogut trobar el arxiu
            except Exception as _:
                text = 'No tinc cap edifici que es digui \'' + id + '\''
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    # Metode que es linkarà cada cop que l'usuari envii un missatge de text.
    # Rep un missatge, el processa, i retorna la l'operació que s'especificava en
    # el missatge
    def interpret(self, update, context):
        input = update.message.text
        #print('Instruccio', input)
        # Provem d'extreure el resultat de executar l'instrucció
        # Si ens retorna dos valors, es que el resultat ha estat
        # un Skyline
        info = context.user_data['antlr'].executarInstruccio(input)
        print('Info: ', info)
        # Si info es una tupla, es que tenim un Skyline per tant, area i altura
        if (type(info) is tuple and info[0] is not None):
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(self.file, 'rb'))
            context.bot.send_message(chat_id=update.effective_chat.id, text='Area: {}\nAlçada: {}'.format(str(info[0]), str(info[1])))

        elif (type(info) is tuple):
            context.bot.send_message(chat_id=update.effective_chat.id, text=info[1])

        # Si info es None, es que hi ha hagut algun error al tractar l'instrucció
        elif (info is None):
            text = 'No entenc el que em vols dir. Intenta-ho un altre cop'

        # Si info es qualsevol altra tipus de dades, simplement imprimirem el resultat.
        else:
            text = info

        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


bot = Bot()
