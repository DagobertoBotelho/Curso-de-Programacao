def cadastrar_notas(notas,nome,nota1,nota2,nota3,nota4,media):
	cadastrar = {
		'Nome': nome,
		'Nota1': nota1,
		'Nota2': nota2,
		'Nota3': nota3,
		'Nota4': nota4,
		'Media': media,
	}
	
	notas.append(cadastrar)
	print("\n")
	print("--------------- CADASTRADO ---------------")
	print("Nota cadastrada com sucesso!")
notas = []

def imprimir_nota(notas):
        for i,cadastrar in enumerate(notas):
        	print("\n")
        	print("--------------- NOTAS CADASTRADAS ---------------")
        	print("ID do aluno:",i)
        	print("Nome do aluno:",cadastrar['Nome']) 
        	print("Primeira nota do aluno:",cadastrar['Nota1'])
        	print("Segunda nota do aluno:",cadastrar['Nota2'])
        	print("Terceira nota do aluno:",cadastrar['Nota3'])
        	print("Quarta nota do aluno:",cadastrar['Nota4'])
        	
def editar_nota(notas,indice,nome,nota1,nota2,nota3,nota4):
	if 0 <= indice < len(notas):
		notas[indice]['Nome'] = nome
		notas[indice]['Nota1'] = nota1
		notas[indice]['Nota2'] = nota2
		notas[indice]['Nota3'] = nota3
		notas[indice]['Nota4'] = nota4
		print("\n")
		print("--------------- ATUALIZADO ---------------")
		print("Nota editada com sucesso!")
		
def media_aluno(nome,media):
	for i,cadastrar in enumerate(notas):
		print("Aluno:",cadastrar['Nome'])
		print("Média:",cadastrar['Media'])
		print("\n")
		
def alunos_aprovados(notas):
	print("--------------- APROVADOS ---------------")
	for i,cadastrar in enumerate(notas):
		if cadastrar['Media'] >= 7:
			print("Aluno:",cadastrar['Nome'])

def alunos_reprovados(notas):
	print("--------------- REPROVADOS ---------------")
	for i,cadastrar in enumerate(notas):
		if cadastrar['Media'] < 7:
			print("Aluno:",cadastrar['Nome'])
	

def deletar_nota(notas,indice):
		if 0 <= indice < len(notas):
			del notas [indice]
			print("--------------- DELETADOA ---------------")
			print("Nota deleteada com sucesso!")
		


while True:
    	print("\n")
    	print("--------------- ESCOLHA UMA OPÇÃO ---------------")
    	print("1. Cadastra nota.")
    	print("2. Imprimir nota")
    	print("3. Editar nota.")
    	print("4. Média dos alunos.")
    	print("5. Alunos aprovados.")
    	print("6. Alunos reprovados")
    	print("7. Deletar nota.")
    	print("8. Sair.")
    	print("\n")
    	op = int(input("Digite uma opção: "))
    	
    	if op == 1:
    		nome = str(input("Digite o nome do aluno: ")) 
    		nota1 = float(input("Digite a primeira nota: "))
    		nota2 = float(input("Digite a segunda nota: "))
    		nota3 = float(input("Digite a terceira nota: "))
    		nota4 = float(input("Digite a quarta nota: "))
    		media = ((nota1 + nota2 + nota3 + nota4) / 4)
    		cadastrar_notas(notas,nome,nota1,nota2,nota3,nota4,media)
    		
    	elif op == 2:
    		print("\n")
    		imprimir_nota(notas)
    	
    	elif op == 3:
    		indice = int(input("Digite o ID do aluno: "))
    		nome = str(input("Digite o nome do aluno: ")) 
    		nota1 = float(input("Digite a primeira nota: "))
    		nota2 = float(input("Digite a segunda nota: "))
    		nota3 = float(input("Digite a terceira nota: "))
    		nota4 = float(input("Digite a quarta nota: "))
    		editar_nota(notas,indice,nome,nota1,nota2,nota3,nota4)
    		
    	elif op == 4:
    		print("\n")
    		print("--------------- MÉDIAS ---------------")
    		media_aluno(nome,media)
    		
    	elif op == 5:
    		print("\n")
    		alunos_aprovados(notas)
    		  	
    	elif op == 6:
    		print("\n")
    		alunos_reprovados(notas)
    	
    	elif op == 7:
    		indice = int(input("Digite o ID do aluno: "))
    		deletar_nota(notas,indice)
    		  
    	elif op == 8:
    		break
    	
    	else:
    	   print("\n")
    	   print("--------------- ERRO ---------------")
    	   print("Opção invalida, digite novamente.")				  			