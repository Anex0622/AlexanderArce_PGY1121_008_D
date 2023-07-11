def menú():
    while True:
        try:
            eleccion = input("""\tBienvenido a la venta de entradas de Michael Jam!
            1. compra de entradas.
            2. mostrar ubicaciones disponibles.
            3. ver listado de asistentes.
            4. mostrar ganancias totales.
            5. salir.
            """)
            if eleccion in(1,2,3,4):
                break
            else:
                print("ERROR!")
        except:
            print("Elija una opcion valida.")


def siclo_for():
    while True:
                try:
                    cantidad_platinum = input("Ingrese una cantidad de entradas con un limite de 3 por persona!")
                    if cantidad_platinum <= 3 and cantidad_platinum >= 1:
                        total_platinum = 120000*cantidad_platinum
                        break
                    else:
                        print("Limite de 3 por persona!")

                except:
                    print("Ingrese una cantidad valida!")
            
                for x in range(cantidad_platinum):
                    while True:
                        try:
                            rut = input("Ingrese el rut que quedara como titular de las sillas!")
                            if rut <= 99999999 and rut >= 10000000:
                                break
                            else:
                                print("ERROR! rut invalido")
                        except:
                            print("ERROR!")