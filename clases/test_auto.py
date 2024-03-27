from auto import Auto

auto1= Auto("SUZUKI","VITARA SZ","2010")
auto1.mostrar_informacion(auto1)
auto1.actualizar_kilometraje(10)
auto1.realizar_viaje(50000)
auto1.estado_auto()

 #Metodo clase
toyot_auto=Auto.toyota_auto()
print(toyot_auto.__dict__)

#Metodo clase
auto_2=Auto.marca_auto(2000)
print(auto_2.__dict__)

#Metodo estatico
print(Auto.comparar_kilometraje(auto1, toyot_auto))

#Metodo estatico
print(Auto.comparar_año(auto_2, toyot_auto))