class Aluno:
    nome = None
    cpf = None
    peso = None
    altura = None
    status = False
class Exercicio:
    nome = None
    numRep = 0
    pesoExec = 0

cadAlunos = []
listaExerc = []

def menu():
    while True:
        print('Bem Vindo ao Menu principal')
        print('1 - cadastrar aluno')
        print('2 - gerenciar treino')
        print('3 - consultar aluno')
        print('4 - atualizar cadastro do aluno')
        print('5 - excluir aluno')
        print('6 - relatorio de alunos')
        print('9 - sair do programa')
        caso = int(input('Digite um número:'))
        match caso:
            case 1:
                return cadAluno()
            case 6:
                return relatorio()
            
def relatorio():
    print('1 - todos os alunos')
    print('2 - alunos ativos')
    print('3 - alunos inativos')
    caso = int(input('digite um numero:'))
    match caso:
        case 1:
            print('------lista------')
            for i in cadAlunos:
                print('nome:', i.nome ,'cpf:', i.cpf, 'peso:', i.peso, 'altura:', i.altura)
        case 2:
            print('------lista------')
            for i in cadAlunos:
                if i.status == True:
                    print('nome:', i.nome ,'cpf:', i.cpf, 'peso:', i.peso, 'altura:', i.altura)
        case 3:
            print('------lista------')
            for i in cadAlunos:
                if i.status == False:
                    print('nome:', i.nome ,'cpf:', i.cpf, 'peso:', i.peso, 'altura:', i.altura)

# ALUNO-------------------------------------------------------
def cadAluno():
    new = Aluno()
    new.nome = str(input('Nome do aluno:'))
    new.cpf = input('CPF do aluno:')
    new.peso = input('Peso do aluno:')
    new.altura = input('Altura do aluno:')
    cadAlunos.append(new)
    listaExerc.append([])
    print('Aluno cadastrado com sucesso')
    return menu()


# TREINO-------------------------------------------------------
def menuTreino():
    print('Menu de Treino')
    print('1 - cadastrar novo exercicio')
    print('2 - alterar exercicio')
    print('3 - excluir exercicio especifico')
    print('4 - excluir treino todo')

def addExercicio(idAluno):
    x = int(input('Digite 0 para sair'))
    while True:
        if x == 0:
            break
        else:
            exer = Exercicio()
            exer.nome = input('Nome do exercicio:')
            exer.numRep = int(input('Numero de repetições'))
            exer.pesoExec = input('Peso usado no exercicio')
            if exer in listaExerc[idAluno]:
                print('exercicio ja existente na lista')
                return menu()
            else:
                listaExerc[idAluno].append(exer)
                print('Exercicio adicionados com sucesso')
                for i in range(cadAlunos):      # testa o id dos alunos ate achar o correto e seta o status pra true
                    if i == idAluno:
                        cadAlunos[i].status == True
    return menu()      
    

def main():
    return menu()

main() 