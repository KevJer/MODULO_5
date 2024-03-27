class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0) -> None:
        self.marca= marca
        self.modelo= modelo
        self.año= año
        self.kilometraje= kilometraje

    def mostrar_informacion(self, auto):
        return print(f"Información del auto: {auto.__dict__}")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje < self.kilometraje:
            print("No se puede reducir el kilometraje!!")
        else:
            self.kilometraje= kilometraje
        
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
             self.kilometraje=self.kilometraje + kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
             print("¡Ya déjame descansar por favor!")
    
    #Metodo clase
    @classmethod
    def toyota_auto(cls):
        marca= "Toyota"
        modelo="Lexus"
        año="2024"
        return cls(marca, modelo, año)
    
    #Metodo clase
    @classmethod
    def marca_auto(cls, kilometraje):
        marca= "Suzuki"
        modelo="Swift"
        año="2024"
        return cls(marca, modelo, año, kilometraje)
    

     #Metodo estatico
    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Los kilometraje son iguales"
        return "Los kilometraje son distimtos"

      #Metodo estatico
    @staticmethod
    def comparar_año(auto1, auto2):
        if auto1.año == auto2.año:
            return "Los año son iguales"
        return "Los año son distimtos"
 

    