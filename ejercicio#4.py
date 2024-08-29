class Vehiculo:
    def __init__(self, tipo, marca, modelo, año, precio_diario):
        if not tipo or not marca or not modelo or año <= 0 or precio_diario <= 0:
            raise ValueError("Todos los campos de tipo, marca, modelo, año y precio diario deben estar completos y válidos.")
        
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_diario = precio_diario
        self.rentado = False

    def __str__(self):
        estado = "Rentado" if self.rentado else "Disponible"
        return f"{self.tipo} {self.marca} {self.modelo} ({self.año}) - {self.precio_diario} USD/día - {estado}"


class EmpresaRenta:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("Solo se pueden agregar objetos de tipo Vehiculo.")
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en la empresa.")
        else:
            print("Listado de todos los vehículos disponibles en la empresa:")
            for vehiculo in self.vehiculos:
                print(vehiculo)

    def rentar_vehiculo(self, tipo, marca, modelo, nombre_cliente, dias_renta):
        try:
            for vehiculo in self.vehiculos:
                if vehiculo.tipo.lower() == tipo.lower() and vehiculo.marca.lower() == marca.lower() and vehiculo.modelo.lower() == modelo.lower():
                    if not vehiculo.rentado:
                        vehiculo.rentado = True
                        total = vehiculo.precio_diario * dias_renta
                        print(f"Vehículo rentado con éxito a {nombre_cliente} por {dias_renta} días. Total a pagar: {total} USD")
                        return
                    else:
                        raise ValueError("El vehículo ya está rentado.")
            raise ValueError("Vehículo no encontrado.")
        except ValueError as e:
            print(f"Error: {e}")


def menu():
    print("Empresa de Renta de Transporte")
    print("1. Agregar vehículo")
    print("2. Listar todos los vehículos")
    print("3. Rentar vehículo")
    print("4. Salir")


def main():
    empresa = EmpresaRenta()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                tipo = input("Tipo de vehículo (ej. Auto, Camión, Moto): ")
                marca = input("Marca del vehículo: ")
                modelo = input("Modelo del vehículo: ")
                año = int(input("Año del vehículo: "))
                precio_diario = float(input("Precio de renta por día (USD): "))
                
                vehiculo = Vehiculo(tipo, marca, modelo, año, precio_diario)
                empresa.agregar_vehiculo(vehiculo)
                print("Vehículo agregado con éxito!")

            elif opcion == "2":
                empresa.listar_vehiculos()

            elif opcion == "3":
                tipo = input("Tipo de vehículo que desea rentar: ")
                marca = input("Marca del vehículo: ")
                modelo = input("Modelo del vehículo: ")
                nombre_cliente = input("Nombre del cliente: ")
                dias_renta = int(input("Número de días de renta: "))
                empresa.rentar_vehiculo(tipo, marca, modelo, nombre_cliente, dias_renta)

            elif opcion == "4":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as e:
            print(f"Error de entrada: {e}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
