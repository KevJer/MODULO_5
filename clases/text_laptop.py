from laptop import Laptop
from laptop_gaming import Laptop_Gaming


laptop_juanito = Laptop_Gaming("MSI", "i7", 4, "RTX 8GB")

print(laptop_juanito.realizar_diagnostico_sistema())
# print(laptop_kevin.costo)


# laptop_pepito = Laptop("lenovo", "17", 32)
# laptop_maria = Laptop("lenovo", "19", 35,40)
# print(laptop_pepito.__dict__)

# print(laptop_pepito.valor_final())       
# print(f"El valor descuento: {laptop_pepito.valor_descuento(10)}")       

# # for item in range(1,100):
# #     asus_laptop= Laptop.asus_laptop(1000)
#     # print(asus_laptop.__dict__)


# print(Laptop.comparar_costo(laptop_pepito,laptop_maria))