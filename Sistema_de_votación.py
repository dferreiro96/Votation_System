## Sistema_de_votación
# diccionario de candidatos
# funciones: votar, mostrar_resultados, main
# sin duplicados por votantes

import random


def cantidad_de_candidatos():
    while True:
        try:
            numero_de_candidatos = int(input("\n¿Cuántos candidatos habrá?: "))
            if numero_de_candidatos < 2 or numero_de_candidatos > 5:
                print("\nSe permiten entre 2 y 5 candidatos\n")
                continue
        except ValueError:
            print("\nSolo números")
            continue
        return numero_de_candidatos


def introducir_candidatos(lista_de_candidatos):
    while True:
        candidato = input("\nNombre del candidato: ").title().strip()
        if len(candidato) < 3:
            print(
                "\nEl nombre del candidato debe ser mayor a 3 caracteres, y contener ùnicamnete letras."
            )
            continue
        tiene_numeros = any(c.isdigit() for c in candidato)
        if tiene_numeros:
            print(
                "\nEl nombre del candidato debe ser mayor a 3 caracteres, y contener únicamente letras."
            )
            continue
        if any(candidatos["Nombre"] == candidato for candidatos in lista_de_candidatos):
            print("\nEl candidato ya ha sido registrado")
            continue
        else:
            lista_de_candidatos.append({"Nombre": candidato, "Votos": 0})
            print(f"\nCandidato {len(lista_de_candidatos)}, {candidato} añadido")
            return


def cantidad_de_votantes():
    while True:
        try:
            numero_de_votantes = int(input("\n¿Cuántos votantes habrá?: "))
            if numero_de_votantes < 2:
                print("\nTiene que haber más de 2 votantes")
                continue
        except ValueError:
            print("\nSolo números")
            continue
        print(f"\nSe anotaron {numero_de_votantes} electores")
        return numero_de_votantes


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
        
    
def menu():
    print("\n____MENU____")
    print("1. Registrar nuevo candidato")
    print("2. Mostrar lista de candidatos")
    print("3. Determinar cantidad de votantes")
    print("4. Votar y mostrar resultados de la votación")
    print("5. Salir")


def pedir_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion in opciones:
            return opcion
        else:
            print("\nOpción no válida")


def programa():
    lista_de_candidatos = []
    print("\nSistema de votación")
    numero_de_votantes = 0
    while True:
        menu()
        opcion = pedir_opcion("\nOpción: ", ["1", "2", "3", "4", "5", "6"])
        match opcion:
            case "1":
                numero_de_candidatos = cantidad_de_candidatos()
                while len(lista_de_candidatos) < numero_de_candidatos:
                    introducir_candidatos(lista_de_candidatos)
            case "2":
                if not lista_de_candidatos:
                    print("\nNo ha introducido candidatos")
                else:
                    mostrar_lista_de_candidatos(lista_de_candidatos)
            case "3":
                numero_de_votantes = cantidad_de_votantes()
                    
            case "4":
                if not lista_de_candidatos or not numero_de_votantes:
                    print("\nNo ha introducido candidatos o votantes")
                else:
                    votar(lista_de_candidatos, numero_de_votantes)
                    mostrar_resultados(lista_de_candidatos, numero_de_votantes)
                    return
                    
                    
            case "5":
                return


def main():
    programa()
    print("\nHa salido del programa satisfactoriamente\n")


if __name__ == "__main__":
    main()
