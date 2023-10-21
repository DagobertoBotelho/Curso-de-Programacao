def adicionar_tarefa(tarefas,titulo,descricao,):
    pasta = {
        'Titulo' : titulo,
        'Descricao' : descricao,
    }
    tarefas.append(pasta)
    print("Cliente cadastrado com sucesso!")
    print("-------------------------------------------")
    print("\n")
tarefas = []

def editar_tarefa(tarefas,ID,titulo,descricao,):
    if 0 <= ID < len(tarefas): 
        tarefas[ID]['Titulo'] = titulo
        tarefas[ID]['Descricao'] = descricao
        print("\n")
        print("--------------- ATUALIZADO ---------------")
        print("Tarefa editada com sucesso!") 

def listar_tarefas(tarefas):
    for ID,pasta in enumerate(tarefas):
        print("\n")
        print("--------------- TAREFAS CADASTRADAS ---------------")
        print("ID do aluno:",ID)
        print("Titulo da tarefa:",pasta['Titulo']) 
        print("Descrição da terfa:",pasta['Descricao'])

while True:

    print("\n")
    print("--------------- MENU ---------------")
    print("1. Adicionar tarefa.")
    print("2. Editar tarefa.")
    print("3. Listar tarefas pendentes.")
    print("4. Listar tarefas vencidas.")
    print("5. Excluir tarefa.")
    print("6. Sair.")
    print("\n")
    op = str(input("Escolha uma opção: "))

    if op == "1":
        titulo = str(input("Digite o titulo da tarefa: "))
        descricao = str(input("Digite uma descrição para a tarefa: "))
        adicionar_tarefa(tarefas,titulo,descricao)
    elif op == "2":
        ID = int(input("Digite o ID da tarefa: "))
        titulo = str(input("Digite o titulo da tarefa: "))
        decricao = str(input("Digite uma descrição para a tarefa: "))
        vencimento = str(input("Digite o dia para o vencimento: "))
        editar_tarefa(tarefas,ID,titulo,descricao)
        