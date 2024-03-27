
class Laptop:
    #Constructor:
    def __init__(self, marca, procesador, memoria, costo= 500, impuesto= 10):

        #Metodo instamcia
        self.marca= marca
        self.procesador= procesador
        self.memoria= memoria
        self.costo= costo
        self.impuesto= impuesto

    def valor_final(self):
        return (self.costo + self.impuesto)
    
    def valor_descuento(self, descuento):
        return(self.costo * descuento)/100
    
    # @staticmethod
    # def comparar_costo(laptop1, laptop2):
    #     if laptop1.costo == laptop2.costo:
    #         return "Los costos son iguales"
    #     return "Los costos son distimtos"
    
    #     #Metodo clase
    # @classmethod
    # def asus_laptop(cls, costo):
    #     marca="asus"
    #     procesador="i5"
    #     memoria=16
    #     return cls(marca, procesador, memoria, costo)

laptop_pepito = Laptop("lenovo", "17", 32)
print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final())       
print(f"El valor descuento: {laptop_pepito.valor_descuento(10)}")       