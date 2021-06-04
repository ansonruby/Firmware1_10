#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
from lib.Configuracion import *  # importar con los mismos nombres
#from lib.L_Archivos import *  # importar con los mismos nombres
#import time, commands

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
#----      Funciones para la informacion del dispositivo  --
#-----------------------------------------------------------
def GET_Firmware():
    Firmware = ((Leer_Linea(29, 1)).replace("\n","")).replace("\r","")
    return Firmware.replace("# ","")     # version firmware

#-----------------------------------------------------------
def GET_Vercion():
    Firmware = ((Leer_Linea(17, 1)).replace("\n","")).replace("\r","")
    return Firmware.replace("# ","")     # version firmware

#-----------------------------------------------------------
def GET_IPS():
    IPs = commands.getoutput('hostname -I')
    return IPs.split(' ')

#-----------------------------------------------------------
def GET_Nombre():
    return commands.getoutput('hostname')

#-----------------------------------------------------------
def GET_Inf():
    Inf = '              '
    Inf += GET_Firmware()+'\n'
    Inf += GET_Vercion()+'\n'
    Inf +='              Nombre\n'
    Inf += GET_Nombre()+'\n'
    Inf +='              Serial\n'
    Inf += GET_ID(1)+'\n'
    Inf +='              Conexion\n'
    IPS = GET_IPS()

    for linea in IPS:
        if len(linea)>=3:
            Inf +='IP: '
            Inf +=linea
            Inf +='\n'
    return Inf
#-----------------------------------------------------------
def Estatus_Coneccion (c):
        res2 = commands.getoutput('cat /sys/class/net/'+c+'/carrier')
        if res2 == '0':     return 0 #  print 'Desconectado'
        else:               return 1 # print 'Conectado'
#-----------------------------------------------------------
def GET_STatus_Red():
        Sres = ""
        Cantidad =0
        res = commands.getoutput('ls /sys/class/net/')
        redes =res.split("\n")

        for x1 in range(len(redes)):
                c= redes[x1]
                #print c
                if c.find('eth') != -1: #print 'ethernet'
                        if Estatus_Coneccion (c) == 0:  #print 'ED'
                            Sres = Sres + 'ED'
                            Cantidad+=1
                        else:                           #print 'EC'
                            Sres = Sres + 'EC'
                            Cantidad+=1
                if c.find('wlan') != -1: #print 'Wifi'

                        if Estatus_Coneccion (c) == 0:  #print 'WD'
                                Sres = Sres + 'WD'
                                Cantidad+=1
                        else:                           #print 'WC'
                                Sres = Sres + 'WC'
                                Cantidad+=1
        #print str(Cantidad) + Sres
        return  str(Cantidad) + Sres

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
#print Leer_Archivo(17)
#print Get_MAC()
#print GET_ID()
#print GET_ID(1)
#print GET_Firmware()
#print GET_Vercion()
#print GET_IPS()
#print GET_Nombre()
#print GET_Inf()
#print GET_STatus_Red()

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------
