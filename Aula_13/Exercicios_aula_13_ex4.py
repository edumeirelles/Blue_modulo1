# 4. Uma escola te contratou para desenvolver um programa em Python para que o
# professor gerencie as notas de seus alunos. Seu programa deve apresentar o seguinte
# menu:
# 0. Sair
# 1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
# 2. Inserir aluno e nota
# 3. Alterar a nota de um aluno
# 4. Consultar nota de um aluno específico
# 5. Apagar um aluno da lista
# 6. Exibir a média da turma
# As notas e os nomes dos alunos serão fornecidos pelo professor. Implemente a sua
# solução utilizando dicionário.

def menu():
    while True:
        print()
        print('Escola T2B')
        print('1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)')
        print('2. Inserir aluno e nota')
        print('3. Alterar a nota de um aluno')
        print('4. Consultar nota de um aluno específico')
        print('5. Apagar um aluno da lista')
        print('6. Exibir a média da turma')
        print()
        op = input('Digite a opção desejada: ')
        if op == '0':
            break
        if op == '1':
            exibir()
        elif op == '2':
            inserir()
        elif op == '3':
            alterar()
        elif op == '4':
            consultar()
        elif op == '5':
            apagar()
        elif op == '6':
            exibir()
        else:
            


anlunos = dict()
menu()