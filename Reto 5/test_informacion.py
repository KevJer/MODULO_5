import informacion

print("Deseamos guardar la información de unos pacientes voluntarios de la cruz roja, tenemos sus nombres y el año en el que nacieron.")
print("************************** Por favor ingresar la información ************************** ")
count=0
for i in range(13):
    count+=1
    print(" ")
    print(f"Paciente numero: {count}")
    nombre_apellido= input("Ingresar el nombre y apellido: ")
    informacion.agregar_nombre(nombre_apellido)
    anio_nacimiento= int(input("Ingresar el año de nacimiento: "))
    informacion.agregar_edad(anio_nacimiento)
print(" ")
print("************************** LISTAS **************************")
print(f"Lista de nombres: {informacion.nombres}")
print(f"Lista de edades: {informacion.edad}")

mayor= max(informacion.edad) #Obtengo el mayor de la lista
menor= min(informacion.edad) #Obtengo el menor de la lista
posicionMax=informacion.edad.index(mayor) # Obtengo el indice del mayor de la lista
posicionMin=informacion.edad.index(menor) # Obtengo el indice del menor de la lista
nombre_mayor=informacion.nombres[posicionMax] #Obtengo el nombre en la poscion indicada del mayor de la lista 
nombre_menor=informacion.nombres[posicionMin]
print(" ")
print("************************** EL MAYOR DE LOS PACIENTES **************************")
print(f"{nombre_mayor} con la edad de {mayor} años es mayor a los demás pacientes. ")
print(f"{nombre_menor} con la edad de {menor} años es menor a los demás pacientes. ")
print(" ")   
    