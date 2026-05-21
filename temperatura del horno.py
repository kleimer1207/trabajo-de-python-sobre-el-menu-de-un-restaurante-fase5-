continuar = "si"
while continuar== "si":
    temperatura = int(input("ingrese el valor de la temperataura:"))
    
    if temperatura >200:
        print("alerta:la temperatura es muy alta, por favor enfriar el horno]")
    elif temperatura < 180:
        print("alerta: la temperatura es muy baja, por favor calentar el horno")
    else:
        print("temperatura óptima")
    continuar = input("desea continuar con el monitoreo?, responda si o no:").strip().lower()
    
print ("el monitoreo a terminado, vuelva cuando quiera")
