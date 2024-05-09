import sqlite3

conexion = sqlite3.connect("base de datos.db")
cursorBD = conexion.cursor()

class Granja:
    def __init__(self):
        self.create_tables()

    def create_tables(self):
        cursorBD.execute('''CREATE TABLE IF NOT EXISTS cultivos (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT,
                                area REAL,
                                produccion REAL
                                )''')
        cursorBD.execute('''CREATE TABLE IF NOT EXISTS animales (
                                id INTEGER PRIMARY KEY,
                                raza TEXT,
                                edad INTEGER,
                                peso REAL
                                )''')
        conexion.commit()

    def agregar_cultivo(self, nombre, area, produccion):
        cursorBD.execute("INSERT INTO cultivos (nombre, area, produccion) VALUES (?, ?, ?)",
                            (nombre, area, produccion))
        conexion.commit()
        print("Cultivo agregado con éxito.")

    def agregar_animal(self, raza, edad, peso):
        cursorBD.execute("INSERT INTO animales (raza, edad, peso) VALUES (?, ?, ?)",
                            (raza, edad, peso))
        conexion.commit()
        print("Animal agregado con éxito.")

    def consultar_cultivos(self):
        cursorBD.execute("SELECT * FROM cultivos")
        cultivos = cursorBD.fetchall()
        print("Lista de cultivos:")
        for cultivo in cultivos:
            print(cultivo)

    def consultar_animales(self):
        cursorBD.execute("SELECT * FROM animales")
        animales = cursorBD.fetchall()
        print("Lista de animales:")
        for animal in animales:
            print(animal)

    def modificar_cultivo(self, id, nombre, area, produccion):
        cursorBD.execute("UPDATE cultivos SET nombre=?, area=?, produccion=? WHERE id=?",
                            (nombre, area, produccion, id))
        conexion.commit()
        print("Cultivo modificado con éxito.")

    def modificar_animal(self, id, raza, edad, peso):
        cursorBD.execute("UPDATE animales SET raza=?, edad=?, peso=? WHERE id=?",
                            (raza, edad, peso, id))
        conexion.commit()
        print("Animal modificado con éxito.")

    def eliminar_cultivo(self, id):
        cursorBD.execute("DELETE FROM cultivos WHERE id=?", (id,))
        conexion.commit()
        print("Cultivo eliminado con éxito.")

    def eliminar_animal(self, id):
        cursorBD.execute("DELETE FROM animales WHERE id=?", (id,))
        conexion.commit()
        print("Animal eliminado con éxito.")

    def calcular_produccion_total_cultivos(self):
        cursorBD.execute("SELECT SUM(produccion) FROM cultivos")
        produccion_total = cursorBD.fetchone()[0]
        print(f"Producción total de cultivos: {produccion_total if produccion_total else 0}")

    def calcular_produccion_total_ganado(self):
        cursorBD.execute("SELECT SUM(peso) FROM animales")
        peso_total = cursorBD.fetchone()[0]
        print(f"Peso total del ganado: {peso_total if peso_total else 0}")

# Ejemplo de uso:
granja = Granja()

opcion = 0
while opcion != 7:
    print("\nMenú:")
    print("1. Agregar cultivo")
    print("2. Agregar animal")
    print("3. Consultar cultivos")
    print("4. Consultar animales")
    print("5. Modificar cultivo")
    print("6. Modificar animal")
    print("7. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Nombre del cultivo: ")
        area = float(input("Área del cultivo en metros cuadrados: "))
        produccion = float(input("Producción del cultivo en toneladas: "))
        granja.agregar_cultivo(nombre, area, produccion)
    elif opcion == 2:
        raza = input("Raza del animal: ")
        edad = int(input("Edad del animal en años: "))
        peso = float(input("Peso del animal en kilogramos: "))
        granja.agregar_animal(raza, edad, peso)
    elif opcion == 3:
        granja.consultar_cultivos()
    elif opcion == 4:
        granja.consultar_animales()
    elif opcion == 5:
        id = int(input("ID del cultivo que desea modificar: "))
        nombre = input("Nuevo nombre del cultivo: ")
        area = float(input("Nueva área del cultivo en metros cuadrados: "))
        produccion = float(input("Nueva producción del cultivo en toneladas: "))
        granja.modificar_cultivo(id, nombre, area, produccion)
    elif opcion == 6:
        id = int(input("ID del animal que desea modificar: "))
        raza = input("Nueva raza del animal: ")
        edad = int(input("Nueva edad del animal en años: "))
        peso = float(input("Nuevo peso del animal en kilogramos: "))
        granja.modificar_animal(id, raza, edad, peso)
    elif opcion == 7:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

conexion.close()
                  