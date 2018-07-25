# -*# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
import os
import json
import requests
import _thread
from telebot import types # Tipos para la API del bot.
from datetime import datetime, date, time, timedelta
import calendar
from threading import Thread
from random import randrange
from os import listdir
from os.path import isfile, join
import time # Librería para hacer que el programa que controla el bot no se acabe.
from pathlib import Path
#import scrapy
import urllib

import sys


now = datetime.now()
horaPole= now.replace(hour=22, minute=6,second=59,microsecond=0)

TOKEN = '[Telegram Bot TOKEN]' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################



#Listener

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
        for m in messages: # Por cada dato 'm' en el dato 'messages'
            if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
                cid = m.chat.id # Almacenaremos el ID de la conversación.
                print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

#####################################################################33 variables

text_messages = {
    'holat':
        u'Un supeeeeer saludo para ti amigo \n',
    'gracias':
        u'De nada nakama por algo soy un supeeeeeeeeer nakama \n',
    'adios':
        u'Hasta luego supeeeeeeer crack :) \n',
    'llora':
        u'No llores vas hacer que yo también llore :,( \n',
    'buenosDias':
        u'Supeeeeer buenos días nakama que tal está el día hoy? \n',
    'buenasTardes':
        u'Supeeeeer buenas tardes nakama que tal está el día hoy? \n',
    'buenasNoches':
        u'Supeeeeer buenas noches nakama que descanses mañana empezará un supeeeeeer día :3 \n',

}

'''class MySpider(scrapy.Spider,link,funcion):
    name = 'mangatux.blogspot.com'
    allowed_domains = ['mangatux.blogspot.com','mangatux.blogspot.com.es','anzanime.club']
    start_urls == [
        link
	]

    def parse(self, response):
        if funcion == 1:
		    auxlink= response.xpath('//a[contains(@href,numcap).extract()
		    #crear una variable myspider y pasarle auxlink como argumento,
			funcion = 2
        if funcion == 2:
            linksImagenes= response.xpath8'//a[contains(@class,"next-tab")]/img/@src').extract()
            #bucle con tamaño maximo del array x = nosque
			#urllib.urlretrieve(x,nombrearchivo.jpg)
			#cerramos bucle

'''
@bot.message_handler(commands=['mangapdf']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def mangapdf(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    x=m.text
    nombre = ' '.join(x.split(" ")[1:])
    #crear una variable 'myspider (que es la clase de arriba) y pasaremos como argumentos  'http://www.anzanime.club/one-piece-manga-' + nombre + '' y funcion = 1


#############################################

#randommmmmmmmmmmmmmmmmmmmmmm



#Funciones

# Handle '/start' and '/help'

@bot.message_handler(commands=['ayudita', 'start'])
def send_welcome(m):
        cid = m.chat.id
        bot.send_message(cid, """\
        Estoy en beta aun no hay muchos comandos :V
    \
    """)



#pole-----------------------------------------------------------------------------------
'''
@bot.message_handler(func=lambda message: True)
def pole(message):
    cid = message.chat.id
    oro=False
    plata=False
    bronce = False

    pole=False
    now = datetime.now()
    if now >= horaPole :
        bot.send_message(message.chat.id, "La hora de la pole")
        oro = True
        plata = True
        bronce = True

        if message.text.lower() == "pole" or message.text.lower() == "oro" and oro is True:
            oro = False
            user = message.from_user.first_name
            bot.send_message(cid, "el usuario " + user + "ha hecho pole")

        if message.text.lower() == "plata" or message.text.lower() == "pene" and plata is True and oro is False:
            plata = False
            user = message.from_user.first_name
            bot.send_message(cid, "el usuario " + user + "ha hecho plata")

        if message.text.lower() == "bronce" or message.text.lower() == "fail" and bronce is True and oro is False and plata is False:
            bronce = False
            user = message.from_user.first_name
            bot.send_message(cid, "el usuario " + user + "ha hecho bronce")


       '''


#@bot.message_handler(commands=['brah']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
#def command_brah(m): # Definimos una función que resuleva lo que necesitemos.

        #cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
        #bot.send_audio( cid, open( 'brah.ogg', 'rb'))



@bot.message_handler(commands=['ayudita', 'start'])
def send_welcome(m):
        cid = m.chat.id
        bot.send_message(cid, """\
        Estoy en beta aun no hay muchos comandos :V
    \
    """)
	
@bot.inline_handler(lambda query: query.query.startswith('spoiler') and len(query.query.split()) > 1)
def function_spoiler(q):

  cid = q.from_user.id
  txt = q.query.split(None, 1)[1]

  keyboard = types.InlineKeyboardMarkup()
  keyboard.add(types.InlineKeyboardButton("Mostrar spoiler", callback_data="spoiler {}".format(txt)))

  article = types.InlineQueryResultArticle(1, "Enviar spoiler", types.InputTextMessageContent("¡Ojo cuidado, SPOILER!"), reply_markup=keyboard)
  bot.answer_inline_query(q.id, [article], cache_time=1)

@bot.callback_query_handler(func=lambda call: call.data.startswith('spoiler'))
def function_button(call):
  spoiler = call.data.split(None, 1)[1]
  bot.answer_callback_query(call.id, spoiler, show_alert=True)

@bot.message_handler(commands=['juego']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def juego(m): # Definimos una función que resuleva lo que necesitemos.

    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    x=m.text
    msg = bot.send_message(cid, 'Elige piedra papel tijera ')
    bot.register_next_step_handler(msg, step_opcion)

def step_opcion(m):
    cid = m.chat.id
    username = m.from_user.username
    id = m.from_user.id
    opcion = m.text.lower()
    rnd = randrange(0, int(2))
    if rnd == 0 :
        if opcion == 'tijera' or opcion == 'tijeras' :
            bot.send_message(cid, 'Me ha salido piedra as perdido @'+ username + ' jajajajja')
        if opcion == 'piedra':
            bot.send_message(cid, 'Me ha salido piedra empate @'+ username + ' chocala :D')
        if opcion == 'papel':
            bot.send_message(cid, 'Me ha salido piedra he perdido. Tu ganas @'+ username + ' :C')
    if rnd == 1 :
        if opcion == 'piedra':
            bot.send_message(cid, 'Me ha salido papel as perdido @'+ username + ' jajajajja')
        if opcion == 'papel':
            bot.send_message(cid, 'Me ha salido papel empate @'+ username + ' chocala :D')
        if opcion == 'tijera' or opcion == 'tijeras' :
            bot.send_message(cid, 'Me ha salido papel he perdido. Tu ganas @'+ username + ' :C')
    if rnd == 2 :
        if opcion == 'papel':
            bot.send_message(cid, 'Me ha salido tijeras as perdido @'+ username + ' jajajajja')
        if opcion == 'tijera' or opcion == 'tijeras' :
            bot.send_message(cid, 'Me ha salido tijeras empate @'+ username + ' chocala :D')
        if opcion == 'piedra':
            bot.send_message(cid, 'Me ha salido tijeras he perdido. Tu ganas @'+ username + ' :C')




#@bot.message_handler(commands=['malzi']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
#def command_malzi(m): # Definimos una función que resuleva lo que necesitemos.

        #cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
        #bot.send_message( cid, 'No me hables de ese le pone ebola a mis torres y las derrite puto malz de la polla comeme el rabo si me escuchas destruire el vacio entero para matarte cabrón :v') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.bot
        #bot.send_photo( cid, open( 'malz.jpg', 'rb'))



#audios-----------------------------------------------------------------------------------




#@bot.message_handler(commands=['brah']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
#def command_brah(m): # Definimos una función que resuleva lo que necesitemos.

        #cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
        #bot.send_audio( cid, open( 'brah.ogg', 'rb'))
'''
<?
$url = 'https://api.telegram.org/bot' . $bot_id . '/sendChatAction?&chat_id='.$usuario.'&action=typing';
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$output = curl_exec($ch);
curl_close($ch);
if ($output){
  $array = json_decode($output,true);
  if ($array["ok"] == 1){
    //EL USUARIO ESTÁ ACTIVO
  }else{
    $mensaje = "El usuario <code>".$usuario."</code> ha bloqueado el bot: ".$array["description"];
  }
}
?>




bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)



@bot.message_handler(commands=['aviso']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def aviso(m):

    cid = m.chat.id
    id = m.from_user.id

    if cid == 247295279 or cid == 239822769:

        msg = bot.reply_to(m, "Introduce el mensaje que quieras enviar")
        bot.register_next_step_handler(msg, step_envio)

def step_envio(m):
    global aviso
    cid = m.chat.id
    aviso = m.text

    my_file = Path('masiva/masiva.txt')


    if my_file.is_file():

        idLista = 0
        infile = open('masiva/masiva.txt', 'r')
        for line in infile:
            idListaS = line.split(' * ')[1]
            nicknameList = line.split(' * ')[2]
            numLinstaS = line.split(' * ')[0]
            idLista = int(idListaS)
            sendactionResult= bot.send_chat_action(idLista, "typing")
            #bot.send_message(cid,sendactionResult)
            if (sendactionResult==True):
                aviso=bot.send_message(idLista, aviso )
                bot.send_message(cid,aviso)
                bot.send_message(cid, str(numLinstaS) + 'usuario: ' + str(idLista) + 'nickname'+ nicknameList )
            else :
                pass
        infile.close()

    bot.send_message(idLista, "El aviso ha sido enviado correctamente" )


'''



########################################guardar en fichero





@bot.message_handler(commands=['tempo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def tempo(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    x=m.text
    nombre = ' '.join(x.split(" ")[1:])
    if not x == '/tempo' and not nombre.isdigit():
        params = { "q" : nombre, "lang" : "es", "appid" : "[Weather TOKEN]"  }
        data = requests.get("http://api.openweathermap.org/data/2.5/weather", params)
        ciudad = data.json()['name']
        tiempo = data.json()['weather'][0]['description'].capitalize()
        nubosidad = data.json()['clouds']['all']
        viento = data.json()['wind']['speed']
        temperatura = round(data.json()['main']['temp'] - 273)
        humedad = data.json()['main']['humidity']
        bot.send_message(cid, "Bienvenidos al pronostico de franky, ahora mismo nami esta luchando con luffy y está bastante ocupada no me queda otra :V. \n\nEste es el pronostico del tiempo : \n\nEn *" + ciudad + "\n*Tiempo actual: *" + tiempo + "\n*Nubosidad actual: *" + str(nubosidad) + '%' + "\n*Viento actual: *" + str(viento) + 'km/h' + "\n*Temperatura actual: *" + str(temperatura) + ' C' + "\n*Humedad actual: *" + str(humedad) + '%' + "*\n", parse_mode='markdown')




@bot.message_handler(commands=['metermanga']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_pregonado(m): # Definimos una función que resuleva lo que necesitemos.

        cid = m.chat.id
        x=m.text
        manga = ' '.join(x.split(" ")[1:])
        with open('manga/manga.txt','w') as fo:
            fo.write(manga)

@bot.message_handler(commands=['manga']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_pregonazo(m): # Definimos una función que resuleva lo que necesitemos.
        cid = m.chat.id
        with open('manga/manga.txt', 'r') as manga:
            manga = manga.read()
        bot.send_message(cid, 'Enlace del ultimo manga:\n' + manga )


@bot.message_handler(commands=['meteranime']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_pregonado(m): # Definimos una función que resuleva lo que necesitemos.

        cid = m.chat.id
        x=m.text
        anime = ' '.join(x.split(" ")[1:])
        with open('anime/anime.txt','w') as fo:
            fo.write(anime)

@bot.message_handler(commands=['anime']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_rules(m): # Definimos una función que resuleva lo que necesitemos.


        cid = m.chat.id
        with open('anime/anime.txt', 'r') as anime:
            anime = anime.read()
        bot.send_message(cid, 'Enlace del ultimo anime:\n' + anime )



@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def command_bye(m):
    cid = m.chat.id
    despedida = ""
    if (m.left_chat_member.username is None):
        nun = m.left_chat_member.first_name
        if (m.left_chat_member.last_name is not None):
            nun += " "
            nun += m.left_chat_member.last_name
        else:
            despedida = "Hasta lue "
            despedida += str(m.left_chat_member.last_name)
            despedida += " "
    else:
        nun = m.left_chat_member.username
        despedida = "Hasta lue "
        despedida += " @"

    bot.send_message(cid, str(despedida) + str(nun) + '\n\nMe parece que alguien quiere dejar la banda :V')


@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_hi(m):
    cid = m.chat.id
    cname = m.chat.title
    bienvenida = ""
    if (m.new_chat_member.username is None):
        nun = m.new_chat_member.first_name
        if (m.new_chat_member.last_name is not None):
            nun += " "
            nun += m.new_chat_member.last_name
        else:
            bienvenida = "Bienvenido a nuestra banda eres nuestro nuevo nakama "
            bienvenida += str(cname)
            bienvenida += " "
    else:
        nun = m.new_chat_member.username
        bienvenida = "Bienvenido a nuestra banda eres nuestro nuevo nakama  "
        bienvenida += str(cname)
        bienvenida += " @"

    bot.send_message(cid, str(bienvenida) + str(nun) + ' el comando /manga es para el link del ultimo manga y el comando /anime es para el ultimo anime' )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
        cid = message.chat.id

        if "#voto" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder
            x=message.text
            user = ' '
            usuario = ' '
            idUser = message.from_user.id
            idLista = ''
            estaEnLaLista = None
            numLinea = 0
            infile = open('users/votos.txt', 'r')
            for line in infile:
                numLinea = numLinea +1
                if line != "":
                    idListaS = line.split(' * ')[1]
                    idLista = int(idListaS)
                    if idUser == idLista:
                        numVotosSplit = line.split("*")[3]
                        linea = line.split("*")[0] + '*' +  line.split("*")[1] + '*' +  line.split("*")[2]
                        numVotosS = numVotosSplit.split (":")[1]
                        numVotos = int(numVotosS) +1

                        line = line.replace (numVotosS,str(numVotos))
                        sys.stdout.write(line)
                        estaEnLaLista = True
                        bot.send_message(cid,numVotosS + '         ' + str(numVotos))
            infile.close()

            if estaEnLaLista == True:

                bot.send_message(cid, 'ya estabas en la lista wap@')
            else:

                if (message.from_user.username is None):
                    user = message.from_user.first_name
                else:
                    user = '@ '+message.from_user.username
                miembroI = x.split(' ')[0]
                if miembroI == '#voto':


                    mensaje = ' '.join(x.split(" ")[1:])
                    with open('users/votos.txt','a') as fo:
                        fo.write(str(numLinea) + ' * ' + str(idUser) + ' * ' + user + ' * ' + 'votos : 1' + '\n')
                    bot.send_message(cid, 'gracias por votar ' +user)





        if message.text.lower() == "mi id":
            id = message.from_user.id
            cid = message.chat.id
            idUser = str(id)
            bot.send_message( cid, idUser)


        if message.text.lower() == "holi":
            username = message.from_user.username
            id = message.from_user.id
            cid = message.chat.id

            if id == 239822769:
                bot.send_message( cid, 'Hola mi creador 😙')

            if id == 224177651:
                bot.send_message( cid, 'Hola Kobasen que tal va el día? si necesitas algo solo dime super y yo te animo con mi baile ;)')

            if id == 264015825:
                bot.send_message( cid, 'cuando hagas un meme gracioso o que no sea copia te saludo venga katze hazle un poco de bullyng que lo necesita :)')

        if "https://twitter.com" in message.text.lower():
            username = message.from_user.username
            id = message.from_user.id
            cid = message.chat.id
            x = message.text

            if id == 264015825:
                 bot.send_message( cid, 'Oh dios mio, y ese tuit tan soberanamente currado de unos de los mejores tuiteros de One Piece de estas semanas')





        if "gracias franky" in message.text.lower():
            bot.reply_to(message, text_messages['gracias'])

        if "hola" in message.text.lower():
            username = message.from_user.username
            if (username is not None):
                bot.send_message(cid, 'Un supeeeer saludo para ti @' + username + ' :D' )

        if "adios" in message.text.lower():
            bot.reply_to(message, text_messages['adios'])

        if ":c" in message.text.lower():
            bot.reply_to(message, text_messages['llora'])
            bot.send_document( cid, open( 'gifs/cry.gif', 'rb'))

        if "buenos dias" in message.text.lower() or "buenos días" in message.text.lower():
            bot.reply_to(message, text_messages['buenosDias'])

        if "buenas tardes" in message.text.lower():
            bot.reply_to(message, text_messages['buenasTardes'])

        if "buenas noches" in message.text.lower():
            bot.reply_to(message, text_messages['buenasNoches'])



        if "franky di " in message.text.lower():
            id = message.from_user.id
            cid = message.chat.id
            if not id == 50105411:
                x=message.text
                nombre = ' '.join(x.split(" ")[2:])
                bot.send_message(cid, nombre)


        if "fiesta" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'gifs/baile.gif', 'rb'))

        if "feo" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'gifs/feo.gif', 'rb'))

        if "super" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'gifs/super.gif', 'rb'))

        #if "dick" in message.text.lower():
         #   cid = message.chat.id # Guardamos el ID de la conversación para poder responder.



          #  rnd = randrange(1, 43)

           # bot.send_photo( cid, open( 'pene/' + str(rnd) + '.jpg', 'rb'))


        if "franky mata a " in message.text.lower():
            cid = message.chat.id
            x=message.text
            nombre = ' '.join(x.split(" ")[3:])
            bot.send_message( cid, 'Vas a morir porbando mi ultimo invento rayo laser en tu culo ' + nombre + ' uajajajaja')


        #if "audio peli" in message.text.lower():
         #   cid = message.chat.id
          #  rnd = randrange(1, 53)

           # bot.send_audio( cid, open( 'peli/' + str(rnd) + '.ogg', 'rb'))

        if "audio ralph" in message.text.lower():
            cid = message.chat.id
            rnd = randrange(1, 24)
            bot.send_audio( cid, open( 'ralf/' + str(rnd) + '.ogg', 'rb'))

        if "galleta" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/galleta.ogg', 'rb'))

        if "audio chopper" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/chopper.ogg', 'rb'))

        if "cancion big mom" in message.text.lower() or "canción big mom" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/bigmom.ogg', 'rb'))

        if "cancion shake" in message.text.lower() or "canción shake" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/shake.ogg', 'rb'))


#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
