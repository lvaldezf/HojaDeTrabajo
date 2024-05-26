import csv

class HashTable:    4
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search_by_key(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def search_by_value(self, value):
        for bucket in self.table:
            for pair in bucket:
                if pair[1] == value:
                    return pair[0]
        return None

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")

def insert_manual_data(hash_table):
    print("Insertar datos manualmente:")
    while True:
        key = input("Ingrese la clave (o 'q' para salir): ")
        if key == 'q':
            break
        value = input("Ingrese el valor: ")
        hash_table.insert(key, value)
        print(f"Valor '{value}' insertado con la clave '{key}'.")

def load_data_from_csv(hash_table, filename):
    print(f"Cargando datos desde el archivo '{filename}'...")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key, value = row
            hash_table.insert(key, value)
    print("Datos cargados exitosamente.")

def main():
    size = int(input("Ingrese el tamaño de la tabla hash: "))
    hash_table = HashTable(size)

    while True:
        print("\n--- Menú ---")
        print("1. Insertar datos manualmente")
        print("2. Realizar búsqueda por clave")
        print("3. Realizar búsqueda por valor")
        print("4. Cargar datos desde un archivo CSV")
        print("5. Mostrar tabla hash")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            insert_manual_data(hash_table)
        elif choice == '2':
            key = input("Ingrese la clave a buscar: ")
            result = hash_table.search_by_key(key)
            if result:
                print(f"Valor encontrado: {result}")
            else:
                print("Clave no encontrada.")
        elif choice == '3':
            value = input("Ingrese el valor a buscar: ")
            result = hash_table.search_by_value(value)
            if result:
                print(f"Clave encontrada: {result}")
            else:
                print("Valor no encontrado.")
        elif choice == '4':
            filename = input("Ingrese el nombre del archivo CSV: ")
            load_data_from_csv(hash_table, filename)
        elif choice == '5':
            hash_table.display()
        elif choice == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
