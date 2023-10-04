# explicação 

#def cadastrar_cliente(clientes,nome,email,telefone):
 #   cliente ={
  #      'Nome':nome,
   #     'Email':email,
    #    'Telefone':telefone
 #   }
  #   clientes.append(cliente)
   # print("Cliente cadastrado com sucesso!")
    #print("-------------------------------------------")
    #print("\n")
    

#def imprimir_clientes(clientes):
 #   for indice,cliente in enumerate(clientes):
  #      print(f"ID cliente {indice+1}")
   #     print(f"Nome: {cliente['Nome']}")
    #   print(f"Email: {cliente['Email']}")
     #   print(f"Telefone: {cliente['Telefone']}")
      #  print("-------------------------------------------")
       # print("\n")

#clientes = []
#nome = input("Digite o nome: ")
#email = input("Digite o email: ")
#telefone = input("Digite o telefone: ")
#cadastrar_cliente(clientes,nome,email,telefone)
#imprimir_clientes(clientes)

# exercicio 1

def cadastrar_produto(produto,nome_produto,valor_produto,quantidade,frete,lucro,valor_custo,valor_venda,imposto1,imposto2,imposto3):
    cadastrar={
        'Nome_do_produto': nome_produto,
        'Valor_do_produto': valor_produto,
        'Quantidade': quantidade,
        'Frete': frete,
        'Lucro': lucro,
        'Valor_do_custo': valor_custo,
        'Valor_de_venda': valor_venda,
        'Imposto1': imposto1,
        'Imposto2': imposto2,
        'Imposto3': imposto3
    }
    produto.append(cadastrar)
    produto = []
    print("--------------- CADASTRADO ---------------")
    print("Produto cadastrado com sucesso!")

while True:
    print("--------------- ESCOLHA UMA OPÇÃO ---------------")
    print("1. Cadastra produto.")
    print("2. Imprimir produto.")
    print("3. Sair.")

    op = int(input("Digite uma opção: "))
    
    if op == 1:
        print("--------------- CADASTRA PRODUTO ---------------")
        nome = str(input("Digite o nome do produto: "))

        valor_produto = float(input("Digite o valor do produto: "))

        quantidade = int(input("Ditete a quantidade de produtos: "))

        calc_frete = float(input("Digite o valor de frete do produto: "))
        frete = calc_frete / quantidade

        cad_imposto1 = float(input("Digite o valor do primeiro imposto em %: "))
        imposto1 = cad_imposto1 / 100
        cad_imposto2 = float(input("Digite o valor do segundo imposto em %: "))
        imposto2 = cad_imposto2 / 100
        cad_imposto3 = float(input("Digite o valor do terceiro imposto em %: "))
        imposto3 = cad_imposto3 / 100

        cad_lucro = float(input("Digite a porcentagem de lucro: "))
        lucro = cad_lucro / 100 
        calc_individual = (valor_produto / quantidade)
        calc_custo = ((calc_individual * imposto1 * imposto2 * imposto3) + calc_individual + calc_frete)
        valor_custo = int(calc_custo)
        calc_venda = ((valor_custo * lucro) + valor_custo)
        valor_venda = int(calc_venda)
        
        cadastrar_produto(produto,nome_produto,valor_produto,quantidade,frete,lucro,valor_custo,valor_venda,imposto1,imposto2,imposto3)

    elif op == 2:

        for i,cadastrar in enumerate(produto):
            print("--------------- PRODUTO CADASTRADO ---------------")
            print("Nome do produto :",{cadastrar['Nome_do_produto']})
            print("Valor do produto : R$",{cadastrar['Valor_do_produto']})
            print("Quantidade de produtos:",{cadastrar['Quantidade']})
            print("Valor do frete:",{cadastrar['Frete']})
            print("Porcentagem de lucro:",{cadastrar['Lucro']},"%")
            print("Valor de custo: R$",{cadastrar['Valor_do_custo']})
            print("valor de venda: R$",{cadastrar['Valor_da_venda']})
    elif op == 3:
        break
    else:
        print("--------------- ERRO ---------------")  
        print("Opção invalida, digite novamente.") 
    print("Produto cadastrado com sucesso!")