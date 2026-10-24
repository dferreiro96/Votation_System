from persistencia import guardar_datos


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
            guardar_datos(lista_de_candidatos)
            print(f"Candidato {len(lista_de_candidatos)}, {candidato} añadido")
            return

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