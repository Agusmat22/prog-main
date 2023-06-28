#Funciones
import re
from clases import Persona
from clases import AfiliadoPrestador
#ABRE ARCHIVO CSV Y RETORNA UNA LISTA (MODIFICAR LOS PATRONES SEGUN REQUERIMOS)
def abrir_csv(nombre:str,tipo_afiliado = None):

    with open(nombre,'r',encoding='latin-1') as archivo:

        lista_afiliados = []

        flag = True

        for afiliado in archivo:

            if flag == True:

                flag = False
                continue

            linea = re.split(';',afiliado)

            if tipo_afiliado == "prestador":

                afiliado = AfiliadoPrestador(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],linea[6],re.sub('\n','',linea[7]))

            else:

                afiliado = Persona(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],linea[6],re.sub('\n','',linea[7]))


            lista_afiliados.append(afiliado)

        return lista_afiliados
    
    

def crear_archivo_txt(nombre:str,lista:list)->None:

    
    with open(nombre,'w+',encoding='utf-8') as archivo:


        for afiliado in lista:

            #con ljust() indico cuando caracteres tendra la variable, lo que no se complete se rellena con espacion en blanco
            #limito la cantidad de caracteres con [:30]
            contenido = afiliado.entidad[:30].ljust(30) + ' '+str(afiliado.plan)[:30].ljust(30) + ' '+ afiliado.nombre[:30].ljust(30) + ' '+ str(afiliado.dni)[:30].ljust(30)  +'\n'

            archivo.write(contenido)



#MUESTRA UN MENU DE OPCIONES
def imprimir_menu_opciones(mensaje:str):

    print(mensaje)


def imprimir_afiliado(afiliado:object):

    print(afiliado.apellido + ' ' + afiliado.nombre + ' ' + str(afiliado.dni) + ' ' + str(afiliado.n_af))


#SANITIZA UN TEXTO
def sanitizar_texto(dato:str):

    aviso_error = None

    
    if type(dato) == str and dato != "":

        if not re.search('[0-9]',dato):

            #REEMPLAZA CUALQUIER CARACTER NO ALFABETICO EN UN ESPACIO EN BLANCO
            dato = re.sub(r'[^a-zA-Z\s]+',' ',dato)

            dato = re.split(' ',dato)

            elemento = ""

            for text in dato:

                #distinto de una cadena vacia ya que la lista puede fabricar varias cadenas vacias porque puede ocurrir varios espacios en blanco
                if text != "":

                    elemento += text + ' '

            #COLOCO UN SLICE PARA QUE NO MUESTRE EL ULTIMO ESPACIO EN BLANCO
            return elemento[:-1]
             
        else:

            aviso_error = f'La cadena ingresada contiene caracteres tipo numericos {dato}'
    else:

        aviso_error = f'El tipo de dato se encuentra vacio o no es del tipo cadena: {dato}'
        
    
    print(aviso_error)
    return dato



    

#SANITIZA UN NUMERO
def sanitizar_numero(numero):

    if type(numero) == str:

        #VALIDO QUE SEA UN ENTERO
        if re.search('^[0-9]+$',numero):

            numero = int(numero)

        #VALIDO QUE SEA UN FLOTANTE
        elif re.search('^[0-9]+\.[0-9]+$',numero):

            numero = float(numero)

        #ACA MUESTRO LAS KEYS CON ERRORES PERO POR EL MOMENTO NO LO VOY A USAR
        """ elif re.search('[^0-9]',numero):

            print(f'La cadena ingresada contiene caracteres no numericos: "{numero}"') """

    return numero
        

def normalizar_lista(lista:list):

    aviso_error = None

    if type(lista):

        if len(lista) > 1:

            for afi in lista:

                afi.dni = sanitizar_numero(afi.dni)
                afi.nombre = sanitizar_texto(afi.nombre)
                afi.apellido = sanitizar_texto(afi.apellido)
                afi.int = sanitizar_numero(afi.int)
                afi.tipo_documento = sanitizar_texto(afi.tipo_documento)
        

        else:

            aviso_error = 'La lista ingresada no contiene elementos'
    else:

        aviso_error = 'El tipo de dato ingresado no es una lista'

    if aviso_error != None:

        print(aviso_error)
    
    else:

        return lista



#listavich = [ {'nombre':'AGUSTIN','edad': '25'},{'nombre':'lucas','edad': '225'},{'nombre':'brian','edad': '85'}]



def obtener_elementos_lista(lista:list,cantidad:int):

    if type(lista) == list and type(cantidad) == int:

        lista_nueva = []

        for posicion in range(cantidad):

            lista_nueva.append(lista[posicion])

        return lista_nueva
    

    

