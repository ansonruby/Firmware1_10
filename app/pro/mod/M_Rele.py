# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
from lib.Configuracion import *  # importar con los mismos nombres
#from lib.L_Tiempo import *  # importar con los mismos nombres
#from lib.L_Archivos import *  # importar con los mismos nombres
#from M_Inf_Dispositivo import *  # importar con los mismos nombres
#import time
#import RPi.GPIO as GPIO #Libreria Python GPIO
#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------
#        Entrada, Salida de los relevos
#Rele =   [37,38]        #16, 19 #[21,23]
#Tiempo_Torniquete = 2   #tiempo de duracion de los relevos

#ID_Dispositivo_R  = GET_ID()
#ID_Dispositivo_R  = 'CCCB23102020b827eb529826000002'
#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


#-----------------------------------------------------------
#----      Funciones para el manejo de los relevos     ----
#-----------------------------------------------------------
def Actividad_Rele(Direccion):
    global Rele
    Tiempo_Torniquete =int(Leer_Archivo(30))
    GPIO.output(Rele[Direccion], GPIO.LOW)
    time.sleep(Tiempo_Torniquete)
    GPIO.output(Rele[Direccion], GPIO.HIGH)

#-----------------------------------------------------------
def Comando_Rele(Direccion):
    Tiempo_Torniquete =int(Leer_Archivo(30))
    Borrar_Archivo(38)
    if Direccion == 0:      Escrivir_Archivos(38,"¿00000004000" + str(Tiempo_Torniquete) + "?") #Entrar
    elif Direccion == 1:    Escrivir_Archivos(38,"¿00000004010" + str(Tiempo_Torniquete) + "?") #Salir
    elif Direccion == 2:    Escrivir_Archivos(38,"¿000000040300?")                              #Cerrar

#-----------------------------------------------------------
def Entrar():
    global ID_Disp
    if ID_Disp.find("CCCB") != -1:  Comando_Rele(0)       #Para dispositivos CCCB
    else:                           Actividad_Rele(0)     #Para dispositivos con relevos

#-----------------------------------------------------------
def Salir():
    global ID_Disp
    if ID_Disp.find("CCCB") != -1:  Comando_Rele(1)       #Para dispositivos CCCB
    else:                           Actividad_Rele(1)     #Para dispositivos con relevos

#-----------------------------------------------------------
def Cerrado():
    global ID_Disp
    if ID_Disp.find("CCCB") != -1: Comando_Rele(2)       #Para dispositivos CCCB
    else:                          Cerrado_Pin()         #Para cerrar pines
#-----------------------------------------------------------
def Direcion_Rele(Res):
    Direc = Leer_Archivo(13)  # Direccion_Torniquete
    if Res == 'Access granted-E':
        if Direc == 'D': Salir()
        else :           Entrar()
    elif Res == 'Access granted-S':
        if Direc == 'D': Entrar()
        else :           Salir()

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
