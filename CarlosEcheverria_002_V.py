entradas_platinum = [""] * 20
entradas_gold = [""] * 30
entradas_silver = [""] * 50
asistentes = []
ganancias_platinum = 0
ganancias_gold = 0
ganancias_silver = 0
nombre = ""
apellido = ""
def nombre_user():
  global nombre
  global apellido
  print("Biendevenido a Creativos.cl")
  print("Ingrese su nombre: ")
  nombre = input()
  print("Ingrese su apellido: ")
  apellido = input()
def mostrar_menu():
  print()
  print("---------------MENU----------------")
  print("1) Comprar Entradas")
  print("2) Mostrar Ubicaciones Disponibles")
  print("3) Ver Listado De asistentes")
  print("4) Mostrar Ganancias totales")
  print("5) Salir")
def mostrar_ubicaciones_disponibles():
  variable_espaciado = 0
  print("Asientos disponibles: ")
  for repeticion in range(len(entradas_platinum)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_platinum[repeticion]==""):
      if variable_espaciado==11:
        print("")
      print(repeticion+1, end=" ")
    else:
      if variable_espaciado==11:
        print("")
      print("X",end=" ")
  for repeticion in range(len(entradas_gold)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_gold[repeticion]==""):
      if variable_espaciado==11 or variable_espaciado==21 or variable_espaciado==31 or variable_espaciado==41:
        print("")
      print(repeticion+21, end=" ")
    else:
      if variable_espaciado==11 or variable_espaciado==21 or variable_espaciado==31 or variable_espaciado==41:
        print("")
      print("X",end=" ")
  print()
  variable_espaciado = 0
  for repeticion in range(len(entradas_silver)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_silver[repeticion]==""):
      if variable_espaciado==11 or variable_espaciado==21 or variable_espaciado==31 or variable_espaciado==41 or variable_espaciado==51:
        print("")
      print(repeticion+51, end=" ")
    else:
      if variable_espaciado==11 or variable_espaciado==21 or variable_espaciado==31 or variable_espaciado==41 or variable_espaciado==51:
        print("")
      print("X",end=" ")
def comprar_entradas():
  global ganancias_platinum
  global ganancias_gold
  global ganancias_silver
  cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 o 2 o 3)"))
  if(cantidad <= 0 or cantidad >= 4):
    print("Error en la cantidad, debe ser 1 o 2 o 3")
    return
  print(cantidad)
  for repeticion in range(cantidad):
    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()
    ubicacion_valida = False
    while not ubicacion_valida:
      print("")
      ubicacion = int(input("Seleccione una ubicacion: "))
      if ubicacion >= 1 and ubicacion <= 100:
        if ubicacion <= 20 and entradas_platinum[ubicacion-1] == "":
          entradas_platinum[ubicacion-1] = ingresar_rut()
          ubicacion_valida = True
          ganancias_platinum = ganancias_platinum + 120000
          asistentes.append(entradas_platinum[ubicacion -1])
        elif ubicacion <= 50 and entradas_gold[ubicacion-21] == "":
          entradas_gold[ubicacion-21] = ingresar_rut()
          ubicacion_valida = True
          ganancias_gold = ganancias_gold + 80000
          asistentes.append(entradas_gold[ubicacion -21])
        elif ubicacion <= 100 and entradas_silver[ubicacion-51] == "":
          entradas_silver[ubicacion-51] = ingresar_rut()
          ubicacion_valida = True
          ganancias_silver = ganancias_silver + 50000
          asistentes.append(entradas_silver[ubicacion -51])
        if not ubicacion_valida:
          print("No esta disponible")
    print("Operación realizada exitosamente")
def ingresar_rut():
  run_valido = False
  while not run_valido:
    run = input("Ingrese el RUN sin Digito Verificador ni guiones:")
    if(len(run) == 7 or len(run) == 8):
      run_valido = True
  return run
def mostrar_asistentes():
  print("Listado de asistentes")
  asistentes.sort()
  for asistente in asistentes:
    print(asistente, end=".")
def mostrar_ganancias():
  print ("Ganancias por seccion!")
  print (ganancias_platinum)
  print (ganancias_gold)
  print (ganancias_silver)
def exit():
  print("Gracias por usar nuestro Sofware",nombre,apellido)
def inicio():
  try:
    while True:
      nombre_user()
      mostrar_menu()
      opcion = int(input("Ingrese opcion: "))
      if opcion == 1:
        comprar_entradas()
      elif opcion == 2:
        mostrar_ubicaciones_disponibles()
      elif opcion == 3:
        mostrar_asistentes()
      elif opcion == 4:
        mostrar_ganancias()
      elif opcion == 5:
        exit()
        break
  except:
    print("Ha ocurrido un error")
inicio()
