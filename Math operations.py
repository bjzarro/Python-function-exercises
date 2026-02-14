import funcoes

op = str(input("Escreva o tipo de operação (som, sub, div, mul): "))
n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
soma = funcoes.soma(n1,n2)
sub = funcoes.sub(n1,n2)
mult = funcoes.mult(n1,n2)
div = funcoes.div(n1,n2)

if op == "som":
    print("O resultado é:",soma)

elif op == "sub":
    print("O resultado é:",sub)

elif op == "mul":
    print("O resultado é:",mult)

elif op == "div":
    print("O resultado é:",div)

else:
    print("Tipo de operação incorreto.")
