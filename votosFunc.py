import os
import re
import sys
import json

def crearVoto (idGrupo, idMensaje, descripcion):
  file_path = "app/votos/"+str(idGrupo)+".json"
  directory = os.path.dirname(file_path)
  meterVoto = {'descripcion': descripcion, 'idMensaje': idMensaje, 'votos':[]}
  if not os.path.exists(directory):
    os.makedirs(directory)
  if os.path.isfile(file_path):
    with open(file_path, "r") as jsonFile:
      data = json.load(jsonFile)
    data.append(meterVoto)
    with open(file_path, "w") as outfile:
      json.dump(data, outfile, indent=4)
  else:
    with open(file_path, "w") as outfile:
      json.dump([meterVoto], outfile, indent=4)


def actualizarVoto(idGrupo, idMensaje, puntuacion, nomUsuario, idUsuario):
  file_path = "app/votos/"+str(idGrupo)+".json"
  with open(file_path, "r+") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMensaje') == int(idMensaje):
      votos = x.get('votos')
      ids = [y.get('idUsuario') for y in votos] if votos else []
      borrarUsu = {}
      if idUsuario in ids:
        for y in votos:
          if int(idUsuario) == int(y.get('idUsuario')):
            borrarUsu = y
        if borrarUsu:
          votos.remove(borrarUsu)
      else:
        votos.append({
          'idUsuario':idUsuario,
          'puntuacion':puntuacion,
          'nomUsuario':nomUsuario
        })
        x['votos'] = votos
  with open(file_path, "w") as outfile:
    json.dump(data, outfile, indent=4)


def getNuevoTexto(idGrupo, idMensaje):
  file_path = "app/votos/"+str(idGrupo)+".json"
  with open(file_path, "r+") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMensaje') == int(idMensaje):
      texto = "Votad {} del 0 al 10.\n*Puntos*: {}\n*Votantes*: {}\n*Nota*: {}"
      votos = x.get('votos')
      descripcion = x.get('descripcion')
      puntos = 0
      votantes = 0
      nota = 0
      if votos:
        for x in votos:
            mycnt = int(x['puntuacion'])
            puntos += mycnt

        votantes = len(votos)
        nota = puntos/votantes
      texto = texto.format(descripcion, puntos, votantes, nota)

      texto = "Votad *" + descripcion + "* del 1 al 10.\n*Puntos*: " + str(puntos) + "\n*Votos*: " + str(votantes) + "\n*Nota*: " + str(nota)
      return texto



def guardarOfertaNueva(idGrupo, idMessage, nombreUsuario, idUsuario, carta):
  file_path = "app/votos/"+str(idGrupo)+".json"
  with open(file_path, "r+") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMessage') == int(idMessage): # Buscamos el tradeo
      ofertas = x.get('ofertas_gente')# Obtenemos sus ofertas
      ids = [y.get('idUsuario') for y in ofertas] if ofertas else []
      borrarUsu = {}
      if idUsuario in ids:
        for y in ofertas: # Recorremos la ofertas
          if int(idUsuario) == int(y.get('idUsuario')): # Si el usuario ya ha ofrecido algo
            if carta not in y.get('cartas'):
              y['cartas'].append(carta)
            else:
              y['cartas'].remove(carta)
            if not y.get('cartas'):
              borrarUsu = y
        if borrarUsu:
          ofertas.remove(borrarUsu)
      else:
        ofertas.append({
            'nombreUsuario': nombreUsuario,
            'cartas':[carta],
            'idUsuario': int(idUsuario)
        })
      x['ofertas_gente'] = ofertas
  with open(file_path, "w") as outfile:
    json.dump(data, outfile, indent=4)


def getUsuarioPeticion(idGrupo, idUsuario, idMessage):
  file_path = "app/votos/"+str(idGrupo)+".json"
  with open(file_path, "r+") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMessage') == int(idMessage) and x.get('idCreador') == int(idUsuario):
      return x.get('nombreCreador'), x.get('pide')


def addOferta(idGrupo,idUsuario,nombreCarta):
  file_path = "app/votos/"+str(idGrupo)+".json"
  with open(file_path, "r+") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMessage') == 0 and x.get('idCreador') == idUsuario:
      x["ofrece"] = [y.strip() for y in nombreCarta.split(',')]

  with open(file_path, "w") as outfile:
    json.dump(data, outfile, indent=4)



def addPeticion(idGrupo,idUsuario,peticion):
  file_path = "app/votos/"+str(idGrupo)+".json"
  directory = os.path.dirname(file_path)

  with open(file_path, "r+") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMessage') == 0 and x.get('idCreador') == idUsuario:
      x["pide"] = peticion

  with open(file_path, "w") as outfile:
      json.dump(data, outfile, indent=4)


def leerDatos(idGrupo,idUsuario,idMessage):
  file_path = "app/votos/"+str(idGrupo)+".json"
  with open(file_path, "r") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMessage') == int(idMessage) and x.get('idCreador') == int(idUsuario):
      peticion = x['pide']
      oferta = x['ofrece']

  return peticion,oferta



def cambiarIdMensaje(idGrupo, idUsuario, idMessage):

  file_path = "app/votos/"+str(idGrupo)+".json"

  with open(file_path, "r") as jsonFile:
    data = json.load(jsonFile)
  for x in data:
    if x.get('idMessage') == 0 and x.get('idCreador') == idUsuario:
      x['idMessage'] = idMessage

  with open(file_path, "w") as outfile:
    json.dump(data, outfile, indent=4)

#crearTradeo(idGrupo,idMessage)

#addOferta(idGrupo,idMessage,nombreCarta)

#addPeticion(idGrupo,idMessage,peticion)

#cambiarIdMensaje(idMessage)

#datos = leerDatos(idGrupo,idMessage)

#print(datos)
