
import lib.Funciones

print lib.Funciones.Control_Ethernet.Tiempo()

#print lib.Control_Ethernet.Tiempo()

#------------------------------------------------------------------------------
   	#---------------------------------------------------------
	#----						                        ------
	#----				 Programa principal             ------
	#----						                        ------
	#---------------------------------------------------------
#------------------------------------------------------------------------------
print 'Listo'

print lib.Funciones.Cantidad_Pines

while 1:
    #------------------if PP_Mensajes:---------------------------------------
    #  Proceso 0: Tiempo de espera para disminuir proceso
    #---------------------------------------------------------
    lib.Funciones.time.sleep(0.05)
