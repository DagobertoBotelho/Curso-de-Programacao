nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

calc = ((nota1 + nota2) / 2)

if calc >= 9:
    print("Nota A")
elif calc >= 7.5 and calc < 9:
    print("Nota B")
elif calc >= 6 and calc < 7.5:
    print("Nota C")
elif calc >= 4 and calc < 6:
    print("Nota D")
else:
    print("Nota E")