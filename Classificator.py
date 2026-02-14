import funcoes

n = int(input("Escreva um número: "))
positivo,par = funcoes.classificador(n)

print(f"Este número é positivo: {positivo}.")
print(f"Este número é par: {par}.")

# não consegui colocar retorno para o caso de n = 0
