import random

from persistencia import guardar_datos


def mostrar_lista_de_candidatos(lista_de_candidatos):
    lista_de_candidatos.sort(key=lambda x: x["Nombre"])
    print("\nLa lista de candidatos es la siguiente:\n")
    for i, candidato in enumerate(lista_de_candidatos, start=1):
        print(f"{i}. {candidato['Nombre']}")


def votar(lista_de_candidatos, numero_de_votantes):
    for candidato in lista_de_candidatos:
        candidato["Votos"] = 0
    for _ in range(numero_de_votantes):
        elegido = random.choice(lista_de_candidatos)
        elegido["Votos"] += 1
        guardar_datos(lista_de_candidatos)
    print(f"\nSe han repartido {numero_de_votantes} votos aleatoriamente")


def mostrar_resultados(lista_de_candidatos, numero_de_votantes):
    lista_de_candidatos.sort(key=lambda x: x["Votos"], reverse = True)
    print("Los resultados son los siguientes:\n")
    
    for i, candidato in enumerate(lista_de_candidatos, start=1):
        porcentaje = candidato["Votos"]/numero_de_votantes*100
        print(f"{i}. {candidato["Nombre"]}: {candidato["Votos"]} ({porcentaje:.1f} %)")
    print("\n---------------------------------------------")
    ganador = lista_de_candidatos[0]
    porcentaje_del_ganador = ganador["Votos"]/numero_de_votantes*100
    print(f"\nEl ganador fue {ganador["Nombre"]} con el {porcentaje_del_ganador:.1f} % de los votos.")