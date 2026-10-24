import json


def cargar_datos():
    try:
        with open("lista_de_candidatos.json", "r", encoding="utf-8") as archivo:
            lista_de_candidatos = json.load(archivo)
            print("\nDatos recuperados correctamente")
            return lista_de_candidatos
    except FileNotFoundError:
        print("\nNo se encontraron datos guardados. Se creará una nueva lista.")
        return []
    except json.JSONDecodeError:
        print("\nDatos guardados corruptos. Se creará una nueva lista.")
        return []
 
    
def guardar_datos(lista_de_candidatos):
    with open("lista_de_candidatos.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_de_candidatos, archivo, ensure_ascii=False)