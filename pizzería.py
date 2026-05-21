precios = [0,10000,15000,20000,25000,35000]
porciones = [0,2,4,6,8,12]
ventas_por_tipo = [0,0,0,0,0,0]
total_dinero = 0
total_porciones = 0
num_clientes = int(input("¿cuantos clientes son?:"))

for i in range(num_clientes):
        print(f"n\--- pedido del cliente #{i+1} ---")

        while True: 
            tipo= int(input("¿que tipo de pizza quiere ordenar? (1-5 o 0 para terminar)"))
            if tipo == 0:
                break
            elif  1<= tipo <=5:
                total_dinero += precios [tipo] 
                total_porciones += porciones [tipo]
                ventas_por_tipo[tipo]+= 1
            else:
                print("valor no encontrado, por favor digitar un valor del 1 al 5")

print("\n--- REPORTE FINAL ---")
print(f"total de dinero: {total_dinero}")
print(f"total de porciones: {total_porciones}")
print(f"ventas por tipo: {ventas_por_tipo[1:]}")









