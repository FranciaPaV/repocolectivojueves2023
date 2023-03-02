controlador=100

print('************EMPANDADAS EL MACHETICO************')
print('1. Agregar un sabor de empanada')
print('2. Ver el sabor de empanada registrado')
print('3. Salir')

while controlador!=3:
    controlador=int(input("Digita una opcion: "))
    if(controlador==1):
        sabor=input("Ingresa el sabor que quieres: ")
    elif(controlador==2):
        print(f"Elegiste {sabor}")
    elif(controlador==3):
        print('Elegiste la opcion 3')
    else:
        print("Elige una opcion valida")
    