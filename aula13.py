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
    print("\n")
    print("--------------- CADASTRADO ---------------")
    print("Produto cadastrado com sucesso!")
produto = []


def imprimir_produto(produto):

    for i,cadastrar in enumerate(produto):
        print("\n")
        print("--------------- PRODUTO CADASTRADO ---------------")
        print("ID do produto:",i)
        print("Nome do produto :",cadastrar['Nome_do_produto'])
        print("Valor do produto : R$",cadastrar['Valor_do_produto'])
        print("Quantidade de produtos:",cadastrar['Quantidade'])
        print("Valor do frete:",cadastrar['Frete'])
        print("Porcentagem de lucro:",cadastrar['Lucro'],"%")
        print(f"Valor de custo: R${cadastrar['Valor_do_custo']:.2f}")
        print(f"valor de venda: R${cadastrar['Valor_de_venda']:.2f}")

def atualizar_produto(produto,indice,nome_produto,valor_produto,quantidade,frete,lucro,valor_custo,valor_venda,imposto1,imposto2,imposto3):
    if 0 <= indice <  len(produto):
        produto[indice]['Nome_do_produto'] = nome_produto
        produto[indice]['Valor_do_produto'] = valor_produto
        produto[indice]['Quantidade'] = quantidade
        produto[indice]['Frete'] = frete
        produto[indice]['Lucro'] = lucro
        produto[indice]['Valor_do_custo'] = valor_custo
        produto[indice]['Valor_de_venda'] = valor_venda
        produto[indice]['Imposto1'] = imposto1
        produto[indice]['Imposto2'] = imposto2
        produto[indice]['Imposto3'] = imposto3
        print("\n")
        print("--------------- ATUALIZADO ---------------")
        print("Produto atualizado com sucesso!")

def deletar_produto(ptoduto,indice):
    if 0 <= indice <  len(produto):
        del produto [indice]
        print("\n")
        print("--------------- DELETADO ---------------")
        print("Produto deleteado com sucesso!")



while True:
    print("\n")
    print("--------------- ESCOLHA UMA OPÇÃO ---------------")
    print("1. Cadastra produto.")
    print("2. Imprimir produto.")
    print("3. Atualizar produto.")
    print('4. Deletar produto.')
    print("5. Sair.")
    
    print("\n")
    op = int(input("Digite uma opção: "))
    
    if op == 1:
        print("\n")
        print("--------------- CADASTRA PRODUTO ---------------")
        nome_produto = str(input("Digite o nome do produto: "))

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
        lucro = cad_lucro
        calc_lucro = cad_lucro / 100 
        calc_individual = (valor_produto / quantidade)
        calc_custo = ((calc_individual * imposto1 * imposto2 * imposto3) + calc_individual + calc_frete)
        valor_custo = float(calc_custo)
        calc_venda = ((valor_custo * calc_lucro) + valor_custo)
        valor_venda = float(calc_venda)
        
        cadastrar_produto(produto,nome_produto,valor_produto,quantidade,frete,lucro,valor_custo,valor_venda,imposto1,imposto2,imposto3)

    elif op == 2:
        print("\n")
        imprimir_produto(produto)
        

    elif op == 3:
        print('\n')
        indice = int(input("Digite o ID do produto: "))
        nome_produto = str(input("Digite o nome do produto: "))

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
        lucro = cad_lucro
        calc_lucro = cad_lucro / 100 
        calc_individual = (valor_produto / quantidade)
        calc_custo = ((calc_individual * imposto1 * imposto2 * imposto3) + calc_individual + calc_frete)
        valor_custo = float(calc_custo)
        calc_venda = ((valor_custo * calc_lucro) + valor_custo)
        valor_venda = float(calc_venda)  

        atualizar_produto(produto,indice,nome_produto,valor_produto,quantidade,frete,lucro,valor_custo,valor_venda,imposto1,imposto2,imposto3)

    elif op == 4:
        print('\n')
        indice = int(input("Digite o ID do produto: "))
        deletar_produto(produto,indice)

    elif op == 5:
        break
    else:
        print("\n")
        print("--------------- ERRO ---------------")  
        print("Opção invalida, digite novamente.") 