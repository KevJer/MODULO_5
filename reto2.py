# import random

# aleatorios = random.randint(1,9)  
# aleatorios_dos = random.randint(1,9)

# if aleatorios == 4:
#     print("Te ganaste un chupete")
# elif aleatorios == 8:
#     print("Te ganaste un balon")
# elif aleatorios == 3 and aleatorios_dos == 7:
#     print("Te ganaste un televisor")
# else:
#     print("Perdiste!!")       
viaje = int(input("Ingrese una opccion"))
velocidad = int(input("Ingrese su velocidad"))

#   if velocidad >= 10 and 50 >= velocidad:
#     print("Velocidad permitida")
#   else:
#     print("Valocidad no permitida")


if viaje == 1:
    print("Viaje para Ecuador")  
    if 10 <= velocidad <= 50:
        print("Velocidad permitida en Zona Urbana")
    else:
        print("Velocidad no permitida en Zona Urbana")
    if 51 <= velocidad <= 70:
        print("Velocidad permitida en Zona Rural")
    else:
        print("Velocidad no permitida en Zona Rural")
    if 71 <= velocidad <= 90:
        print("Velocidad permitida en Zona Perimetral")
    else:
        print("Velocidad no permitida en Zona Perimetral")     
else:
    print("No hay ningún viaje asignado")



if viaje == 2:
    print("Viaje para Colombia")  
    if 10 <= velocidad <= 50:
        print("Velocidad permitida en Zona Urbana")
    else:
        print("Velocidad no permitida en Zona Urbana")
    if 51 <= velocidad <= 70:
        print("Velocidad permitida en Zona Rural")
    else:
        print("Velocidad no permitida en Zona Rural")
    if 71 <= velocidad <= 90:
        print("Velocidad permitida en Zona Perimetral")
    else:
        print("Velocidad no permitida en Zona Perimetral")     
else:
    print("No hay ningún viaje asignado")
    
    
    
    
if viaje ==3:
    print("Viaje para Perú")  
    if 10 <= velocidad <= 50:
        print("Velocidad permitida en Zona Urbana")
    else:
        print("Velocidad no permitida en Zona Urbana")
    if 51 <= velocidad <= 70:
        print("Velocidad permitida en Zona Rural")
    else:
        print("Velocidad no permitida en Zona Rural")
    if 71 <= velocidad <= 90:
        print("Velocidad permitida en Zona Perimetral")
    else:
        print("Velocidad no permitida en Zona Perimetral")     
else:
    print("No hay ningún viaje asignado")    