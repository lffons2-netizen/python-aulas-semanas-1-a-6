def checar():
    print("função chamada")
    return True
resultado = False and checar()  # nunca imprime
