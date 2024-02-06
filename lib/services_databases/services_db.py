import sqlite3

import pandas as pd


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS servicios (
        id INTEGER PRIMARY KEY,
        puerto INTEGER,
        nombre_servicio TEXT,
        ip TEXT
    );
    '''
    conn.execute(create_table_query)

def insert_data(conn, puerto, nombre_servicio, ip):
    insert_query = f'''
    INSERT INTO servicios (puerto, nombre_servicio, ip)
    VALUES ({puerto}, '{nombre_servicio}', '{ip}');
    '''
    conn.execute(insert_query)
    conn.commit()

def insert_data_from_csv(conn, csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo CSV en la ruta proporcionada: {csv_file_path}")
        return

    for index, row in df.iterrows():
        puerto = int(row['puerto'])
        nombre_servicio = str(row['nombre_servicio'])
        ip = str(row['ip'])

        insert_data(conn, puerto, nombre_servicio, ip)

    print(f"Registros insertados correctamente desde el archivo CSV: {csv_file_path}")



def select_all_data(conn):
    select_query = 'SELECT * FROM servicios;'
    cursor = conn.execute(select_query)
    result = cursor.fetchall()
    return result

def update_data(conn, id, nuevo_puerto, nuevo_nombre_servicio, nueva_ip):
    update_query = f'''
    UPDATE servicios
    SET puerto = {nuevo_puerto},
        nombre_servicio = '{nuevo_nombre_servicio}',
        ip = '{nueva_ip}'
    WHERE id = {id};
    '''
    conn.execute(update_query)
    conn.commit()

def delete_data(conn, id):
    delete_query = f"DELETE FROM servicios WHERE id = {id};"
    conn.execute(delete_query)
    conn.commit()

def main():
    # Conectar a la base de datos SQLite
    conn = create_connection("services.db")

    # Crear la base de datos y la tabla (si no existen)
    create_table(conn)

    while True:
        # Mostrar menú
        print("\nMenú:")
        print("1. Ver registros en la base de datos")
        print("2. Insertar un nuevo registro")
        print("3. Actualizar un registro por ID")
        print("4. Eliminar un registro por ID")
        print("5. Salir")

        # Solicitar la opción al usuario
        option = input("Seleccione una opción (1-5): ")

        if option == '1':
            # Consultar todos los registros en la tabla
            result = select_all_data(conn)
            print("\nRegistros en la base de datos:")
            for row in result:
                print(row)

        elif option == '2':
            try:
                puerto = int(input("Ingrese el puerto: "))
                nombre_servicio = input("Ingrese el nombre del servicio: ")
                ip = input("Ingrese la dirección IP: ")

                insert_data(conn, puerto, nombre_servicio, ip)
                print("Registro insertado correctamente.")

            except ValueError:
                print("Error: Ingrese un número válido para el puerto.")

        elif option == '3':
            try:
                id_a_actualizar = int(input("Ingrese el ID del registro que desea actualizar: "))
                nuevo_puerto = int(input("Ingrese el nuevo puerto: "))
                nuevo_nombre_servicio = input("Ingrese el nuevo nombre del servicio: ")
                nueva_ip = input("Ingrese la nueva dirección IP: ")

                update_data(conn, id_a_actualizar, nuevo_puerto, nuevo_nombre_servicio, nueva_ip)
                print("Registro actualizado correctamente.")

            except ValueError:
                print("Error: Ingrese un número válido para el ID.")

        elif option == '4':
            try:
                id_a_eliminar = int(input("Ingrese el ID del registro que desea eliminar: "))
                delete_data(conn, id_a_eliminar)
                print("Registro eliminado correctamente.")
            except ValueError:
                print("Error: Ingrese un número válido para el ID.")

        elif option == '5':
            # Salir del bucle y cerrar la conexión
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

    # Cerrar la conexión a la base de datos
    conn.close()

if __name__ == "__main__":
    main()
    # Conectar a la base de datos SQLite
    #conn = create_connection("services.db")
    # insert_data_from_csv(conn, "data.csv")
    # print(select_all_data(conn))
