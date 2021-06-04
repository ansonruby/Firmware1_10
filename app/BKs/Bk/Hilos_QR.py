
import lib.Control_Archivos
import lib.Control_Ethernet

import threading
import time


Leer_Estado             = lib.Control_Archivos.Leer_Estado
Borrar                  = lib.Control_Archivos.Borrar_Archivo

Envio                   = lib.Control_Ethernet.envio



def T_Actual():
	return str(int(time.time()*1000.0))

def Leer_Archivo(a):

    #arch = Get_archivo(a)
    arch = a #"Tabla.txt"
    f = open (arch,'r')
    mensaje = f.read()
    #print(mensaje)
    f.close()
    return mensaje

def Borrar_Archivo(a):

    #arch = Get_archivo(a)
    #print arch
    arch = a #"Tabla.txt"
    archivo = open(arch, "w")
    archivo.write("")
    archivo.close()

def Escrivir_Archivos(a, Texto):

    #arch = Get_archivo(a)
    arch = a #"Tabla.txt"
    archivo = open(arch, "w")
    #print(archivo.tell())
    archivo.write(Texto)
    #print(archivo.tell())
    archivo.close()

def Leer_Linea(archivo, Numero):

    arch = archivo #"Tabla.txt"
    f = open (arch,'r')
	#archivo.seek(0)
    lineas = f.readlines()
    f.close()
	#for linea in archivo.readlines():

    return lineas[Numero-1] # revisar si comensar en 1 o 0

def Eliminar_Linea(archivo, Numero):
    arch = archivo #"Tabla.txt"
    f = open (arch,'r')
    lineas = f.readlines()
    f.close()

    lineas.pop(Numero-1)

    #print lineas
    f2 =open(arch, "w")
    f2.write(''.join(lineas) )
    f2.close()

def Modificar_Linea(archivo, Numero, Dato): #incluir el/n

    arch = archivo #"Tabla.txt"
    f = open (arch,'r')
    lineas = f.readlines()
    f.close()

    #lineas.pop(Numero-1)
    lineas[Numero-1]= Dato

    #print lineas
    f2 =open(arch, "w")
    f2.write(''.join(lineas) )
    f2.close()


def Add_Linea_fin(archivo, Dato): #incluir el/n

    arch = archivo #"Tabla.txt"
    f = open (arch,'r')
    lineas = f.readlines()
    f.close()

    #lineas.pop(Numero-1)
    #lineas[Numero-1]= Dato

    #print lineas
    f2 =open(arch, "w")
    f2.write(''.join(lineas) )
    f2.write(Dato)
    f2.close()

def Add_Linea_posicion(archivo, Numero, Dato): #incluir el/n

    arch = archivo #"Tabla.txt"
    f = open (arch,'r')
    lineas = f.readlines()
    f.close()

    inicio = lineas[0:(Numero-1)]
    fin = lineas[(Numero-1):]

    f2 =open(arch, "w")
    f2.write(''.join(inicio) )
    f2.write(Dato)
    f2.write(''.join(fin) )
    f2.close()

def Numero_lineas(archivo):
    arch = archivo #"Tabla.txt"
    f = open (arch,'r')
    lineas = f.readlines()
    f.close()
    return len(lineas)



#correo@gmail.# COMBAK: anderson amaya app_Actualizando
#--------------------------------------------
#               hilos
#--------------------------------------------
def Verificar_ID(Pal): #mejorar por que podia pasa cualquiera
	#global N_A_Servidor

	archivo = open('/home/pi/Firmware/db/Data/Tabla_Servidor.txt', 'r')
	archivo.seek(0)
	for linea in archivo.readlines():
		s=linea.rstrip('\n')
		s=s.rstrip('\r')
		s2 =s.partition(".")
		#print 'ID: '+ s2[0] + ' RUT: '+s2[2]
		Rut = s2[0]
		if 	Rut ==	Pal:
			archivo.close()
			return s2[0]
	archivo.close()
	return -1

def Verificar_acceso(ID1): #mejorar por que podia pasa cualquiera
	#global	N_A_Lector
	Contador=0
	archivo = open('/home/pi/Firmware/db/Data/Tabla_Lector.txt', 'r')
	archivo.seek(0)
	for linea in archivo.readlines():
		s=linea.rstrip('\n')
		s2 =s.partition(".")
		s3 = s2[2].partition(".")
		#print 'QR: '+ s2[0] + ' ID: '+s3[0]
		ID2 = s3[0]
		if 	ID2 ==	ID1:
			Contador +=1
	archivo.close()
	return Contador


def P_Servidor_QR(T_A):
	#T_A = T_Actual()
	R_Q=Leer_Estado(7)
	s =R_Q.partition(".")
	QRT = s[0]
	IDQ = s[2]

	Envio_Dato = QRT
	Estado_RQ = 1
	#Dato2 = R_Q
	#Dato1 = ''

	Respuesta=Envio(Envio_Dato,T_A, Estado_RQ)
	#print R_Q
	#print Envio_Dato
	#print T_A
	#print Estado_RQ
	T2 = T_Actual()
	#print 'inicio: ' +T_A
	#print 'Fin: ' +T2
	print 'R: ' + Respuesta + ', T: ' + str(int(T2)-int(T_A))
	Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Exit_Dispositivos_QR.txt",'1')

	#return Respuesta



#-------- funcion Hilo para autorizar Usuario con el dispositivo por qr-----
def Dispsotivo_QR(T_A):

	Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Exit_Dispositivos_QR.txt",'0')
	Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Status_Dispositivos_QR.txt", '1')
	#T_A = T_Actual()
	Respuesta = 'Denegado'
	N_veri = 0

	R_Q=Leer_Estado(7)
	s =R_Q.split(".")
	QRT = s[0]
	IDQ = s[1]
	#print IDQ

	if Leer_Archivo("/home/pi/Firmware/db/Hilos/QR/Exit_Dispositivos_QR.txt") != '1':

		ID_1 = Verificar_ID(IDQ)
		if ID_1 != -1:
			N_veri = Verificar_acceso(ID_1)

		if Leer_Archivo("/home/pi/Firmware/db/Hilos/QR/Exit_Dispositivos_QR.txt") != '1':

			if N_veri != 0:
				if N_veri % 2 == 0	:	N_veri = 1 # Entrar
				else				:	N_veri = 2 # Salir

			if ID_1 == -1 and  N_veri == 0:					Respuesta =  'Denegado'		 #print 'NO existe'
			if ID_1 != -1 and  N_veri == 0 or N_veri == 1:	Respuesta =  'Access granted-E'#print 'Entrada'
			if ID_1 != -1 and  N_veri == 2:					Respuesta =  'Access granted-S'#print 'Salida'

			T2 = T_Actual()
			print 'R: ' + Respuesta + ', T: ' + str(int(T2)-int(T_A))
			Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Out_Dispositivos_QR.txt",Respuesta)
			Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Status_Dispositivos_QR.txt", '2')

		else:
			print 'Terminar Hilo'
			Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Out_Dispositivos_QR.txt",Respuesta)
			Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Status_Dispositivos_QR.txt", '3')
	else:
		print 'Terminar Hilo'
		Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Out_Dispositivos_QR.txt",Respuesta)
		Escrivir_Archivos("/home/pi/Firmware/db/Hilos/QR/Status_Dispositivos_QR.txt", '3')









H_D_QR   = threading.Thread(target=Dispsotivo_QR, args=(0,))
H_S_QR  = threading.Thread(target=P_Servidor_QR,  args=(0,))

print 'listos'
while 1:
	#------------------if PP_Mensajes:---------------------------------------
	#  Proceso 0: Tiempo de espera para disminuir proceso
	#---------------------------------------------------------
	time.sleep(0.05)
	#print '---'
	#---------------------------------------------------------
	# Proceso 4: Procesamiento del QR
	#---------------------------------------------------------
	if Leer_Estado(8) == '1':   # Hay un QR sin procesar
		T_A = T_Actual()
		print '------ QR ---- '

		"""
		#print '--------------------'
		T1 = T_Actual()

		print Dispsotivo_QR()
		print P_Servidor_QR()

		T2 = T_Actual()

		#print '--------------------'
		#print 'Fin'
		#print T1
		#print T2
		#print 'diferencia ejecucion:'
		print 'Tiempo Ejecucion:'+str(int(T2)-int(T1))
		Borrar(8)



		"""
		"""
		if H_D_QR.isAlive() is False:
			#hilo1 = threading.Thread(target=test1,name='test1')
			H_D_QR = threading.Thread(target=Dispsotivo_QR, args=(T_A,))
			H_D_QR.start()
		"""

		if H_S_QR.isAlive() is False:
			H_S_QR  = threading.Thread(target=P_Servidor_QR, args=(T_A,))
			#hilo1 = threading.Thread(target=test1,name='test1')
			#hilo1 = threading.Thread(target=contar)
			H_S_QR.start()

		Borrar(8)               #final del procesos
