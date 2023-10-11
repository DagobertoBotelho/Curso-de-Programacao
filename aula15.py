# exercicio 1

#valor_menor = float(input("Digite o preço: "))

#for i in range(2):
#    valor = float(input("Digite o preço: "))
#    if valor < valor_menor:
#        valor_menor = valor
#print("O produto mais em conta é o no valor de: R$",valor_menor)

# exercicio 2

numero = []
a = float(input("Digite um número: "))
numero.append(a)
b = float(input("Digite um número: "))
numero.append(b)
c = float(input("Digite um número: "))
numero.append(c)

maior = max(numero)
menor = min(numero)
meio = numero[0] + numero[1] + numero[2] - maior - menor

print(maior)
print(meio)
print(menor)