# planetas = ["Venus", "Tierra", "Marte", "Jupiter"]
# print(planetas[1:3])
# print(len(planetas))
# gravedad = [0.1, 0.2, 0.3, 0.4]
# peso_bus = 123
# print(f"Tierra {peso_bus}")
# print(f"En Marte el peso de bus es {peso_bus * gravedad[2]}")
Menu = ["Encebollado", "Seco", "camarones"]
# listas2 = [10, 11, 12, 13]
# listas3 = [14, 15, 16, 17]
# # listas.append(7)
# # listas.insert(2, "Kevin")
# # listas.extend([6,7,8,9])
# listaUnida = listas2 + listas3
# print(3 in listas)
# print(listas.index(2))
# # print(listas)
# listas.pop(3)
# listas.remove("Kevin")
# listas.sort(reverse = True)
# # listas.reverse()
# print(listas)

# Menu.append("Papas")
# Menu.remove("camarones")
# print(Menu.index("Papas"))
# print(Menu)


print("MENU")
print("1. Añadir plato")
print("2. Buscar en el menu")
print("3. Eliminar plato del menu")
print("4. Mostrar platos del menu")
opccion = int(input("seleccione la opccion"))
if opccion == 1:
  addPlato = input("ingresa un nuevo plato para el menu")
  Menu.append(addPlato)
else:
  if opccion == 2:
      search = input("Ingrese el plato a buscar")
      print(Menu.index(search))
  else:
    if opccion == 3:
      delete = input("Ingrese el pato a eliminar")
      Menu.remove(delete)
    else:
      if opccion == 3:
        m
      else:
        pass