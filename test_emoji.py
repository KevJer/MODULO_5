import emoji

cantidad_frase = int(input("Cuantas frases deseaingresar: "))
for i in range(cantidad_frase):
    frase=input("Ingresa la frase")
    emoji.econtrar_palabra(frase)
    emoji.agregar_frase(frase)