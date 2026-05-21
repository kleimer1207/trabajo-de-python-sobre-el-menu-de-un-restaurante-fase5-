DATOS_DE_EMPLEADOS = [
    {"nombre": "Ana García", "horas": 160, "tarifa": 15.5},
    {"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0},
    {"nombre": "Marta López","horas": 165, "tarifa": 12.0}
]

TASA_DE_DESCUENTO = 0.15 

def calcular_bruto (horas,tarifa):
    """calcular salario bruto del empleado"""
    return horas * tarifa

def calcular_neto (salario_bruto):
    """calcular salario neto del empleado después de aplicar el descuento"""
    descuento = salario_bruto * TASA_DE_DESCUENTO
    return salario_bruto - descuento

def generar_informe (lista_empleados):
    for empleado in lista_empleados:
        nombre = empleado['nombre']
        horas = empleado['horas']
        tarifa = empleado['tarifa']
        salario_bruto = calcular_bruto(horas, tarifa)
        salario_neto = calcular_neto(salario_bruto)
        print(f"empleado {nombre}: salario_neto: ${salario_neto:.2f}")
generar_informe(DATOS_DE_EMPLEADOS)
