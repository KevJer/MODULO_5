import random

aleatorios = random.randint(1,9)  
aleatorios_dos = random.randint(1,9)

if aleatorios == 4:
    print("Te ganaste un chupete")
elif aleatorios == 8:
    print("Te ganaste un balon")
elif aleatorios == 3 and aleatorios_dos == 7:
    print("Te ganaste un televisor")
else:
    print("Perdiste!!")       