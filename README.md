# SkyLand Marc Domènech

Pràctica de Python de l'assignatura de Llenguatges de Programació de la Facultat d'Informàtica de Barcelona. En aquesta pràctica he realitzat un Bot de Telegram capaç de generar Skylines de ciutats.



## Instal·lació i execució



### Requirements.txt

En aquest fitxer, és troben totes les llibreries necessàries per a poder executar el bot. Per a instalar totes les llibreries del fitxer només cal executar la següent instrucció en el terminal.

```
pip install -r requirements.txt
```

Com executar el programa

```
python3 bot.py
```





## Funcionament General

El programa principal és el bot.py. Aquest fitxer, genera un objecte del tipus Bot i l'inicialitza. Un cop executat el programa, el bot passa a estar a disposició de l'usuari.

L'usuari te dues opcions per a interactuar amb el bot. 

### Mitjançant comandes:

- **/start**: Inicia la conversa amb el Bot.

- **/help**: Llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.

- **/author**: Autor del projecte

- **/lst**: Mostra els identificadors definits i la seva corresponent àrea.

- **/clean**: Esborra tots els identificadors definits.

- **/save _id_**: Guarda un Skyline per a que puguis fer-lo servir quan vulguis.

- **/load _id_**: Carrega un skyline que tenies guardat.

  

### Mitjançant missatges de text sense comandes:

- **Crear Skyline Simple**:

  Crea un Skyline amb només un edifici

  ```
  (1,2,3)
  ```

- **Crear Skyline Compost**:

  Crea un Skyline amb diversos edificis

  ```
  [(1,2,3),(4,5,6)]
  ```

- **Crear Skyline aleatori**:

  Crea un Skyline amb `n` edificis, cadascun d’ells amb una alçada aleatòria entre `0` i `h`, amb una amplada aleatòria entre `1` i `w`, i una posició d’inici i de final aleatòria entre `xmin` i `xmax`

  ```
  {200,50,10,1,200}
  ```

- **Assignació**:

  Guarda un Skyline en una variable temporal.

  ```
  a := (1,2,3)
  ```

- **Unió**:

  Uneix dos Skylines, quedant-se amb les parts comunes i no comunes dels dos.

  ```
  a := (1,2,3) + (2,4,6)
  ```

- **Intersecció**:

  Uneix dos Skylines, quedant-se només mab les parts comunes dels dos.

  ```
  a := (1,2,3) * (2,4,6)
  ```

- **Repetir**:

  Replica `n`cops el Skyline

  ```
  a := (1,2,3) * 2
  ```

- **Desplaçar a la dreta**:

  Desplaça cap a la dreta `n`posicions

  ```
  a := (1,2,3) + 2
  ```

- **Desplaçar a l'esquerra**:

  Desplaça cap a l'esquerra `n`posicions. El Skyline mai començarà en posicions negatives.

  ```
  a := (1,2,3) - 2
  ```

- **Mirall**:

  Reflecteix el Skyline

  ```
  a := -(1,2,3)
  ```

Cal destacar, la diferencia entre enviar el missatge `a := (1,2,3)` i el missatge `(1,2,3)`. En el primer cas el Skyline es guarda a la variable `a`, en el segon cas, el bot només mostra com quedaria un Skyline amb aquesta forma, en cap cas el guarda.



## Fitxers i Classes

En aquest projecte intervenen principalment 3 Classes importants:

### Skyline.py

Aquesta és la classe que s'encarrega de gestionar els Skylines. Hi trobem mètodes per operar amb ells a més de poder-los guardar en imatges i en format .sky. 

#### Implementació

Respecte a la implementació, he optat per a implementar un mètode per cada operador. Aquests mètodes apliquen l'operació agafant els Skylines del paràmetre implícit i del paràmetre explícit.

Un cop implementats els mètodes he optat per sobrecarregar els operadors de la classe (+, *, -, ...).

#### Atributs interessants

En aquest apartat comentaré breument, certs atributs interessants de la classe Skyline per a poder entendre el funcionament del bot. Prendrem com exemple aquest Skyline:

```
a := [(1,2,3),(3,2,5),(5,5,10)]
```



![1-llistaAccions](ImatgesDocument/llistaAccions.jpg)

- **self.llistaAccions**: Llista en la que guardem el llistat de accions que han fet possible generar el Skyline. En el Skyline de la figura tindriem:

  ```
  self.llistaAccions = [(1,2,3),(3,2,5),(5,5,10)]
  ```

  

- **self.llistaParts**: Si agafem el mateix Skyline de adalt, el llistat de parts seria un llista amb les accions sintetitzades. En aquest cas la llista de parts quedaria de la següent forma:

  ```
  self.llistaParts = [(1,2,5),(5,5,10)]
  ```

  Veiem com en aquest cas les accions _(1,2,3)_ i _(3,2,5)_ és poden unificar en una sola part.




### Interpret.py

Aquesta és la classe que s'encarrega de analitzar sintàcticament les expressions escrites per l'usuari en el xat de telegram. Un cop fet l'anàlisis, fa ús de la classe Skyline per calcular el Skyline corresponent.

Conté un mètode per executar una instrucció i diversos mètodes per a comunicar el Bot de Telegram amb els Skylines del usuari.



### Bot.py

Aquesta és la classe que implementa el Bot. En aquesta classe es defineixen les funcions Handler que enllaçant amb les comandes del Bot. Aquesta classe fa ús de la classe interpret.py per a poder tractar amb la gramàtica i els Skylines.

S'emmagatzema per cada usuari el llistat dels seus Skylines de manera que es manté la privacitat de les dades en aquest sentit.



## Algorismes interessants

### Calcular les parts d'un edifici

De cara a implementar les operacions de unió i intersecció, m'ha semblat interessant que cada Skyline tingues un atribut "_llistaParts_". Per a poder calcular aquesta llista només ha calgut, recorrer la llista d'accions ordenada i compactar al maxim les accions, formant parts.



## Observacions

Donat que el temps per a fer aquesta pràctica ha estat limitat, no he pogut implementar totes les funcionalitats que m'agradaria haver-hi implementat si hi hagués tingut més temps. M'hauria agradat afegir més funcionalitats al programa, com per exemple poder introduir expressions aritmètiques dins de la construcció de Skylines compostos. També m'hauria agradat donar més informació sobre quin error està cometent l'usuari a l'hora d'introduir alguna comanda, per així facilitar la interacció amb l'usuari.



## Autor

- **Marc Domènech i Vila** - *Initial work* - [MarcDV1999](https://github.com/MarcDV1999)

## Llicencia

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/MarcDV1999/4-en-Ratlla/blob/master/LICENSE.md) file for details

## Agraïments

- Gràcies al meu germà per dedicar-se a testejar que el bot funciona correctament.

