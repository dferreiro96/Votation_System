# Voting System 🗳️

## 🇬🇧 English

A command-line voting simulation application written in Python. It allows you to register candidates, set the number of voters, simulate a random election, and display the final results with percentages and a clear winner.

### Features

- ➕ Register between 2 and 5 candidates per election
- 🛡️ Name validation (minimum length, no numbers, no duplicates)
- 👥 Set the exact number of voters participating
- 📋 View the list of registered candidates alphabetically
- 🎲 Simulate votes randomly (no duplicate voters required, just a total count)
- 📊 Display results sorted by votes, showing percentages and the final winner
- 🧩 Fully modularized structure for easy maintenance

### Requirements

- Python 3.10 or higher (uses `match` statements and modern string formatting)

No external dependencies — only the standard library (`random`).

### Follow the on-screen menu:

text
____MENU____
1. Registrar nuevo candidato
2. Mostrar lista de candidatos
3. Determinar cantidad de votantes
4. Votar y mostrar resultados de la votación
5. Salir

### Project Structure

This project is modular, separating logic, data persistence (if applicable), and UI. Based on the file structure, the responsibilities are divided as follows:



### Logic Overview

- The system simulates an election in memory:

- Candidates are stored as dictionaries: {"Nombre": "Candidato", "Votos": 0}.

- The votar() function distributes the total votes randomly among the candidates.

- The mostrar_resultados() function calculates percentages (votes / total_voters * 100), sorts candidates in descending order, and highlights the winner.

### Possible Improvements
Add persistence so elections can be saved and reviewed later.

Allow multiple rounds (run-off elections) if there is a tie.

Add unit tests for the validation and calculation functions.

Export results to CSV or PDF.

### Usage

1. Clone or download the project files.
2. Run the main script:

```bash
python main.py