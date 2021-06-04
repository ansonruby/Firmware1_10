# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
from lib.L_Tiempo import *  # importar con los mismos nombres
from lib.L_Requests import *  # importar con los mismos nombres
from M_Inf_Dispositivo import *  # importar con los mismos nombres
from M_Rele import *  # importar con los mismos nombres

import threading
#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


#-----------------------------------------------------------
#----      Funciones para el manejo del buzzer     ----
#-----------------------------------------------------------


def Decision_Torniquete (Res, QR, ID2, Ti,Qr_Te, I_N_S ):

    global Estados
    Direc_Torniquete = Leer_Archivo(13)  # Direccion_Torniquete

    Co = QR+'.'             #QR
    Res=Res.rstrip('\n')    #limpiar respuesta
    Res=Res.rstrip('\r')
    #Direccion LED falta diseñar
    Direcion_Rele(Res)      #Activacion de relevos "Proceso bloqueante" Hilo?

    #guardar deciones de Entrada y Salida
    if Res == 'Access granted-E':
        print Co+Ti+'.'+Qr_Te+'.0.'+I_N_S
        Add_Linea_fin(1, Co+Ti+'.'+Qr_Te+'.0.'+I_N_S+'\n')
    elif Res == 'Access granted-S':
        print Co+Ti+'.'+Qr_Te+'.1.'+I_N_S
        Add_Linea_fin(1,Co+Ti+'.'+Qr_Te+'.1.'+I_N_S+'\n')
    else :
        print "Sin Acceso o rut equivocado estado 5 0 6"

    #Escrivir(Co+Ti+'.'+Qr_Te+'.0.'+I_N_S)               #guardar un registro
    #Escrivir_Archivo(Co+Ti+'.'+Qr_Te+'.0.'+I_N_S, 22)   #Para dispotivos asociados



#-----------------------------------------------------------
def Get_QR():
    Pal=Leer_Archivo(7)
    Pal=Pal.rstrip('\n')
    Pal=Pal.rstrip('\r')
    return Pal

#-----------------------------------------------------------
def P_Servidor_QR():            # Hilo principal
    global ID_Disp
    global URL_Servidor
    T_A = T_Actual()
    QRT = Get_QR()
    R_Q = (QRT).split('.')
    QR = R_Q[0]
    #print QR
    Respuesta = Enviar_QR(URL_Servidor, T_A, ID_Disp, QR)
    print 'RS: ' + Respuesta #+ ', T: ' + str(int(T2)-int(T_A))
    Escrivir_Archivos(48,'1')
    #return Respuesta
    print 'Decision_Torniquete'
    Decision_Torniquete (Respuesta, QRT, "", T_A, '1','0')  #Respuesta_Con_Internet


#-----------------------------------------------------------
def P_Dispositivo_QR():
        
    Escrivir_Archivos(48,'0')
    Escrivir_Archivos(49, '1')

    R_Q = (Get_QR()).split('.')
    QR = R_Q[0]
    IDQ = R_Q[1]

    Respuesta = 'Denegado'
    N_veri = 0

    if Leer_Archivo(48) != '1':

        ID_1 = Verificar_ID(IDQ)
        if ID_1 != -1:
            N_veri = Verificar_acceso(ID_1)

        if Leer_Archivo(48) != '1':

            if N_veri != 0:
                if N_veri % 2 == 0	:	N_veri = 1 # Entrar
                else				:	N_veri = 2 # Salir

            if ID_1 == -1 and  N_veri == 0:					Respuesta =  'Denegado'		 #print 'NO existe'
            if ID_1 != -1 and  N_veri == 0 or N_veri == 1:	Respuesta =  'Access granted-E'#print 'Entrada'
            if ID_1 != -1 and  N_veri == 2:					Respuesta =  'Access granted-S'#print 'Salida'

            print 'RD: ' + Respuesta
            Escrivir_Archivos(50,Respuesta)
            Escrivir_Archivos(49, '2')

        else:
            #print 'Terminar Hilo'
            print 'RD: ' + Respuesta
            Escrivir_Archivos(50,Respuesta)
            Escrivir_Archivos(49, '3')
    else:
        #print 'Terminar Hilo'
        print 'RD: ' + Respuesta
        Escrivir_Archivos(50,Respuesta)
        Escrivir_Archivos(49, '3')

#-----------------------------------------------------------
def Activar_Hilos_Procesar_QR():
    global H_D_QR
    global H_S_QR

    if H_D_QR.isAlive() is False:
        H_D_QR = threading.Thread(target=P_Dispositivo_QR)#, args=(0,))
        H_D_QR.start()
    if H_S_QR.isAlive() is False:
        H_S_QR  = threading.Thread(target=P_Servidor_QR)#, args=(0,))
        H_S_QR.start()

#-----------------------------------------------------------
def Procesar_QR():
    if Leer_Archivo(8) == '1':   # Hay un QR sin procesar
        print '------ QR ---- '
        Activar_Hilos_Procesar_QR()
        Borrar_Archivo(8)               #final del procesos


#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
H_D_QR   = threading.Thread(target=P_Dispositivo_QR)#, args=(0,))
H_S_QR  = threading.Thread(target=P_Servidor_QR)#,  args=(0,))


#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------

#print Leer_Archivo(29)
#sonido(Tiempo_sonido)
#while (True):
#    time.sleep(0.05)
#    Control_Sonidos_Por_Archivo()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
