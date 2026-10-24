
from logica import mostrar_lista_de_candidatos, mostrar_resultados, votar
from menu import menu
from persistencia import cargar_datos
from utilidades import pedir_opcion
from validaciones import (
    cantidad_de_candidatos,
    cantidad_de_votantes,
    introducir_candidatos,
)


def main():
    print("\nSistema de votación")
    lista_de_candidatos = cargar_datos()
    numero_de_votantes = 0
    while True:
        menu()
        opcion = pedir_opcion("\nOpción: ", ["1", "2", "3", "4", "5"])
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
                break

    print("\nHa salido del programa satisfactoriamente\n")


if __name__ == "__main__":
    main()
