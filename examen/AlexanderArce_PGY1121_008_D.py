import time
import numpy
import os
import funciones

numpy.zeros[10,10]
lista_platinum = []
lista_gold = []
lista_silver = []
lista_rut = []
platinum = 120000
gold = 80000
silver = 50000







while True:
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
    
    if eleccion == 1:
        while True:
            try:
                entrada = input("""Bienvenido a la compra de entradas!, ingrese que entrada le gustaria comprar.
                1. Platinum
                2. Gold
                3. Silver
                """)
                if entrada in(1,2,3):
                    break
                else:
                    print("ERROR! cantidad no valida")

            except:
                print("ERROR! ingrese una cantidad valida")
        if entrada == 1:
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
        elif entrada == 2:
            while True:
                try:
                    cantidad_gold = input("Ingrese una cantidad de entradas con un limite de 3 por persona!")
                    if cantidad_gold <= 3 and cantidad_gold >= 1:
                        total_gold = 80000*cantidad_gold
                        break
                    else:
                        print("ERROR!")
                
                except:
                    print("ERROR!")
            
                for x in range(cantidad_gold):
                    while True:
                        try:
                            rut = input("Ingrese el rut que quedara como titular de las sillas!")
                            if rut <= 99999999 and rut >= 10000000:
                                break
                            else:
                                print("ERROR! rut invalido")


                        except:
                            print("ERROR!")
        elif entrada == 3:
            while True:
                try:
                    cantidad_silver = input("Ingrese una cantidad de entradas con un limite de 3 por persona!")
                    if cantidad_silver <= 3 and cantidad_silver >= 1:
                        total_silver = 50000*cantidad_silver
                        break
                    else:
                        print("ERROR!")

                except:
                    print("ERROR!")
            
                for x in range(cantidad_silver):
                    while True:
                        try:
                            nombre = input("Ingrese su nombre: ")
                            rut = input("Ingrese el rut que quedara como titular de las sillas: ")
                            if rut <= 99999999 and rut >= 10000000:
                                break
                            else:
                                print("ERROR! rut invalido")


                        except:
                            print("ERROR!")
        
            lista_platinum[cantidad_platinum]
            lista_gold[cantidad_gold]
            lista_silver[cantidad_silver]
            lista_rut[rut]
    elif eleccion == 2:
        for x in range(10):
            for y in range(10):
                numpy.zeros
    elif eleccion == 3:
        print(lista_rut)




        print("Todas las personas con entradas!")
    elif eleccion == 4:
        total_entradas = cantidad_platinum + cantidad_gold + cantidad_silver
        ganancia_total = total_platinum + total_gold + total_silver
        print("|------------------------------------------------------------|")
        print("|     TIPO ENTRADA   |     CANTIDAD      |      TOTAL        |")
        print("|------------------------------------------------------------|")
        print("|Platinum   $120.000", cantidad_platinum , total_platinum,  "|")
        print("|____________________________________________________________|")
        print("|Gold       $80.000",  cantidad_gold ,     total_gold,      "|")
        print("|____________________________________________________________|")
        print("|Silver     $50.000",  cantidad_silver,    total_silver,    "|")
        print("|____________________________________________________________|")
        print("|TOTAL",               total_entradas ,    ganancia_total,  "|")
        print("|------------------------------------------------------------|")
    else:
        print(f"Muchas gracias {nombre} por alagirnos! tenga un muy lindo dia.")
    