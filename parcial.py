import time
import random

#funcion si se quiere  que la lista sea desordenada para comprobar su tiempo 
def listadesordenada(tamaño):
    # crea una lista desordenada con datos entre 1.0 y 5.0
    #round significa redondee los decimales(float) a solo uno
    #random.uniform crea numeros aleatorios tipo float
    #for _ in range(tamaño)]: se van a crear hasta donde diga el susuario
    lista = [round(random.uniform(1.0,5.0),1) for _ in range(tamaño)]
    return lista
    

def lista_por_bloques(tamaño, tam_bloque):
    #round significa redondee los decimales(float) a solo uno
    #random.uniform crea numeros aleatorios tipo float
    #for _ in range(tamaño)]: se van a crear hasta donde diga el susuario
    lista = sorted([round(random.uniform(1.0, 5.0), 1) for _ in range(tamaño)])
    
    #[lista[i:i+tam_bloque] crea bloques o sublistas ordenadas con la cantidad de datos que ingreso el usuario
    #for i in range(0, tamaño, tam_bloque)] se van acrar estas listas desde 0 hasta el tamaño total de datos
    #con un salto entre ellos que seria el tamaño del bloque para evitar que se repitan datos

    bloques = [lista[i:i+tam_bloque] for i in range(0, tamaño, tam_bloque)]

    #Mezcla  el orden de las sublistas dejandolas desordenadas
    random.shuffle(bloques)
    #rrecorre el arreglo de bloques y los une en una sola lista
    lista = [num for bloque in bloques for num in bloque]
    return lista

def merge_sort(lista):#Divide la lista en  casos base
    if len(lista) <= 1:
        return lista
    #divide la lista en dos
    medio = len(lista) // 2
    #izquierda = :medio = desde el inicio hasta medio sin contar el final(inicio:fin) 
    izquierda = merge_sort(lista[:medio])
    #derecha = medio: = desde el inicio(medio) hasta el final x
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)#devuelve la lista en casos base para organizarla


def merge(izquierda, derecha):
    #donde se va a guardar
    resultado = []
    # i = contador izquierda j = contador derecha
    i = 0
    j = 0
    #el ordenamiento se va a efectuar hasta que i y j terminen de recorrer sus listas respectivas
    while i < len(izquierda) and j < len(derecha):

        # si el dato que representa i es menor a el de jota se añade a la lista ordenada
        if izquierda[i] <= derecha[j]:  # <= garantiza estabilidad
            resultado.append(izquierda[i])
            # añade uno a i para seguir recorriendo la lista y verificar el nuevo numero es menor que j
            i += 1
        else:
            #se añade a la lista organizada 
            resultado.append(derecha[j])
            # añade uno a j para seguir recorriendo la lista y verificar que el nuevo numero es menor que i
            j += 1
    #.extend envia lo que quedo de "sobra" en los datos de izquierda que no se pudieron  comparar y los manda al fnal
    #recordar que para este punto izquierda ya esta ordenada
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    #de vuelve el resultado 
    return resultado
#elije como llegan los datos para permitir  ver como se maneja el algoritmo en distintos casos
print(""" --Tipo de listas a ordenar:--
        1.)Lista desordenada
        2.)Lista semiodenada""")
tipo = int(input("elije  el tipo de lista que quieres ordenar "))
#verifica que lo recibido en la terminal si sea correcto y si no repite el menu
while tipo not in (1,2):
    
    print("opcion no valida")
    print(""" --Tipo de listas a ordenar:--
        1.)Lista desordenada
        2.)Lista semiodenada""")
    tipo = int(input("elije  el tipo de lista que quieres ordenar "))
#ejecuta la funcion de llegada de datos desordenados
if tipo ==1:
        tamaño = int(input("ingresa la cantidad de datos que va a tener la lista"))
        lista= listadesordenada(tamaño)
#ejecuta la funcion de datos semiordenados
elif tipo==2:
        tamaño = int(input("ingresa la cantidad de datos que va a tener la lista"))
        tam_bloque = int(input("Ingresa de cuantos datos tenga cada bloque"))
        lista = lista_por_bloques(tamaño, tam_bloque)


#incia el reloj
# time.perf_counter() es un cronometro de alta precision
# que mo se ve afectado por ajustes internos del dispositivo  es ideal para verificar tiempos de ejecucion 
inicio = time.perf_counter()
#ya teniendo las listas desordenadas o semiordenadas se llama a el algoritmo merge
lista_merge = merge_sort(lista)
#marca el final de ejecucion del algoritmo
fin = time.perf_counter()
# muestra los resultados y las variaciones que tubo el algoritmo para medir mejor diferencias
print(f"\n----RESULTADOS merge.sort----")
#en casos normales muestra 20 datos de la lista desorganizada y 20 de la organizada
# for i in range(min(20,len(lista))): proteje a el sistema en caso de que se ingresen menos de 20 datos no ocurra un error
# en  el caso de menos datos que 20 se muestra la cantidad que haya  
for i in range(min(20,len(lista))):
    print(f"Origin: {lista[i]}  Mod: {lista_merge[i]}")
    
if tipo ==1:
    print("tipo de lista de datos: Desordenada")
elif tipo == 2:
    print("tipo de lista de datos: Semiordenada")
print(f"Tamaño de datos: {tamaño}")
print(f"Tiempo Merge: {fin - inicio}")