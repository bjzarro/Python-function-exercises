import funcoes

print("Escolha a unidade que deseja converter:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
escala = input(":")
n1 = int(input("Escreva a temperatura:"))

if escala == "1":
    print(f"A temperatura em fahrenheit é: {funcoes.c_para_f(n1)}")

elif escala == "2":
    print(f"A temperatura em celsius é: {funcoes.f_para_c(n1)}")

else:
    print("Escala incorreta.")
