#!/usr/bin/python
import telepot, time, serial, sys, geocoder
ser = serial.Serial('/dev/ttyACM0', 9600)
g=geocoder.ip('me')
print('Bot activado.')
print('Esperando comandos...')

def handle(msg):

   userName = msg['from']['first_name']

   content_type, chat_type, chat_id = telepot.glance(msg)

   if (content_type == 'text'):
      command = msg['text']
      print ('Comando obtenido: %s' % command)

      if  '/start' in command:
         bot.sendMessage(chat_id, "Hola, "+userName+"\n"+"Mi nombre es: Risarino. Aquí la lista de comandos que puedo reconocer:"+"\n"
                                        +"/encender_led"+" -Enciendo el Led"+"\n"
                                        +"/apagar_led"+" -Apago el Led"+"\n"
                                        +"/encender_cool"+" -Enciendo el Cooler"+"\n"
                                        +"/apagar_cool"+" -Apago el Cooler"+"\n"
                                        +"/ubicacion"+" -Envio mi ubicacion actual"+"\n"
                                        +"/humedad"+" -Te muestro la Humedad en el ambiente"+"\n"
                                        +"/temperatura"+" -Te muestro la temperatura")

      elif '/encender_led' in command:
          ser.write(b'Y')
          bot.sendMessage(chat_id, "Led Encendido!")

      elif '/apagar_led' in command:
          ser.write(b'N')
          bot.sendMessage(chat_id, "Led Apagado!")

      elif '/encender_cool' in command:
          ser.write(b'P')
          bot.sendMessage(chat_id, "Cooler Encendido!")

      elif '/apagar_cool' in command:
          ser.write(b'A')
          bot.sendMessage(chat_id, "Cooler Apagado!")

      elif '/ubicacion' in command:
          bot.sendLocation(chat_id, str(g.latlng[0]),str(g.latlng[1]))

      elif '/temperatura' in command:
          ser.write(b'T')
          linea=ser.readline()
          bot.sendMessage(chat_id, 'Temperatura (ºC): ' + str(linea.decode()))

      elif '/humedad' in command:
          ser.write(b'H')
          linea=ser.readline()
          bot.sendMessage(chat_id, 'Humedad Relativa (%): ' +str(linea.decode()))

      elif '/llama' in command:
          ser.write(b'F')
          linea = ser.readline()
          bot.sendMessage(chat_id, linea)
      else:
          bot.sendMessage(chat_id, "Lo siento, no reconozco ese comando!")

bot = telepot.Bot('945939373:AAEy9JPN7i2IhJJIUA-CATLMuqsT217OF3g')
#bot = telepot.Bot('1005860483:AAF6HXyGqGYsq6gOpUQlKPMPeWdIt3RzpW4')
bot.message_loop(handle)

# Espera por nuevos mensajes
while 1:
   time.sleep(500)
