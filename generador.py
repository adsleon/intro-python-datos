import pandas as pd
import numpy as np

# Generar datos ficticios
np.random.seed(42)  # Para reproducibilidad

num_prod = 20

# Crear un DataFrame con datos de ejemplo
data = {
    'Producto': [f'Producto_{i}' for i in range(1, num_prod+1)],        # 20 productos
    'Fabricados': np.random.randint(50, 500, num_prod),               # Cantidad fabricada entre 50 y 500
    'Coste Unitario': np.random.uniform(10, 100, num_prod),           # Costo por unidad entre 10 y 100
    'Vendidos': np.random.randint(20, 400, num_prod),                 # Cantidad vendida entre 20 y 400
    'Precio de Venta': np.random.uniform(20, 200, num_prod)           # Precio de venta entre 20 y 200
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Guardar en un archivo Excel
df.to_excel('datos_ejemplo.xlsx', index=False)

print("Archivo 'datos_ejemplo.xlsx' ha sido creado con datos de ejemplo.")
