import time
import random

#funcion si se quiere  que la lista sea desordenada para comprobar su tiempo 
def listadesordenada(tamaño):
    # crea una lista desordenada con datos entre 1.0 y 5.0
    #round significa redondee los decimales(float) a solo
    lista = [round(random.uniform(1.0,5.0),2) for _ in range(tamaño)]
    return lista
    

def lista_por_bloques(tamaño, tam_bloque):
    lista = list(range(1, tamaño+1))
    lista = [round(random.uniform(0.0, 5.0), 2) for _ in range(tamaño)]
    
    bloques = [lista[i:i+tam_bloque] for i in range(0, tamaño, tam_bloque)]
    random.shuffle(bloques)
    lista = [num for bloque in bloques for num in bloque]
    return lista

def merge_sort(lista):#Divide la lista en  casos base
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)#devuelve la lista en casos base para organizarla


def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:  # <= garantiza estabilidad
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

print(""" --Tipo de listas a ordenar:--
        1.)Lista desordenada
        2.)Lista semiodenada""")
tipo = int(input("elije  el tipo de lista que quieres ordenar "))

while tipo not in (1,2):
    
    print("opcion no valida")
    print(""" --Tipo de listas a ordenar:--
        1.)Lista desordenada
        2.)Lista semiodenada""")
    tipo = int(input("elije  el tipo de lista que quieres ordenar "))
if tipo ==1:
        tamaño = int(input("ingresa la cantidad de datos que va a tener la lista"))
        lista= listadesordenada(tamaño)

elif tipo==2:
        tamaño = int(input("ingresa la cantidad de datos que va a tener la lista"))
        tam_bloque = int(input("Ingresa de cuantos datos tenga cada bloque"))
        lista = lista_por_bloques(tamaño, tam_bloque)



inicio = time.perf_counter()
lista_merge = merge_sort(lista)
fin = time.perf_counter()

print(f"\n----RESULTADOS merge.sort----")
for i in range(min(20,len(lista))):
    print(f"Origin: {lista[i]}  Mod: {lista_merge[i]}")
    
if tipo ==1:
    print("tipo de lista de datos: Desordenada")
elif tipo == 2:
    print("tipo de lista de datos: Semiordenada")
print(f"Tamaño de datos: {tamaño}")
print(f"Tiempo Merge: {fin - inicio}")