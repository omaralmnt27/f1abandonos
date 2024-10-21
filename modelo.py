import requests
from bs4 import BeautifulSoup
import csv

# URL de la página que deseas scrape
url = 'https://www.statsf1.com/en/oscar-piastri/abandon.aspx'

# Configurar encabezados para simular un navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# Realizar la solicitud GET a la página
response = requests.get(url, headers=headers)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer la tabla de abandonos
    abandon_table = soup.find('table', id='ctl00_CPH_Main_GV_Stats')

    # Comprobar si se encontró la tabla
    if abandon_table:
        # Obtener las filas de la tabla
        rows = abandon_table.find_all('tr')[1:]  # Ignorar el encabezado

        results = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 12:  # Verificar que hay suficientes columnas
                n = cols[0].text.strip()
                year = cols[1].text.strip()
                grand_prix = cols[2].text.strip()
                grid = cols[3].text.strip()
                number = cols[4].text.strip()
                chassis = cols[5].text.strip() + " " + cols[6].text.strip()  # Concatenar columnas de Chassis
                engine = cols[7].text.strip() + " " + cols[8].text.strip()  # Concatenar columnas de Engine
                tyre = cols[9].text.strip()
                lap = cols[10].text.strip()
                retirement = cols[11].text.strip()

                results.append({
                    'N': n,
                    'Year': year,
                    'Grand Prix': grand_prix,
                    'Grid': grid,
                    'N°': number,
                    'Chassis': chassis,
                    'Engine': engine,
                    'Tyre': tyre,
                    'Lap': lap,
                    'Retirement': retirement
                })

        # Guardar los resultados en un archivo CSV
        csv_file = 'abandonos_oscar-piastri.csv'
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()  # Escribir encabezados
            writer.writerows(results)  # Escribir filas de datos

        print(f'Datos guardados en {csv_file}')
    else:
        print("No se encontró la tabla de abandonos en la página.")
else:
    print(f'Error al realizar la solicitud: {response.status_code}')
