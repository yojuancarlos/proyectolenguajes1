def parametros ():
    cantidad_terminal= int
    lista_terminales=[]
    lista_noterminales=[]

    cantidad_terminal = input("escriba la cantidad de termniales que desea ingresar:")

    for i in range(int(cantidad_terminal)):

        lista_terminales.append(input("escriba el termninal : "))

        lista_noterminales.append(input("escriba el no terminal : "))

    print(lista_terminales)
    print(lista_noterminales)

parametros()