contador = 1
numero_empleados = int(input('Ingrese el número de empleados: '))
planilla = []

while contador <= numero_empleados:
    departamento = input('Ingrese el departamento al que pertenece: ')
    nombre = input('Ingrese el nombre del empleado: ')
    salario = float(input('Ingrese el Salario: '))

    # Calcular bono según el departamento
    if departamento == "rrhh":
        bono = salario * 0.10
    elif departamento == "ventas":
        bono = salario * 0.20
    else:
        bono = 0

    # Calcular descuentos (ISSS, AFP, Renta)
    descuento_isss = salario * 0.03
    descuento_afp = salario * 0.0725
    if salario > 1000:
        descuento_renta = salario * 0.10
    else:
        descuento_renta = 0

    # Calcular salario neto
    salario_neto = salario + bono - descuento_isss - descuento_afp - descuento_renta

    # Guardar los valores en un arreglo
    empleado = {
        'nombre': nombre,
        'departamento': departamento,
        'salario': salario,
        'bono': bono,
        'descuento_isss': descuento_isss,
        'descuento_afp': descuento_afp,
        'descuento_renta': descuento_renta,
        'salario_neto': salario_neto
    }
    planilla.append(empleado)

    contador += 1

# Mostrar los datos de la planilla en pantalla
for empleado in planilla:
    print("\nNombre:", empleado['nombre'])
    print("Departamento:", empleado['departamento'])
    print("Salario:", empleado['salario'])
    print("Bono:", empleado['bono'])
    print("Descuento ISSS:", empleado['descuento_isss'])
    print("Descuento AFP:", empleado['descuento_afp'])
    print("Descuento Renta:", empleado['descuento_renta'])
    print("Salario Neto:", empleado['salario_neto'])