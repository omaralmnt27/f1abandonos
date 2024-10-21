import pandas as pd

# Cargar el dataset original
archivo = "abandonos_unificado.csv"  # Asegúrate de cambiar el nombre por el de tu archivo original
df = pd.read_csv(archivo)

# Definir las causas que consideraremos fallas mecánicas
fallas_mecanicas = [
    'Engine', 'Gearbox', 'Brakes', 'Turbo', 'Clutch', 'Hydraulics', 
    'Electronics', 'Power loss', 'Oil leak', 'Exhaust', 'Suspension', 
    'Battery', 'Wheel', 'Steering', 'Undertray', 'Overheating', 'Water pressure'
]

# Filtrar los abandonos que sean por fallas mecánicas
df_fallas_mecanicas = df[df['Retirement'].isin(fallas_mecanicas)]

# Guardar el nuevo CSV
df_fallas_mecanicas.to_csv("f1_abandonos_fallas_mecanicas.csv", index=False)

print("Se ha creado el archivo CSV con los abandonos por fallas mecánicas.")
