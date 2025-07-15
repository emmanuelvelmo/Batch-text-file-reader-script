import os

# Lista de codificaciones a probar (en orden de prioridad)
codificaciones_txt = ['utf-8', 'latin-1', 'utf-16', 'cp1252']

ruta_dir = input("Enter directory: ")

print("\n------------------------------------")

# Recorre todos los archivos en la carpeta
for nombre_archivo in os.listdir(ruta_dir):
    # Construye la ruta completa del archivo
    ruta_completa = os.path.join(ruta_dir, nombre_archivo)
    
    # Verifica si es un archivo (y no una carpeta)
    if os.path.isfile(ruta_completa):
        # Intenta decodificar en cada formato
        for codificacion_iter in codificaciones_txt:  
            try:
                # Intenta abrir y leer el contenido del archivo como texto
                with open(ruta_completa, 'r', encoding = codificacion_iter) as archivo:
                    contenido_val = archivo.read()
                    
                    # Si no hay excepción, imprime el nombre y el contenido del archivo
                    print(f"{nombre_archivo}\n")
                    print(contenido_val)
                    print("------------------------------------")

                    break
            except (UnicodeDecodeError, PermissionError, IOError):
                # Si ocurre un error, simplemente continúa con el siguiente archivo
                continue

# Espera a que el usuario presione Enter antes de cerrar
input()
