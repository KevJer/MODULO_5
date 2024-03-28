from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def __str__(self):
         return f"Marca: {self.marca} \n Procesador: {self.precesador} \n Memoria: {self.memoria} \n Almacenamiento: {self.almacenamiento} \n Duracion de Bateria: {self.duracion_bateria} \n  Costo: {self.costo} \n Impuesto: {self.impuesto} \n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Almacenamiento"] = f"{self.almacenamiento} GB"
        resultado_diagnostico["Duración de Batería"] = f"{self.duracion_bateria} horas"
        resultado_diagnostico["Conectividad de Red"] = resultado_conectividad
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi": random.choice([True, False]),
            "Acceso a Servidores Empresariales": random.choice([True, False]),
            "Latencia de Red": random.randint(1, 100) 
        }
        return conectividad

    pass