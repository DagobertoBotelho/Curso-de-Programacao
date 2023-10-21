import datetime
def cadastro_livro(livros,titulo,autor,editora):
	cad_livro = {
	'Titulo' : titulo,
	'Autor' : autor,
	'Editora' : editora
	}
	
	livros.append(cad_livro)
livros = []
	
def imp_livro (livros):
	for i,cad_livro in enumerate(livros):
		print("Número de cadastro do livro:",i)
		print("Título:",cad_livro['Titulo'])
		print("Autor:",cad_livro['Autor'])
		print("Editora:",cad_livro['Editora'])
		
def edit_livro(livros,indice,titulo,autor,editora):
	if 0 <= indice < len(livros):
		livros[indice]['Titulo'] = titulo
		livros[indice]['Autor'] = autor
		livros[indice]['Editora'] = editora
		
def deleter_livro(livros,indice):
		if 0 <= indice < len(livros):
			del livros [indice]
		
def cadastro_pessoa(pessoas,nome,email,telefone):
	cad_pessoa = {
	'Nome' : nome,
	'Email' : email,
	'Telefone' : telefone
	}
	pessoas.append(cad_pessoa)
pessoas = []
	
def imp_pessoa(pessoas):
	for i,cad_pessoa in enumerate(pessoas):
		print("Número de cadastro da pessoa:",i)
		print("Nome:",cad_pessoa['Nome'])
		print("E-mail:",cad_pessoa['Email'])
		print("Telefone:",cad_pessoa['Telefone'])
		
def edit_pessoa(pessoas,indice,nome,email,telefone):
	if 0 <= indice < len(pessoas):
		pessoas[indice]['Nome'] = nome
		pessoas[indice]['Email'] = email
		pessoas[indice]['Telefone'] = telefone
		
def deleter_pessoa(pessoas,indice):
	if 0 <= indice < len(pessoas):
		del pessoas [indice]

def registro_emp(emprestimos,pessoa,livro,data_emp,data_entrega):
	emprestimo = {
	'Pessoa': pessoa,
	'Livro': livro,
	'Data_emp': data_emp,
	'Data_entrega': data_entrega
	}
	emprestimos.append(emprestimo)
emprestimos = []
			
def imp_registro(emprestimos):
	for i,emprestimo in enumerate(emprestimos):
		print("Número do registro:",i)
		print("Nome:",emprestimo['Pessoa'])
		print("Livro:",emprestimo['Livro'])
		print("Data do emprestimo:",emprestimo['Data_emp'])
		print("Data de devolusão:",emprestimo['Data_entrega'])

def imp_atrasados(emprestimos,data_entrega,pessoa,livro):
	data = datetime.datetime.now()
	for i,emprestimo in enumerate(emprestimos):
		if data_entrega< data:
			print("Número do registro:",i)
			print("Nome:",emprestimo['Pessoa'])
			print("Livro:",emprestimo['Livro'])
			print("Data do emprestimo:",emprestimo['Data_emp'])
			print("Data de devolusão:",emprestimo['Data_entrega'])

def edit_registro(emprestimos,indice,pessoa,livro,data_emp,data_entrega):
	if 0 <= indice < len(emprestimos):
		emprestimos[indice]['Pessoa'] = pessoa
		emprestimos[indice]['Livro'] = livro
		emprestimos[indice]['Data_emp'] = data_emp
		emorestimos[indice]['Data_entrega'] = data_entrega

def deleter_registro(emprestimos,indice):
	if 0 <= indice < len(emprestimos):
		del emprestimos [indice]
		

while True:
	    print("\n")
	    print("--------------- ESCOLHA UMA OPÇÃO ---------------")
	    print("\n")
	    print("|---------- LIVROS ----------|")
	    print("1. Cadastrar livro.")
	    print("2. Exibir livros cadastrados.")
	    print("3. Editar livro.")
	    print("4. Deletar livro.")
	    print("\n")
	    print("|---------- PESSOAS ----------|")
	    print("5. Cadastrar pessoa.")
	    print("6. Exibir pessoas cadastradas.")
	    print("7. Editar dados da pessoa.")
	    print("8. Deletar pessoa")
	    print("\n")
	    print("|---------- EMPRÉSTIMOS ----------|")
	    print("9. Registrar um novo empréstimo.")
	    print("10. Exibir empréstimos.")
	    print("11. Exibir empréstimos atrasados.")
	    print("12. Editar registro de empréstimo.")
	    print("13. Deletar registro de empréstimo.")
	    print("\n")
	    print("|---------- SAIR ----------|")
	    print("14. Sair.")
	    print("\n")
	    op = str(input("Digite uma opção: "))
	    
	    if op == "1":
	    	titulo = str(input("Digite o título do livro: "))
	    	autor = str(input("Digite o nome do autor do livro: "))
	    	editora = str(input("Digitebo nome da editora do livro: "))
	    	cadastro_livro(livros,titulo,autor,editora)
	    
	    elif op == "2":
	    	print("\n")
	    	imp_livro (livros)
	    	
	    elif op == "3":
	    	indice = int(input("Digite o número de cadastro do livro: "))
	    	titulo = str(input("Digite o título do livro: "))
	    	autor = str(input("Digite o nome do autor do livro: "))
	    	editora = str(input("Digitebo nome da editora do livro: "))
	    	edit_livro(livros,indice,titulo,autor,editora)
	    	
	    elif op == "4":
	    	indice = int(input("Digite o número de cadastro do livro: "))
	    	deleter_livro(livros,indice)
	    
	    elif op == "5":
	    	nome = str(input("Digite o nome da pessoa: "))
	    	email = str(input("Digite o e-mail da pessoa: "))
	    	telefone = str(input("Digitebo o telefone da pessoa: "))
	    	cadastro_pessoa(pessoas,nome,email,telefone)
	    
	    elif op == "6":
	    	print("\n")
	    	imp_pessoa(pessoas)
	    
	    elif op == "7":
	    	indice = int(input("Digite o número de cadasrro da pessoa: "))
	    	nome = str(input("Digite o nome da pessoa: "))
	    	email = str(input("Digite o e-mail da pessoa: "))
	    	telefone = str(input("Digitebo o telefone da pessoa: "))
	    	edit_pessoa(pessoas,indice,nome,email,telefone)
	    
	    elif op == "8":
	    	indice = int(input("Digite o número de cadastro da pessoa: "))
	    	deleter_pessoa(pessoas,indice)
	    
	    elif op == "9":
		    esc_p = int(input("Digite o número de cadastro da pessoa: "))
	    	for i,cad_pessoa in enumerate(pessoas,i):
				if esc_p = i:
	    			pessoa = cad_pessoa['Nome']
			esc_l = int(input("Digite o número de cadastro do livro: "))
	    	for i,cad_livro in enumerate(livros,i):
				if esc_l = i:
	    			livro = cad_livro['Titulo']
	    	hoje = datetime.datetime.now()
	    	data_emp = (hoje.date())
	    	dia = int(input("Digite a dia da devolusão: "))
	    	mes = int(input("Digite o mês da devolusão: "))
	    	ano = int(input("Digite o ano da devolusão: "))
	    	entrega = datetime.datetime(year=ano,month=mes,day=dia)
	    	data_entrega = (entrega.date())
	    	registro_emp(emprestimos,pessoa,livro,data_emp,data_entrega) 
	    
	    elif op == "10":
	    	print("\n")
	    	imp_registro(emprestimos)	    				    
	    elif op == "11":
	    	print("\n")
	    	imp_atrasados(emprestimos,data_entrega,pessoa,livro)
	    	
	    elif op == "12":
	    	indice = int(input("Digite o número do registro: "))
	    	import datetime
	    	for i,cad_pessoa in enumerate(pessoas):
	    		i = int(input("Digite o número de cadastro da pessoa: "))
	    		pessoa = cad_pessoa['Nome']
	    	for i,cad_livro in enumerate(livros):
	    		i = int(input("Digite o número de cadastro do livro: "))
	    		livro = cad_livro['Titulo']
	    	hoje = datetime.datetime.now()
	    	data_emp = (hoje.date())
	    	dia = int(input("Digite a dia da devolusão: "))
	    	mes = int(input("Digite o mês da devolusão: "))
	    	ano = int(input("Digite o ano da devolusão: "))
	    	entrega = datetime.datetime(year=ano,month=mes,day=dia)
	    	data_entrega = (entrega.date())
	    	edit_registro(emprestimos,indice,pessoa,livro,data_emp,data_entrega)
	    
	    elif op == "13":
	    	indice = int(input("Digite o número do registro: "))
	    	deleter_registro(emprestimos,indice)
	    
	    elif op == "14":
	    	break
	    	
	    else:
	       print("\n")
	       print("--------------- ERRO ---------------")
	       print("Opção invalida, digite novamente.")		    	