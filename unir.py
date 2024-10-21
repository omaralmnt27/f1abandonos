import os
import csv

# Lista de archivos CSV de los pilotos
csv_files = [


    {'file': 'abandonos_alexander-albon.csv', 'name': 'Alexander Albon'},

    {'file': 'abandonos_carlos-sainz.csv', 'name': 'Carlos Sainz'},

    {'file': 'abandonos_charles-leclerc.csv', 'name': 'charles Leclerc'},

    {'file': 'abandonos_daniel-ricciardo.csv', 'name': 'Daniel Ricciardo'},

    {'file': 'abandonos_esteban-ocon.csv', 'name': 'Esteban Ocon'},

    {'file': 'abandonos_fernando-alonso.csv', 'name': 'Fernando Alonso'},

    {'file': 'abandonos_george-russell.csv', 'name': 'George Russel'},

    {'file': 'abandonos_guanyu-zhou.csv', 'name': 'Guanyu Zhou'},

    {'file': 'abandonos_kevin-magnussen.csv', 'name': 'Kevin Magnussen'},
    {'file': 'abandonos_lance-stroll.csv', 'name': 'Lance stroll'},
    {'file': 'abandonos_lando-norris.csv', 'name': 'Lando norris'},
    {'file': 'abandonos_lewis-hamilton.csv', 'name': 'Lewis Hamilton'},

    {'file': 'abandonos_logan-sargeant.csv', 'name': 'Logan Sargeant'},

    {'file': 'abandonos_max-verstappen.csv', 'name': 'Max Verstappen'},

    {'file': 'abandonos_nico-hulkenberg.csv', 'name': 'Nico Hulkenberg'},

    {'file': 'abandonos_oscar-piastri.csv', 'name': 'Oscar Piastri'},

    {'file': 'abandonos_pierre-gasly.csv', 'name': 'Pierre Gasly'},

    {'file': 'abandonos_sergio-perez.csv', 'name': 'Sergio Perez'},
    {'file': 'abandonos_valtteri-bottas.csv', 'name': 'Valtteri Bottas'},
    {'file': 'abandonos_yuki-tsunoda.csv', 'name': 'Yuki Tsunoda'},
   
    # Agrega más pilotos aquí
]

# Archivo final donde se unificarán todos los datos
output_file = 'abandonos_unificado.csv'

# Comenzar a procesar cada archivo
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = None
    for pilot in csv_files:
        csv_file = pilot['file']
        pilot_name = pilot['name']

        # Abrir cada archivo CSV y añadir la columna "Pilot Name"
        with open(csv_file, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            if writer is None:
                # Crear el writer con las columnas originales más la de "Pilot Name"
                fieldnames = reader.fieldnames + ['Pilot Name']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

            # Añadir los datos de cada fila junto con el nombre del piloto
            for row in reader:
                row['Pilot Name'] = pilot_name  # Añadir el nombre del piloto
                writer.writerow(row)  # Escribir la fila en el archivo de salida

print(f'Los datos han sido unificados en {output_file}')
