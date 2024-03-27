from laptop import Laptop


# Herencia
class Laptop_Gaming(Laptop):
    def __init__(
        self, marca, procesador, memoria, tarj_grafica, costo=500, impuesto=10
    ):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarj_grafica = tarj_grafica

    def __str__(self):
        return f"marca:{self.marca}\n procesador: {self.precesador}\n   memoria:{self.memoria}\n tarj_grafica:{self.tarj_grafica}\n costo:{self.costo}"

    # sobreescritura de metodos
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico

    def realizar_diagnostico_juegos(self):
        juegos = ["FORNITE", "COD", "GTA"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarj_grafica:
                fps = fps_base * 3
            elif "GTX" in self.tarj_grafica:
                fps = fps_base * 2
            else:
                fps = fps_base

            resultados[juego] = f"{fps} FPS"
        return resultados
    pass

    def realizar_informe_uso(self):
        informe = super().realizar_metodo_uso()
        informe.update({
            "Tipo" : "Gaming",
            "Uso Recomendado": "JUego de video",
            "Horas de  uso": 10,
            "Recomedacion de software": {"antivirus", "virus"}
        })
        return informe
    pass
