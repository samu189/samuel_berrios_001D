productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
def main():
    while True:
        print("*"*70)
        print("***menu***")
        print("1. Stock marca")
        print("2. Búsqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")
        print("*"*70)
        opc=input("ingrese una opcion: ")
        return opc

def stock_marca(marca):
    marca = marca.lower()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            print(f"{modelo}: {stock[modelo][1]} unidades")
            encontrados = True
    if not encontrados:
        print("No hay stock en esa marca")

def busqueda_precio(p_min, p_max):
    lista = []
    for modelo, (precio, cantidad) in stock.items():
        if modelo in productos and cantidad > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            lista.append(f"{marca}--{modelo}")
    if lista:
        for item in sorted(lista):
            print(item)
    else:
        print("No hay productos en ese rango de precios")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

while True:
    opc=main()
    if opc == "1":
        marca = input("Ingrese la marca: ")
        stock_marca(marca)
    elif opc == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("solo puedes ingresar numeros enteros")
        busqueda_precio(p_min, p_max)
    elif opc == "3":
            while True:
                modelo = input("Ingrese el modelo: ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("solo puedes ingresar numeros enteros")
                    continue
                resultado = actualizar_precio(modelo, nuevo_precio)
                if resultado:
                    print("Precio actualizado con exito")
                else:
                    print("El modelo no existe en el programa")
                otra = input("¿Desea actualizar otro precio de notebook? (si/no): ").strip().lower()
                if otra != "si":
                    break
    elif opc == "4":
        print("saliendo del programa...")
        break
    else:
        print("Debe seleccionar una opción válida")

