# exercicio 1

nome_produto = []
valor_produto = []
quant_produto = []
valor_frete = []
lucro = []
valor_custo = []
valor_venda = []

while True:
    print("--------------- ESCOLHA UMA OPÇÃO ---------------")
    print("1. Cadastra produto.")
    print("2. Imprimir produto.")
    print("3. Sair.")

    op = int(input("Digite uma opção: "))
    
    if op == 1:
        print("--------------- CADASTRA PRODUTO ---------------")
        cad_nome = str(input("Digite o nome do produto: "))
        nome_produto.append(cad_nome)

        cad_valor = float(input("Digite o valor do produto: "))
        valor_produto.append(cad_valor)

        cad_quant = int(input("Ditete a quantidade de produtos: "))
        quant_produto.append(cad_quant)

        cad_frete = float(input("Digite o valor de frete do produto: "))
        valor_frete.append(cad_frete)

        imposto1 = 0
        imposto2 = 0
        imposto3 = 0
        cad_imposto1 = float(input("Digite o valor do primeiro imposto em %: "))
        imposto1 = cad_imposto1 / 100
        cad_imposto2 = float(input("Digite o valor do segundo imposto em %: "))
        imposto2 = cad_imposto2 / 100
        cad_imposto3 = float(input("Digite o valor do terceiro imposto em %: "))
        imposto3 = cad_imposto3 / 100

        cad_lucro = float(input("Digite a porcentagem de lucro: "))
        calc_lucro = cad_lucro / 100 
        lucro.append(calc_lucro)
        print("--------------- CADASTRADO ---------------")
        print("Produto cadastrado com sucesso")

    elif op == 2:

        for i in range(len(nome_produto)):
            calc_frete = valor_frete[i] / quant_produto [i]
            calc_individual = (valor_produto[i] / quant_produto[i])
            calc_custo = ((calc_individual * imposto1 * imposto2 * imposto3) + calc_individual + calc_frete)
            valor_custo.append(calc_custo)
            calc_venda = ((valor_custo[i] * lucro[i]) + valor_custo[i])
            valor_venda.append(calc_venda)
            print("--------------- PRODUTO CADASTRADO ---------------")
            print("Nome do produto :",nome_produto[i])
            print("Valor do produto : R$",valor_produto[i])
            print("Quantidade de produtos:",quant_produto[i])
            print("Valor do frete:",valor_frete[i])
            print("Porcentagem de lucro:",lucro [i],"%")
            print(f"Valor de custo: R${valor_custo[i]:.2f}")
            print(f"valor de venda: R${valor_venda[i]:.2f}")
    elif op == 3:
        break
    else:
        print("--------------- ERRO ---------------")  
        print("Opção invalida, digite novamente.") 