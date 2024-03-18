# Se definen las tasas de deducción
tasa_isss = 0.03
tasa_afp = 0.0625
tasa_renta = 0.071

# Se realiza lista para almacenar los detalles de los empleados
detalles_empleados = []

contador = 1
numero_empleados = int(input('Ingrese el número de empleados: '))
while contador <= numero_empleados:

    departamento = input('Ingrese el departamento al que pertenece: ')
    nombre = input('Ingrese el nombre del empleado: ')
    salario = float(input('Ingrese el salario: '))
    contador = contador + 1

    if departamento == "rrhh":
        bono = salario * 0.10
    elif departamento == "ventas":
        bono = salario * 0.20
    else:
        bono = 0

    descuento_isss = salario * tasa_isss
    descuento_afp = salario * tasa_afp
    descuento_renta = salario * tasa_renta

    salario_neto = salario + bono - descuento_isss - descuento_afp - descuento_renta

    # Se guardara los detalles del empleado en un diccionario
    detalles_empleado = {
        'nombre': nombre,
        'departamento': departamento,
        'salario': salario,
        'bono': bono,
        'descuento_isss': descuento_isss,
        'descuento_afp': descuento_afp,
        'descuento_renta': descuento_renta,
        'salario_neto': salario_neto
    }

    detalles_empleados.append(detalles_empleado)

    contador += 1

# Se mostrara los resultados de los empleados
print("\nDetalles de los empleados:")
for empleado in detalles_empleados:
    print(f"Nombre: {empleado['nombre']}")
    print(f"Departamento: {empleado['departamento']}")
    print(f"Salario: ${empleado['salario']:.2f}")
    print(f"Bono: ${empleado['bono']:.2f}")
    print(f"Descuento ISSS: ${empleado['descuento_isss']:.2f}")
    print(f"Descuento AFP: ${empleado['descuento_afp']:.2f}")
    print(f"Descuento Renta: ${empleado['descuento_renta']:.2f}")
    print(f"Salario Neto: ${empleado['salario_neto']:.2f}")
    print()
