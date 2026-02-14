def eh_par(n):
    return n % 2 == 0

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

def f_para_c(n1):
    return (5/9 * (n1 - 32))

def c_para_f(n1):
    return (n1 * 1.8) + 32

def classificador(n):
    positivo = n > 0
    par = n % 2 == 0
    return positivo,par

def vogais(n):
    for i in n:
        i = ("a","e","i","o","u")
        return print(f"A vogal {i} está presente na palavra.")
    