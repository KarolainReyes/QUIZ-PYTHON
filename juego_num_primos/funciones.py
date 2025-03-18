def mostrar_menu (men_principal):
    print(menu_principal)

def pedir_opcion ():
    return("Por favor seleccione la opcion que desea: ")

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
        return False
    return True

def primos_gemelos(limit):
    num_gemelos[]
    for num in range (2, limit-1)
    if es_primo(num) and es_primo(num+2):
        num_gemelos.append((num, num+2))
        return primos_gemelos
    
def num_palindromo(limit):
    return str(num)==str(num)[::-1]

def encontrar_palindromo(limit):
    palindromo_primo[]
    for num in range (10, limit+1):
        if es_primo (num) and num_palindromo(num):
            palindromo_primo.append(num):
            return palindromo_primo




