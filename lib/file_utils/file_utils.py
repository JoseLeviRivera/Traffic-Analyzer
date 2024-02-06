import pandas as pd


def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def print_banner_green(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            print_red(contenido)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")


def print_green(contenido):
    print("\033[92m" + contenido + "\033[0m")

def print_red(contenido):
    print("\033[91m" + contenido + "\033[0m")