
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------

from lib.L_Archivos import *  # importar con los mismos nombres
import serial
from serial import SerialException

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

PP_MensajesQR = 0         # 0: NO print  1: Print
Puerto_Serial = '/dev/ttyS0'

#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------

port = serial.Serial(Puerto_Serial, baudrate=9600, timeout=1)
GF=''
GI=''
M_QR=''  #depronto se nesesite una memoria de lista de dos pociciones para procesar despues o revizar

#-----------------------------------------------------------
#----      Funciones para el manejo del sensor QR     ----
#-----------------------------------------------------------
def Convertir_listado( RX_Serial):
    return RX_Serial.split('\r')
#-----------------------------------------------------------
def Armado_de_QR_Valido(RX_Serial):

    global GF
    global GI
    global M_QR

    Inicio = RX_Serial.find("<")
    Fin = RX_Serial.find(">")
    Cantidad = len(RX_Serial)
    Tramas= RX_Serial.find('\r')
    Bandera = 0

    if (Inicio != -1 ) and (Fin != -1):
        M_QR = RX_Serial[(Inicio+1):(Fin)]
        Bandera = 1                         #print "QR_F : " + M_QR
    elif (Inicio != -1 ) and (Fin == -1):
        GI = RX_Serial[(Inicio+1):]
        Bandera = -1                        #print "Guardar Inicio: " + GI
    elif (Inicio == -1 ) and (Fin != -1):
        GF = RX_Serial[0:(Fin)]           #print "Guardar Fin: " + GF
        M_QR = GI + GF
        Bandera = 1                         #print "QR_F T: " + M_QR
    elif (Inicio == -1 ) and (Fin == -1):
        if RX_Serial.find("Igual") != -1:
            Bandera = 3                     #print "QR_F Igual: " + M_QR
        else:
            M_QR = RX_Serial
            Bandera = 2                     #print "X    : " + M_QR

    if Bandera != -1:   return Bandera, M_QR
    else:               return Bandera, ""

#-----------------------------------------------------------
def Recibir_Cadenas(RX_Serial):

    Numero_Caracteres = len(RX_Serial)
    if Numero_Caracteres >= 1:
        status, QR = Armado_de_QR_Valido(RX_Serial)
        #print str(status) +': '+ QR
        if status == 1: # Nuevo QR para Procesar ------------------------
            if PP_MensajesQR == 1:
                print 'N_QR: '+ QR #print "Nuevo QR fusepong"
            Borrar_Archivo(7)                 # Borrar QR
            Escrivir_Archivos(7, QR)           # Guardar QR
            Escrivir_Archivos(8, '1')          # Cambiar estado del QR
        if status == 3: # QR ya leido -----------------------------------
            if PP_MensajesQR == 1:
                print 'L_QR: '+ QR #print "QR Igual"
            #Escrivir_Archivos('2',11)        # Estado QR repetido
            if QR.count(".") == 3:            # para procesar QR invitado
                Escrivir_Archivos(8, '1')      # Cambiar estado del QR
            else:
                Escrivir_Archivos(11, '2')     # Estado QR repetido
        if status == 2: # QR NO valido -------------------------
            if PP_MensajesQR == 1:
                print 'X   : '+ QR #print "NO es un QR"
            Borrar_Archivo(7)                 # Borrar QR
            Escrivir_Archivos(7, QR)           # Guardar QR
            Escrivir_Archivos(8, '1')          # Cambiar estado del QR

#-----------------------------------------------------------
def Lectura_Serial():

    global port

    while True:
        try :

            #-------------------------------
            #Para dispotitos CCCB
            #-------------------------------
            rele = Leer_Archivo(38)
            if len(rele)>= 1:
                #print rele
                port.write(rele)
                Borrar_Archivo(38)
            #-------------------------------

            Recibir_Cadenas(port.read(250))
        except SerialException: #   Reiniciar el serial
            while True:
                port = serial.Serial(Puerto_Serial, baudrate=9600, timeout=1)
                break

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
#M_QR = Leer_Archivo(7)
#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
#print 'Listo'
#Lectura_Serial()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
# Lectura_Serial()
# Recibir_Cadenas(RX_Serial):
# Armado_de_QR_Valido(RX_Serial):
# Convertir_listado( RX_Serial):
