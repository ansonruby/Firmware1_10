
import threading
import time


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

def Escrivir_Archivos(Texto, a):

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





inicio  =   1
fin     =   0
contador =  0

def hilo_Contador():
	contador = 0
	print 'Hilo'
	while 1:
		time.sleep(0.05)
		#print 'leer archivo'
		Pal = Leer_Archivo("Statushilo1.txt")
		if Pal.find('0') != -1:
			#print '---'contador = 0
			Escrivir_Archivos('1', "Statushilo1.txt") #ejecutando
		else:
			#print 'sdfsd'
			contador+=1
			if contador >=500:
				contador= 500
				Escrivir_Archivos('2', "Statushilo1.txt") # fin

		#print str(threading.current_thread().getName()) + 'Contador: '+ str(contador) + '\n'



def contar():
    contador = 0
    while contador<5:
        contador+=1
        print str(threading.current_thread().getName()) + 'Contador: '+ str(contador) + '\n'

def contar2():
    contador = 0
    while contador<10:
        contador+=2
        print str(threading.current_thread().getName()) + 'Contador: '+ str(contador) + '\n'

hilo1 = threading.Thread(target=contar)
hilo2 = threading.Thread(target=contar)
hilo3 = threading.Thread(target=contar2)

hilo4 = threading.Thread(target=hilo_Contador)


#hilo2.start()
#hilo3.start()

#hilo4.start()

while 1:

	#time.sleep(0.05)
	time.sleep(0.05)
	print 'Inicio\n'
	#print '-------\n'
	if hilo1.isAlive() is False:
        #hilo1 = threading.Thread(target=test1,name='test1')
		hilo1 = threading.Thread(target=contar)
		hilo1.start()


	"""
	Pal = Leer_Archivo("Statushilo1.txt")
	print 'Estado: '+ Pal
	if Pal.find('2') != -1:
		#print '---'
    	contador = 0
    	Escrivir_Archivos('0', "Statushilo1.txt") #ejecutando
	"""




























"""
# Librerias creadas para multi procesos o hilos -------------
import time

# definiciones para el aplicativo principal -----------------

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




#Leer_Linea(archivo, Numero):
#Eliminar_Linea("Tabla.txt", 12)
#Modificar_Linea("Tabla.txt", 180, 'g2yd1.8e494d978f923f6e66beaf1905a747e8888\n')
#Eliminar_Linea("Tabla.txt", 183)
#Add_Linea_fin("Tabla.txt", 'g2yd1123.32345566e68\n')
#Add_Linea_posicion("Tabla.txt", 4, 'g2yd1.8e494d978f923f6e66beaf1905a747e8888\n')


while 1:
    time.sleep(0.05)
    #print 'Inicio'
    #print '--------------------'
    T1 = T_Actual()



    #Texto=Leer_Archivo("Tabla.txt")
    #print Texto
    #print Leer_Archivo("Tabla.txt")

    #print Leer_Linea("Tabla.txt",5)
    #linea = Leer_Linea("Tabla.txt",183)
    #print Leer_Linea("Tabla.txt",183)
    #Eliminar_Linea("Tabla.txt", 183)
    #Add_Linea_fin("Tabla.txt", 'g2yd1123.32345566e68\n')
    #Add_Linea_posicion("Tabla.txt", 4, 'g2yd1.8e494d978f923f6e66beaf1905a747e8888\n')
    Numero_lineas("Tabla.txt")



    T2 = T_Actual()

    #print '--------------------'
    #print 'Fin'
    #print T1
    #print T2
    #print 'diferencia ejecucion:'
    print 'Tiempo Ejecucion:'+str(int(T2)-int(T1))

    #modificarLinea("archivo.txt","casa","avion")

"""







"""
# Librerias creadas para multi procesos o hilos -------------

import lib.Control_Archivos


# definiciones para el aplicativo principal -----------------

Leer_Archivo            = lib.Control_Archivos.Leer_Archivo
Leer_Estado             = lib.Control_Archivos.Leer_Estado
Borrar                  = lib.Control_Archivos.Borrar_Archivo
Escrivir_Estados        = lib.Control_Archivos.Escrivir_Estados
ID                      = lib.Control_Archivos.ID
Estado_Usuario 	        = lib.Control_Archivos.Estado_Usuario
Escrivir_Enviar         = lib.Control_Archivos.Escrivir_Enviar
Escrivir                = lib.Control_Archivos.Escrivir
Escrivir_nuevo          = lib.Control_Archivos.Escrivir_nuevo
Leer                    = lib.Control_Archivos.Leer
Escrivir_Archivo        = lib.Control_Archivos.Escrivir_Archivo
Verificar_PIN           = lib.Control_Archivos.Verificar_PIN
PIN_Usado               = lib.Control_Archivos.PIN_Usado


import time


while 1:
    #------------------if PP_Mensajes:---------------------------------------
    #  Proceso 0: Tiempo de espera para disminuir proceso
    #---------------------------------------------------------
    time.sleep(0.05)
    #---------------------------------------------------------
    # Proceso 4: Procesamiento del QR
    #---------------------------------------------------------
    if Leer_Estado(8) == '1':   # Hay un QR sin procesar
        #Decision('QR')

        print "QR"
        Borrar(8)               #final del proceso
"
def modificarLinea(archivo,buscar,reemplazar):

	Esta simple función cambia una linea entera de un archivo
	Tiene que recibir el nombre del archivo, la cadena de la linea entera a
	buscar, y la cadena a reemplazar si la linea coincide con buscar
	"

	with open(archivo, "r") as f:
		# obtenemos las lineas del archivo en una lista
		lines = (line.rstrip() for line in f)

		# busca en cada linea si existe la cadena a buscar, y si la encuentra
		# la reemplaza
		altered_lines = [reemplazar if line==buscar else line for line in lines]

	with open(archivo, "w") as f:
		# guarda nuevamente todas las lineas en el archivo
		f.write('\n'.join(altered_lines) + '\n')

modificarLinea("archivo.txt","casa","avion")


https://www.lawebdelprogramador.com/codigo/Python/3843-Reemplazar-una-linea-de-un-archivo.html
https://uniwebsidad.com/libros/algoritmos-python/capitulo-11

"""
