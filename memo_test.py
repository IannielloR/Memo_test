from random import randint

def crear_tab(tamaño: int) -> list:
    """
    Pre-condiciones: (tamaño: int) tamaño para crear el tablero
    Post-condicion: devuelve una lista
    Funcion para crear tableros de tamaño x tamaño, que contiene pares de numeros 
    y cada par es un numero random entre el 10 y el 100
    """
    mitad = int((tamaño*tamaño)/2) 
    tablero = []
    cartas = []
    cartas_repetidas = []
    cont = 0

    #Creo una lista random con la mitad de la cantidad de cartas
    for i in range(mitad): 
        cartas.append(randint(10,100))
        while cartas[i] in cartas_repetidas:
            cartas[i] = randint(10,100)
        cartas_repetidas.append(cartas[i])

    for i in range(len(cartas_repetidas)):
        cartas_repetidas[i] = 0

    #Voy creando la matriz con los numeros de la lista,
    #si el numero no se repitio (que no esta en "cartas repetidas"), se agrega a "cartas repetidas"
    #Si el numero se repite (que esta en "cartas repetidas"), se borra de la lista
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            cant_cartas= ((len(cartas)-1))
            num = randint(0,cant_cartas)
            fila.append(cartas[num])   
            carta = cartas[num]
       
            if ((cartas[num] in cartas_repetidas) and (cant_cartas !=0)):
                cartas.pop(num)
                cant_cartas= (len(cartas))
                
            if (carta in cartas):
                if cartas[num] not in cartas_repetidas:
                    cartas_repetidas[cont] = cartas[num]
                    cont +=1    

        tablero.append(fila)

    return tablero

def crear_tab_nulo(tamaño: int)-> list:
    """
    Pre-condicion: (tamaño: int) tamaño del tablero a crear
    Post-condicion: devuelve una lista, tablero de tamaño x tamaño 
    Crea un tablero con todos sus lugares = 0
    """
    tablero = []
    
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            fila.append(0)
        tablero.append(fila)
    
    return tablero

def copiar_tab(tablero_original: list)-> list:
    """
    Pre-condicion: (tablero a copiar: list),
    Post-condicion: devuelve el tablero de tipo list copiado sin que se pasen los datos por referencia
    crea una copia del tablero sin pasar los datos por referencia 
    """
    tablero_copia = []
    for i in range(len(tablero_original)):
        fila = []
        for j in range(len(tablero_original)):
            fila.append(tablero_original[i][j])
        tablero_copia.append(fila)

    return tablero_copia 

def mostrar_tablero(tablero: list, nro_tablero: int)-> None:
    """
    Pre-condicion: (tablero: list, nro_tablero: int) 
    Post-condicion: No devuelve nada
    Muestra el tablero con las cartas dadas vuelta
    """
    print("\nTablero ", nro_tablero, ": ")
    for i in range(len(tablero)):
        print(tablero[i])

def mostrar_tablero_oculto(tablero: list)-> None:
    """
    Pre-condicion: (tablero: list)
    Post-condicion: no devuelve nada
    Muestra todas las cartas del tablero de forma oculta y las cartas eliminadas como espacios en blanco
    """
    fila = []
    for i in range(len(tablero)):
        i_str= str((i+1))   
        fila.append(i_str)
    print("\n ",fila)

    for i in range((len(tablero))):
        fila = []
        for j in range(len(tablero)):
            if((tablero[i][j] != 0)):
                #Los espacios que son c, son cartas que todavia no descubrieron
                fila.append("C")
            elif tablero[i][j] == 0 :
                #Los espacios que son 0, son cartas que ya descurbieron 
                fila.append(" ")
        print((i+1),fila)

def eleccion_de_cartas(tablero: list, espacio_a_ingresar: str)-> int:
    espacio = input(espacio_a_ingresar)
    while ((espacio.isalpha()) or (int(espacio)> len(tablero)) or (int(espacio) <= 0)):
        print("Error intentelo de nuevo")
        espacio = input(espacio_a_ingresar)
    
    return int(espacio)

def modificar_tablero(tablero: list)-> list:
    """
    Pre-condicion: (tablero: list)
    Post-condicon: devuelve el tablero de tipo list modificado o no
    Funcion donde el usuario elije las cartas y si son iguales las vuelve 0
    """
    espacio_x = 0
    espacio_y = 0
    espacio_x2 = 0
    espacio_y2 = 0
    while ((espacio_x == espacio_x2) and (espacio_y == espacio_y2)):

        print("\n")  
        espacio_x = eleccion_de_cartas(tablero,"Ingrese la fila de la 1er carta: ")
        espacio_y = eleccion_de_cartas(tablero,"Ingrese la columna de la 1er carta: ")
        espacio_x2 = eleccion_de_cartas(tablero,"Ingrese la fila de la 2da carta: ")
        espacio_y2 =eleccion_de_cartas(tablero,"Ingrese la columna de la 2da carta:  ")      

        if ((espacio_x == espacio_x2) and (espacio_y == espacio_y2)):
            print("\nEsta elijiendo solo una carta, intente de nuevo,  i: ")

    #Si las cartas son iguales se modifican
    if (tablero[((espacio_x)-1)][((espacio_y)-1)] == tablero[((espacio_x2)-1)][((espacio_y2)-1)]):
        print("son iguales")
        tablero[((espacio_x)-1)][((espacio_y)-1)] = 0
        tablero[((espacio_x2)-1)][((espacio_y2)-1)] = 0
        
    mostrar_tablero_oculto(tablero)
    
    return tablero

def carta_fatality(tablero: list)-> list:
    """
    Pre-condicion: (tablero: list) 
    Post-condicion: devuelve el tablero de tipo list
    Traspone el tablero ingresado
    """
    tablero_trans = []
    for i in range(len(tablero)):
        fila = []
        for j in range(len(tablero)):
            fila.append(tablero[j][i])
        tablero_trans.append(fila)

    tablero_trans = modificar_tablero(tablero_trans)
    for i in range(len(tablero_trans)):
        fila = []
        for j in range(len(tablero_trans)):
            tablero[i][j] = (tablero_trans[j][i])

    return tablero

def carta_toti(tablero: list)->list:
    """
    Pre-condicion: (tablero: list) 
    Post-condicion: devuelve el tablero de tipo list
    Espeja el tablero de forma azarosa,de forma horizontal o vertical.
    """
    tablero_espejado = []
    horizontal = randint(0,1)
    #Para espejarla: cuento la cantidad de casilleros y a medida que suma j o i, 
    #se lo descuento a la cantidad del tablero -1
    #Ejemplo: len(tablero) = 12 | j = 0 entonces (12-1)-0 = posicion 11
    if (horizontal == 1):
        for i in range(len(tablero)):
            fila = []
            for j in range(len(tablero)):
                fila.append(tablero[i][((len(tablero)-1)-j)])
            tablero_espejado.append(fila)
    else:
        for i in range(len(tablero)):
            fila = []
            for j in range(len(tablero)):
                fila.append(tablero[((len(tablero)-1)-i)][j])
            tablero_espejado.append(fila)

    tablero_espejado = modificar_tablero(tablero_espejado)
    
    #Se vulve a espejar el tablero de la misma forma que antes para volverlo a la normalidad
    if (horizontal == 1):
        for i in range(len(tablero_espejado)):
            for j in range(len(tablero_espejado)):
                tablero[i][j] = tablero_espejado[i][((len(tablero_espejado)-1)-j)]  
    else: 
        for i in range(len(tablero_espejado)):
            for j in range(len(tablero_espejado)):
                tablero[i][j] = tablero_espejado[((len(tablero_espejado)-1)-i)][j]

    return tablero

def carta_layout(tablero: list)-> list:
    """
    Pre-condicion: (tablero: list) 
    Post-condicion: devuelve el tablero de tipo list
    Espeja el tablero de forma azarosa,de forma horizontal o vertical.
    """
    lista_descarte = []
    tablero_random = []
    #Se crea una lista, donde se copian los numeros del tablero
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            lista_descarte.append(tablero[i][j])
    
    #Y se crea un tablero donde se le asignan esos numeros de forma random
    #y al asignarse el numero se borra de la lista
    for i in range(len(tablero)):
        fila = []
        for j in range(len(tablero)):
            cant_cartas= ((len(lista_descarte)-1))
            num = randint(0,cant_cartas)
            fila.append(lista_descarte[num]) 
            lista_descarte.pop(num)
        tablero_random.append(fila)

    tablero_random= modificar_tablero(tablero_random)
    #Se le agregan los datos del tablero ya modificado a la lista vacia "lista_descarte" 
    #mientras las cartas no se hayan descubierto
    for i in range(len(tablero_random)):
        for j in range(len(tablero_random)):
            if (tablero_random[i][j] != 0):
                lista_descarte.append(tablero_random[i][j])

    #Se fija si los valores del tablero estan el la lista, sino esta
    # quiere decir que las descubrio el jugador y se "borran" 
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] not in lista_descarte:
                tablero[i][j] = 0 

    return tablero

def mostrar_puntaje(puntaje: list) -> None:
    """
    Pre-condicion: (puntaje: list) 
    Post-condicion: no devuelve nada
    Muestra el puntaje ordenado de mayor a menor
    """
    """
    #Para no modificar el puntaje original creo un puntaje auxiliar
    puntaje_ordenado = []
    for i in range(len(puntaje)):
        fila = []
        for j in range(len(puntaje[i])):
            fila.append(puntaje[i][j])
        puntaje_ordenado.append(fila)

    #Si el puntaje en [(i-1)] es menor al puntaje[i], se intercambian los lugares del [(i-1)] y del [i]    
    for i in range(len(puntaje_ordenado)):
        if (( i != 0) and (puntaje_ordenado[i][1] > puntaje_ordenado[(i-1)][1])):
            jug_aux = puntaje_ordenado[(i-1)]
            pun_aux = puntaje_ordenado[(i-1)][1]
            puntaje_ordenado[(i-1)] = puntaje_ordenado[i]
            puntaje_ordenado[(i-1)][1] = puntaje_ordenado[i][1]  
            puntaje_ordenado[i] = jug_aux
            puntaje_ordenado[i][1]= pun_aux
    """
    puntaje_ordenado = sorted( puntaje, reversed = True)
    
    for i in range(len(puntaje_ordenado)):
        print(puntaje_ordenado[i])

def modificar_puntaje(ganador: str, puntaje: list) -> list:
    """
    Pre-condicion: (ganador: str, puntaje: list)  
    Post-condicion: devuelve el puntaje modificado, tipo lista
    Actualiza el puntaje, agrega al ganador de la ultima partida y saca al de la primer partida, mientras que la cantidad de partidas sea iguala 4
    """
    sumatoria_puntaje = 0
    ganador_existe = 0
    #La matriz del puntaje no esta ordenada de mayor a menos, solo se muestra de esa forma
    #Entra en la funcion cuando alguien gano
    #La cantidad de puntajes no puede ser mayor a 4

    for i in range(len(puntaje)):
        sumatoria_puntaje += puntaje[i][1]

    #Si la persona que esta en el primer espacio tiene un punto y la sumatoria de puntos da 4 => se borra el lugar de memoria  
    if ((sumatoria_puntaje == 4) and (puntaje[0][1] == 1)):
        puntaje.pop(0)
    #Sino solo se le resta un punto
    elif ((sumatoria_puntaje == 4) and (puntaje[0][1] > 1)):
        puntaje[0][1] -= 1
    
    #Si el ganador ya esta en el puntaje solo se le suma el punto, sino se agrega a la lista
    for i in range(len(puntaje)):
        if ganador == puntaje[i][0]:
            puntaje[i][1] += 1
            ganador_existe = 1

    if ganador_existe == 0:
        fila = [ganador, 1]
        puntaje.append(fila)  

    return puntaje    

def sumar_cartas_especiales( mazo: dict, config: list)-> dict:
    """
    Pre-condicion: (mazo: dict, configuracion: list) 
    Post-condicion: devuelve el mazo modificado, tipo dict
    Agrega o no una carta especial al mazo 
    """
    carta = randint(1,5)
    #Si el numero es de 1 a 4 es una de las cartas, si sale el 5 no es ninguna

    prov = randint(1,100)
    #Al cada carta tener una prob propia se hacer otro random,
    #si el numero que sale es menor o igual a la probabilidad dicha se agrega
    if ((carta == 1) and (prov < config[1])):
        mazo["REPLAY"] += 1 
    if ((carta == 2) and (prov < config[2])):
        mazo["LAYOUT"] += 1 
    if ((carta == 3) and (prov < config[3])):
        mazo["TOTI"] += 1 
    if ((carta == 4) and (prov < config[4])):
        mazo["FATALITY"] += 1 
    return mazo

def eleccion_de_tablero(tablero: list, pregunta: list)-> list:
    """
    Pre-condicion: (tablero: list, pregunta: list) 
    Post-condicion: devuelve el tablero, ya modificado
    Dependiendo de la carta que haya elegido el jugador contrario se modifica el tablero o no
    """
    mostrar_tablero_oculto(tablero)
    if ((pregunta[0] in "SI") and (pregunta[1] not in "REPLAY")):
        if (pregunta[1] in "LAYOUT"):
            tablero = carta_layout(tablero)
        if (pregunta[1] in "TOTI"):
            tablero = carta_toti(tablero)
        if(pregunta[1] in "FATALITY"):
            tablero = carta_fatality(tablero)
    else:
        tablero = modificar_tablero(tablero)
    return tablero
    
def eleccion_cartas(mazo: list,pregunta: list)-> list:
    """
    Pre-condicion: (mazo: list, pregunta: list) 
    Post-condicion: devuelve la pregunta (tipo list), con la respuesta del jugador y la carta 
    Funcion donde el jugador elige si quiere usar una tabla del mazo
    """
    #recorre el mazo del jugador
    for carta in mazo:
        if ((mazo[carta] != 0) and (pregunta[0] not in "SI")):
            #Si tiene cartas, se muestra de una en una y se pregunta si la quiere usar
            print("\nTiene {} cartas de {}".format(mazo[carta], carta))
            pregunta[0]= input("¿Desea usar una de las cartas? si = si | no = no: ").upper()
            while (((pregunta[0].isalpha()) != "true") and ((pregunta[0] not in "SI") and (pregunta[0] not in "NO"))):
                #Si no ingreso si ni no, se le vuelve a preguntar
                print("\nError")
                pregunta[0]= input("¿Desea usar una de las cartas? si = si | no = no: ").upper()
            if pregunta[0] in "SI":  
                #Si ingreso que si se guarda la carta que quiere en pregunta
                pregunta[1] = carta

    return pregunta

def manipulacion_tablero_auxiliar(tablero: list, pregunta: list)-> list:
    """
    Pre-condicion: (tablero: list, pregunta: list) 
    Post-condicion: devulve el tablero (tipo list) modificado
    Utiliza la copia del tablero original para que el usuario juegue y lo devulve
    """
    tablero_mod = []
    tablero_mod = copiar_tab(tablero)
    tablero_mod = eleccion_de_tablero(tablero_mod, pregunta)
    
    return tablero_mod

def partida(jug1 :str, jug2: str, config: list, puntaje: list)-> None:
    """
    Pre-condicion: (jugador1 :str, jugador2: str, configuracion: list, puntaje: list) 
    Post-condicion: No devuelve nada
    Realiza las partidas 
    """
    tablero0 = crear_tab_nulo(config[0]) #El todos los datos del tablero son 0
    tablero1 = crear_tab(config[0])
    tablero2 = crear_tab(config[0])
    juego_terminado = False
    turno = 0
    cartas_jug1 = {}
    cartas_jug1["REPLAY"] = 1
    cartas_jug1["LAYOUT"] = 0
    cartas_jug1["TOTI"] = 1
    cartas_jug1["FATALITY"] = 0
    cartas_jug2 = {}
    cartas_jug2["REPLAY"] = 0
    cartas_jug2["LAYOUT"] = 0
    cartas_jug2["TOTI"] = 0
    cartas_jug2["FATALITY"] = 0 
    pregunta = [" "," "] #En el [0] se ingresa si el jugador quiere usar la carta ("SI" o "NO"), y en [1] el nombre de la carta que quiere jugar 

    mostrar_tablero(tablero1,1)
    mostrar_tablero(tablero2,2)

    while (juego_terminado == False):
        if (turno == 0):

            print("\nTurno del jugador: ", jug1)
            tablero_mod = manipulacion_tablero_auxiliar(tablero2,pregunta) 
            #Creo una copia del tablero para que el usuario juegue con el, despues la comparo con la original
            #si son distintos quiere decir que el usuario encontro un par y puede tirar otra vez 
            if tablero2 != tablero_mod:
                turno = 2 

            tablero2 = tablero_mod
            cartas_jug1 = sumar_cartas_especiales(cartas_jug1, config) 
            pregunta[0] = "NO"
            pregunta = eleccion_cartas(cartas_jug1, pregunta)

            if (pregunta[1] in cartas_jug1) and (pregunta[0] == "SI"):
                #Borra la carta que eligio el jugador de su mazo
                cartas_jug1[pregunta[1]] -= 1
                
            if (pregunta[1] in "REPLAY") and (pregunta[0] == "SI"):
                #Si la carta que eligio el jugador es replay puede volver a jugar
                turno = 2
                
            if tablero2 == tablero0:
                #Si cuando el tablero del jugador tiene todos los espacios con 0, entonces gano 
                puntaje = modificar_puntaje(jug1,puntaje)
                juego_terminado = True
                
            elif turno == 2:
                turno = 0
                #Es para que la carta que eligio no afecte el tablero de vuelta del jugador
                pregunta[0] = "NO"
            else:
                turno = 1
            
        if (turno == 1):
            print("\nTurno del jugador: ", jug2)
            tablero_mod = manipulacion_tablero_auxiliar(tablero1,pregunta) 
            if tablero1 != tablero_mod:
                turno = 2 

            tablero1 = tablero_mod
            cartas_jug1 = sumar_cartas_especiales(cartas_jug2, config) 
            pregunta[0] = "NO"
            pregunta = eleccion_cartas(cartas_jug2, pregunta)

            if (pregunta[1] in cartas_jug2) and (pregunta[0] == "SI"):
                cartas_jug2[pregunta[1]] -= 1
            
            if (pregunta[1] in "REPLAY") and (pregunta[0] == "SI"):
                turno = 2
                
            if tablero1 == tablero0:
                puntaje = modificar_puntaje(jug2,puntaje)
                juego_terminado = True
       
            elif turno == 2:
                turno = 1

                pregunta[0] = "NO"
            else:
                turno = 0

def eleccion_de_probabilidad( probabilidad_a_ingresar: str)-> int:
    """
    Pre-condicion: ( probabilidad_a_ingresar: str)
    Post-condicion: devuelve la probabilidad ingresada por el usuario
    Relaiza la comprobacion de que el usuario haya ingresado bien la probabilidad
    """
    probabilidad = input(probabilidad_a_ingresar)
    while ((probabilidad.isalpha()) or (int(probabilidad) > 100)):
        print("Error al ingresar la probabilidad, vuelva a intentarlo")
        probabilidad = input(probabilidad_a_ingresar)
    
    return int(probabilidad)

def configuracion()-> list:
    """
    Pre-condicion: No tiene parametros
    Post-condicion: devuelve los parametros, tipo list
    Realiza la configuracion del juego, se elije el tamaño del tablero y las probabilidades
    """
    print("Configuracion")
    duracion =input("Elegir tamaño Corto(4x4), Medio(8x8) o Largo(12x12): ").upper()
    while (duracion not in "C") and (duracion not in "M") and (duracion not in "L"):
        print("\nError al ingresar el tamaño, intentelo nuevamente")
        duracion =input("Elegir tamaño Corto(4x4), Medio(8x8) o Largo(12x12): ").upper()

    if duracion == "C":
        duracion = 4
    if duracion == "M":
        duracion = 8
    if duracion == "L":
        duracion = 12

    print("\nProbabilidades: (cada probabilidad no puede ser mayor a 100)")

    prob_replay = eleccion_de_probabilidad("Ingresar la probabilidad de Replay: ") 
    prob_layout = eleccion_de_probabilidad("Ingresar la probabilidad de Layout: ") 
    prob_toti = eleccion_de_probabilidad("Ingresar la probabilidad de Toti: ") 
    prob_fatality = eleccion_de_probabilidad("Ingresar la probabilidad de Fatality: ") 

    config=[duracion, prob_replay, prob_layout, prob_toti,prob_fatality]
    return config

def main()-> None:
    puntaje = []
    config = [4,100,100,100,100]
    print("Bienvenido a Reglas... Reglas...\nMenu")
    print("A-Comenzar partida \nB-Configuracion \nC-Score \nD-Salir")
    opc= input("Ingrese su eleccion: ").upper()
    while (opc not in "D") and ((opc.isalpha())): 
        if opc == "A":
            jug1 = input("\nIngrese el nombre del jugador 1: ")
            jug2 = input("\nIngrese el nombre del jugador 2: ")
            if (jug1.isalnum) and (jug2.isalnum):
                partida(jug1, jug2, config, puntaje) 
            opc = " "
            
        elif opc.upper() == "B":
            config = configuracion()
            opc = " "
    
        elif opc.upper() == "C":
            mostrar_puntaje(puntaje)
            opc = " "
        else:
            print("\nError al ingresar la opcion, intentelo nuevamente")
            print("\nA-Comenzar partida \nB-Configuracion \nC-Score \nD-Salir")
            opc= input("Ingrese su eleccion: ").upper()
        
        print(opc)
        print("\nA-Comenzar partida \nB-Configuracion \nC-Score \nD-Salir")
        opc= input("Ingrese su eleccion: ").upper()
    
main()