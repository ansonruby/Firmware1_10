# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
from lib.L_Tiempo import *  # importar con los mismos nombres
from lib.L_Requests import *  # importar con los mismos nombres
from M_Inf_Dispositivo import *  # importar con los mismos nombres


import threading
#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------
E_H_Get_Users_serv = 0 #estada para que se actualise por hora
#ID_Dispositivo  = GET_ID()
#ID_Dispositivo  = 'CCCB23102020b827eb529826000002'
#URL_Servidor     = 'https://plataforma.ifchile.com'
#IP_Servidor     = 'http://45plataforma.ifchile.com' #error de direccion



#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------


#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


#-----------------------------------------------------------
#----      Funciones para el manejo de usuarios   ----
#-----------------------------------------------------------
def Filtro_Caracteres(s):       # eliminar los caracteres y estructura Jason
    s = s.replace('"',"")
    s = s.replace('[',"")
    s = s.replace('{',"")
    s = s.replace(']',"")
    s = s.replace('}',"")
    s = s.replace('data:',"")
    s = s.replace(',',"\r\n")
    return s
#-----------------------------------------------------------
def Get_Usuarios_Server():#peticion de usuarios al servidor y guardado en un archivo
    global ID_Disp
    global URL_Servidor

    T_A = T_Actual()            # Tiempo()
    #print 'Inicio'
    Us_acti=  Pedir_Usuarios_Activos(URL_Servidor,T_A, ID_Disp) # U_Activos
    #T2 = T_Actual()             # Tiempo()
    #print 'Fin'
    #print 'T: ' + str(int(T2)-int(T_A))
    if Us_acti.find("Error") == -1:
        s = Us_acti
        s= Filtro_Caracteres (s)
        Escrivir_Archivos(0,s)
        Escrivir_Archivos(54,'OK') #Status finalizacion hilo
        print 'Get user OK'
        return 1

    #Escrivir_Archivos(54,'Error') #Status finalizacion hilo
    Escrivir_Archivos(54,Us_acti) #Status finalizacion hilo
    print 'Get user Error'
    return -1

def Activar_Hilos_Get_User():
    global GET_User_Server

    if GET_User_Server.isAlive() is False:
        GET_User_Server = threading.Thread(target=Get_Usuarios_Server)#, args=(0,))
        GET_User_Server.start()

#-----------------------------------------------------------
def Evento_por_hora_Usuarios_Server():
    global H_Get_Users_serv
    global E_H_Get_Users_serv

    if Hora_Actual() == H_Get_Users_serv:

        if E_H_Get_Users_serv == 0:
            E_H_Get_Users_serv = 1
            print 'Get_User por hora'
            #Get_Usuarios_Server()
            Activar_Hilos_Get_User()
    else:
        E_H_Get_Users_serv = 0

#-----------------------------------------------------------
def Evento_por_Estado_Usuarios_Server():


    if Leer_Archivo(53) == '1': #Star de Hilos Usuarios_Server
            print 'Get_User por sistema'
            Activar_Hilos_Get_User()
            Borrar_Archivo(53)

#-----------------------------------------------------------
def Eventos_Usuarios_Server():#peticion de usuarios al servidor
    Evento_por_hora_Usuarios_Server()  # solo una hora en espesifico se puede mejorar a un siclo de peticiones
    Evento_por_Estado_Usuarios_Server()




    #hora especifica #"12:10 AM"
    #peticion del sofwate por algun evento

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------
GET_User_Server   = threading.Thread(target=Get_Usuarios_Server)#, args=(0,))
#H_S_QR  = threading.Thread(target=P_Servidor_QR)#,  args=(0,))


#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------


#print 'hola agregando datos'
#while (True):
#    time.sleep(0.05)
#    Eventos_Usuarios_Server()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
