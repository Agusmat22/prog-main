import re
from copy import deepcopy
import funciones



list_af = funciones.abrir_csv('appRoisa\\PADRONCSV.csv')
copy_lista_afiliados = deepcopy(list_af)

list_af_prestador = funciones.abrir_csv('appRoisa\\pruebaPrestador.csv',"prestador")
copy_lista_afiliados_prestador = deepcopy(list_af_prestador)

#print(list_af_prestador[5])

#funciones.normalizar_lista(copy_lista_afiliados,'dni','numero')


""" for afi in copy_lista_afiliados:

    afi.dni = funciones.sanitizar_numero(afi.dni)
    afi.nombre = funciones.sanitizar_texto(afi.nombre)
    afi.apellido = funciones.sanitizar_texto(afi.apellido)
    afi.entidad = funciones.sanitizar_texto(afi.entidad)
    afi.int = funciones.sanitizar_texto(afi.int)

    lista_nueva.append(afi) """

lista_normalizada_afiliados = funciones.normalizar_lista(copy_lista_afiliados)
lista_normalizada_afiliados_prestador = funciones.normalizar_lista(copy_lista_afiliados_prestador)


#lista_afiliado_encontrados = []

#LOS AFILIADOS INGRESADOS POR EL PRESTADOR, SEGUN EL NOMBRE LES CAMBIO EL NUMERO DE IDENTIDAD.
#MOSTRAR ESTO ALAN.
for afiliado in lista_normalizada_afiliados:

    for af_prestador in lista_normalizada_afiliados_prestador:

        if af_prestador.dni == afiliado.dni:

           if af_prestador.entidad == "AFILIADOS EXTRA CAPITA":
               
               af_prestador.entidad = "5"
            

        





funciones.crear_archivo_txt('lista_afiliados.txt',lista_normalizada_afiliados_prestador)



