import requests


def auto_clasificado_por_color(color):
    url = "https://myfakeapi.com/api/cars/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        autos = data["cars"]

        autos_or_color = [auto for auto in autos if auto["car_color"] == color]
        return autos_or_color

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud HTTP: {str(e)}")

    except ValueError as e:
        print(f"Error de respuesta JSON: {str(e)}")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")



def auto_clasificado_por_valor_max(num_autos):
    url = "https://myfakeapi.com/api/cars/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        autos = data["cars"]

        autos_or_valor = sorted(autos, key=lambda auto: float(auto["price"].strip("$")), reverse=True)

        autos_valor_max = autos_or_valor[:num_autos]
        return autos_valor_max

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud HTTP: {str(e)}")

    except ValueError as e:
        print(f"Error de respuesta JSON: {str(e)}")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")


def auto_clasificado_por_vin(vin):
    url = f"https://myfakeapi.com/api/cars/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        autos = data["cars"]

        autos_or_vin = next((auto for auto in autos if auto["car_vin"] == vin), None)
        return autos_or_vin

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud HTTP: {str(e)}")

    except ValueError as e:
        print(f"Error de respuesta JSON: {str(e)}")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")

def auto_clasificado_por_ma_mo(marca, modelo):
    url = "https://myfakeapi.com/api/cars/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        autos = data["cars"]

        autos_or_ma_mo = [(auto["car"], auto["car_model"]) for auto in autos if
                                     auto["car"] == marca and auto["car_model"] == modelo]

        return autos_or_ma_mo

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud HTTP: {str(e)}")

    except ValueError as e:
        print(f"Error de respuesta JSON: {str(e)}")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")

def auto_clasificado_por_ma_an_mo(marca, an_modelo):
    url = f"https://myfakeapi.com/api/cars/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        autos = data["cars"]

        autos_or_ma_an_mo = [(auto["car"], auto["car_model_year"]) for auto in autos if
                                          auto["car"] == marca and auto["car_model_year"] == an_modelo]

        return autos_or_ma_an_mo

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud HTTP: {str(e)}")

    except ValueError as e:
        print(f"Error de respuesta JSON: {str(e)}")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")



def mostrar_autos(autos):
    for auto in autos:
        print(auto)
    print()


def menu():
    print("¡Bienvenido al menú de opciones de vehículo!")
    print("1. Obtener vehículo por color")
    print("2. Obtener vehículo por precio máximo")
    print("3. Obtener vehículo por car_vin")
    print("4. Obtener vehículo por marca y modelo")
    print("5. Obtener vehículo por marca y año de modelo")
    print("6. Salir")
    print()

    while True:
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            color = input("Ingrese el color de los autos: ")
            autos_or_color = auto_clasificado_por_color(color)
            if autos_or_color:
                print(f"autos con color {color}:")
                mostrar_autos(autos_or_color)
            else:
                print(f"No se encontraron autos con el color {color}.")

        elif opcion == "2":
            precio_maximo = float(input("Ingrese el precio máximo: "))
            autos_valor_max = auto_clasificado_por_valor_max(precio_maximo)
            if autos_valor_max:
                print(f"autos con precio máximo de ${precio_maximo}:")
                mostrar_autos(autos_valor_max)
            else:
                print(f"No se encontraron autos con un precio máximo de ${precio_maximo}.")

        elif opcion == "3":
            vin = input("Ingrese el VIN del auto: ")
            autos_or_vin = auto_clasificado_por_vin(vin)
            if autos_or_vin:
                print(f"Información del auto con VIN {vin}:")
                print(autos_or_vin)
                print()
            else:
                print(f"No se encontró un auto con el VIN {vin}.")

        elif opcion == "4":
            marca = input("Ingrese la marca de los autos: ")
            modelo = input("Ingrese el modelo de los autos: ")
            autos_or_ma_mo = auto_clasificado_por_ma_mo(marca, modelo)
            if autos_or_ma_mo:
                print(f"autos de la marca {marca} y modelo {modelo}:")
                mostrar_autos(autos_or_ma_mo)
            else:
                print(f"No se encontraron autos de la marca {marca} y modelo {modelo}.")

        elif opcion == "5":
            marca = input("Ingrese la marca de los autos: ")
            an_modelo = int(input("Ingrese el año de modelo de los autos: "))
            autos_or_ma_an_mo = auto_clasificado_por_ma_an_mo(marca, an_modelo)
            if autos_or_ma_an_mo:
                print(f"autos de la marca {marca} y año de modelo {an_modelo}:")
                mostrar_autos(autos_or_ma_an_mo)
            else:
                print(f"No se encontraron autos de la marca {marca} y año de modelo {an_modelo}.")

        elif opcion == "6":
            print("¡Gracias!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        print()


menu()