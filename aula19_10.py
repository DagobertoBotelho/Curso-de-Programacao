def cadastrar_pessoa(Pessoas,nome,email,telefone):
    pessoa = {
        'NOME': nome,
        'EMAIL': email,
        "TELEFONE": telefone
    }
    pessoas.apppend(pessoa)
pessoas = []

with open('pessoas.csv', mode='w', newline='') as pessoas_csv:
        writer = csv.writer(pessoas_csv)
        writer.writerow(["ID","Nome", "e-Mail", "Telefone"])
        for pessoa in pessoas:
            writer.writerow([pessoa,pessoa['NOME'], pessoa['EMAIL'], pessoa['TELEFONE']])

def cadastrar_livro(livros,titulo,autor,editora):
    livro = {
        'TITULO': titulo,
        'AUTOR': autor,
        'EDITORA': editora
    }
    livros.append(pessoa)
livros = []

with open('livros.csv', mode='w', newline='') as livros_csv:
        writer = csv.writer(livros_csv)
        writer.writerow(["Titulo", "Autor", "Editora"])
        for livro in livros:
            writer.writerow([livro['TITULO'], livro['AUTOR'], livro['EDITORA']])

print("MENU")
nome = str(input("Digite o nome: "))
email = str(input("Digite o email: "))
telefone = int(input("Ditegite o telefone: "))