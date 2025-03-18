from menu import menu_pricipal
from funciones import mostrar_menu, pedir_opcion, primos_gemelos, num_palindromo, encontrar_palindromo, es_primo

 while True:
    mostrar_menu
    print("1. Mostrar numeros primos gemelos con rando de diferencia 2")
    print("2. Mostrar numeros palindromicos ")
    print("Saliendo...")
    opc = input (">")
    input(pedir_opcion)
    if opc == "1":
      limite=input(int("Ingrese el numero hasta en cual le gustaria llevar la secuencia de numeros primos: "))
      num_gemelos = primos_gemelos(limit=)
      print("Estos numeros son primos gemelos", + num_gemelos)
        elif opc == "2":
        limite=input(int("Ingrese el numero hasta el cual le gustaria llevar la secuencia de numeros primos palindromos"))
        num_palindromo = encontrar_palindromo(limit=)
        print("Estos numeros son primos palindromicos")
        elif opc == "3"
        print("Saliendo...")
        break
    else:
      print("Esta opcion no es valida, por favor intente de nuevo")

      