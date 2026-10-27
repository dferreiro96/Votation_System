# Voting System 🗳️

## 🇬🇧 English

A command-line voting simulation application written in Python. It allows you to register candidates, set the number of voters, simulate a random election, and display the final results with percentages and a clear winner. All data is persistently stored so you don't lose your progress between sessions.

### Features

- ➕ Register between 2 and 5 candidates per election
- 🛡️ Name validation (minimum length, no numbers, no duplicates)
- 👥 Set the exact number of voters participating
- 📋 View the list of registered candidates alphabetically
- 🎲 Simulate votes randomly (no duplicate voters required, just a total count)
- 📊 Display results sorted by votes, showing percentages and the final winner
- 💾 **Automatic persistence:** Saves candidates and election data to a JSON file
- 🧩 Fully modularized structure for easy maintenance

### Requirements

- Python 3.10 or higher (uses `match` statements and modern string formatting)

No external dependencies — only the standard library (`random`, `json`).


### Follow the on-screen menu:


____MENU____
1. Registrar nuevo candidato
2. Mostrar lista de candidatos
3. Determinar cantidad de votantes
4. Votar y mostrar resultados de la votación
5. Salir

### Data Storage

The system saves data locally using JSON. If the file doesn't exist, it will be created automatically. This allows you to close the program and resume your configuration later.

usuarios.json: Stores the registered candidates and their current vote count.

Example structure:

json
[
    {"Nombre": "Candidato A", "Votos": 0},
    {"Nombre": "Candidato B", "Votos": 0}
]

### Project Structure

This project is modular, separating logic, data persistence, and the user interface. Based on the file structure, the responsibilities are divided as follows:

### Logic Overview

- The system simulates an election in memory and saves the state:

- Candidates are stored as dictionaries: {"Nombre": "Candidato", "Votos": 0}.

- The votar() function distributes the total votes randomly among the candidates.

- The mostrar_resultados() function calculates percentages (votes / total_voters * 100), sorts candidates in descending order, and highlights the winner.

### Possible Improvements

- Allow multiple rounds (run-off elections) if there is a tie.

- Add unit tests for the validation and calculation functions.

- Export final results to CSV or PDF.

## 🇪🇸 Español

Una aplicación de línea de comandos para simular un sistema de votación, escrita en Python. Permite registrar candidatos, definir la cantidad de votantes, simular una elección de forma aleatoria y mostrar los resultados finales con porcentajes y el ganador. Todos los datos se guardan de forma persistente para no perder el progreso entre sesiones.

### Características

- ➕ Registrar entre 2 y 5 candidatos por elección
- 🛡️ Validación de nombres (longitud mínima, sin números, sin duplicados)
- 👥 Definir la cantidad exacta de votantes que participarán
- 📋 Mostrar la lista de candidatos registrados ordenada alfabéticamente
- 🎲 Simular los votos de forma aleatoria (sin duplicados, solo el total)
- 📊 Mostrar resultados ordenados por votos, con porcentajes y el ganador final
- 💾 Persistencia automática: Guarda los candidatos y los datos de la elección en un archivo JSON
- 🧩 Estructura completamente modularizada para facilitar el mantenimiento

### Requisitos

- Python 3.10 o superior (usa match y formato moderno de cadenas)

Sin dependencias externas — solo la librería estándar (random, json).

### Uso

Clona o descarga los archivos del proyecto.

Ejecuta el script principal:

bash
python main.py
Sigue el menú en pantalla:


____MENU____
1. Registrar nuevo candidato
2. Mostrar lista de candidatos
3. Determinar cantidad de votantes
4. Votar y mostrar resultados de la votación
5. Salir

### Almacenamiento de datos

El sistema guarda los datos localmente usando JSON. Si el archivo no existe, se creará automáticamente. Esto te permite cerrar el programa y retomar la configuración más tarde.

usuarios.json: Almacena los candidatos registrados y su conteo actual de votos.

Ejemplo de estructura:

json
[
    {"Nombre": "Candidato A", "Votos": 0},
    {"Nombre": "Candidato B", "Votos": 0}
]

### Estructura del proyecto

Este proyecto está modularizado, separando la lógica de negocio, la persistencia de datos y la interfaz de usuario. Según la estructura de archivos, las responsabilidades se dividen así:


### Resumen de la lógica

 El sistema simula una elección en memoria y guarda su estado:

- Los candidatos se guardan como diccionarios: {"Nombre": "Candidato", "Votos": 0}.
- La función votar() reparte el total de votos de forma aleatoria entre los candidatos.
- La función mostrar_resultados() calcula los porcentajes (votos / total_votantes * 100), ordena de mayor a menor y destaca al ganador.

### Mejoras posibles

- Permitir múltiples rondas (segunda vuelta) en caso de empate.
- Añadir tests unitarios para las funciones de validación y cálculo.
- Exportar los resultados finales a CSV o PDF.

### Author

- [dferreiro96]

### 📄 License / Licencia

Free to use and modify for personal or educational purposes.
Libre para usar y modificar con fines personales o educativos.

### Usage

1. Clone or download the project files.
2. Run the main script:

```bash
python main.py

