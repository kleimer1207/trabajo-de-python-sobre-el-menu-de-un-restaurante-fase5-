menu = [ ["hambuergasa", 20000],
    ["ensalada", 10000],
    ["perro_caliente", 12000],
    ["empanadas", 3000],
    ["gaseosa", 2000],
    ["jugo_natural", 4500]


]

total_cuenta = 0
productos_comprados= []

continuar = "si"
while continuar == "si":
    print("--- BIENVENIDO, ACONTINUACION LE MOSTRAMOS NUESTRO MENU---")
    print("0. Hambuerguesa - $20000")
    print("1. ensalada - $10000")
    print("2. perro_caliente - $12000")
    print("3. empanadas - $3000")
    print("4. gaseosa - $2000")
    print("5. jugo natural - $4500")

    opcion = int(input("por favor ingrese el numero del producto que desea ordenar"))
    nombre_producto = menu[opcion][0]
    productos_comprados.append(nombre_producto)
    precio_producto = menu[opcion][1]

    total_cuenta = total_cuenta + precio_producto

    continuar = input ("¿desea continuaar? (si/no):")

if total_cuenta >= 30000:
    descuento = total_cuenta * 0.15
    total_con_descuento = total_cuenta - descuento
    print("gracias por tu compra y felicidades te has ganado un descuento del 15%.")
    print(f"total original: ${total_cuenta}")
    print(f"total con el descuento: ${total_con_descuento}")
else:
    print(f"su total a pagar es de: ${total_cuenta}")
    print("no aplicaste para el descuento, recuerda que para el descuento debes hacer una compra mayor o igual a $30000")

print(f"los productos que compraste fueron: {productos_comprados}")