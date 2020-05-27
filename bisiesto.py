import turtle #paso previo a pygame
import winsound
import os
import time
from main import directory_path as audio_path

winsound.PlaySound(audio_path + '\\pong_intro.wav', winsound.SND_FILENAME)
############### variables ###############
width_screen = 800
height_screen = 600

while True:
  ########### window object ################
  window = turtle.Screen() # objeto ventana
  window.title("Será Bisiesto?") # crea titulo 
  window.bgcolor('#ffa123') # color de fondo
  window.setup(width = width_screen, height = height_screen) # tamaño ventana
  window.tracer(0) # evita que se actualice la ventana
  #########################################

  year = int(window.textinput('Suspenso...', 'INGRESE UN AÑO'))

  ############ pen object #################
  pen = turtle.Turtle()
  pen.speed(0)
  pen.color('#f12500')
  pen.penup() # asi no escribe mientras se mueve
  pen.hideturtle() # objeto invisible
  pen.goto(0, (height_screen/14) * 2) # coordenada x del cartel
  pen.write('{}'.format(year), align='center', font=('Arial', 24, 'normal')) 

  time.sleep(1)
  window.update()
  pen.clear()
  pen.write('CALCULANDO RESULTADO...', align='center', font=('Arial', 24, 'normal'))
  window.update()

  ######################### algotirmo #############################

  bisiesto = False

  if year % 4 == 0:
    if year % 100 == 0:
      bisiesto = year % 400 == 0
    else:
      bisiesto = True


  if bisiesto:
    result_message = 'Es bisiesto'
  else:
    result_message = 'No es bisiesto'

  #################################################################

  time.sleep(2)

  pen.clear()
  pen.write('{}'.format(year), align='center', font=('Arial', 24, 'normal')) 

  ########### result objetc ###############

  result = turtle.Turtle()
  result.speed(0)
  result.color('#118800')
  result.penup()
  result.hideturtle()
  result.goto(0, 0)
  result.write('{}'.format(result_message), align='center', font=('Arial', 24, 'normal')) 


  window.update()
  time.sleep(2)

  escape = window.textinput('Responde si o no', 'Otra pregunta?')


  if escape == 'no':
    break
  result.clear()
  pen.clear()