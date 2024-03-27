import random


class Laptop:
    # Metodo constructor
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca = marca
        self.precesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto

    def valor_descuento(self, descuento):
        return (self.costo * descuento) / 100

    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.precesador}",
            "MEMORIA RAM": "OK" if self.memoria >= 8 else "Aumentar memoria",
            "BATERIA": "OK" if random.choice([True, False]) else "Cambiar Bateria",
        }

        return resultado

    def realizar_metodo_uso(self):
        reultado_informe = {
            "Tipo" : "GEnerica",
            "Uso Recomendado": "Tareas cotidianas",
            "Horas de  uso": 5,
            "Diagnostico actual": self.realizar_diagnostico_sistema()
        }
        return reultado_informe

    # Metodo Estatico
    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"

    # Metodo de clase
    @classmethod
    def asus_laptop(cls, costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria, costo)