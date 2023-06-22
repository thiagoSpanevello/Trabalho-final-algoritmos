class Aluno:
    def __init__(self, nome, cpf, peso, altura, status):
        self.nome = nome
        self.cpf = cpf
        self.peso = peso
        self.altura = altura
        self.status = status


class Exercicio:
    def __init__(self, nome, numRep, pesoExec):
        self.nome = nome
        self.numRep = numRep
        self.pesoExec = pesoExec


listaAlunos = [Aluno('jorge', 39552078, 65, 165, False)]

listaTreinos = [[Exercicio('Flexão', 12, 50)]]


def menu():
    while True:
        print('\nBem vindo ao Menu Principal')
        print('  1 - Cadastrar aluno')
        print('  2 - Gerenciar treino')
        print('  3 - Consultar aluno')
        print('  4 - Atualizar cadastro do aluno')
        print('  5 - Excluir aluno')
        print('  6 - Relatório de alunos')
        print('  9 - Sair do programa')
        caso = numeroValido('int', input('Digite uma opção: '))
        print()
        match caso:
            case 1:  # cadastra um aluno
                return novoAluno()

            case 2:  # acha o id do aluno usando o nome dele e então entra no
                nomeAluno = input(
                    'Para gerenciar um treino, digite o nome do aluno: ')
                aluno = aluno = buscaAlunoNome(nomeAluno)
                if (aluno != -1):
                    idAluno = listaAlunos.index(aluno)
                    return menuTreino(idAluno)
                else:
                    print('Aluno não encontrado')

            case 3:
                nomeAluno = input('Digite o nome do aluno: ')
                aluno = buscaAlunoNome(nomeAluno)
                if (aluno != -1):
                    print('\n------ ALUNO ------')
                    printAluno(aluno)

                    idTreino = listaAlunos.index(aluno)
                    print('\n----- TREINO -----')
                    treino = listaTreinos[idTreino]
                    if (not treino):
                        print('O aluno não possui treino')
                    else:
                        for exer in treino:
                            printExer(exer)

                else:
                    print('\nAluno não encontrado')

            case 6:  # entra no menu de relatórios
                return relatorio()
            case 9:  # sai do programa
                print('Saindo do programa...')
                return
            case _:  # caso default
                print('Opção inválida')
                continue


# VERIFICAÇÕES -------------------------------------------------------

def numeroValido(tipo, input):  # permite somente números como entrada
    try:
        if (tipo == 'int'):
            number = int(input)
        elif (tipo == 'float'):
            number = float(input)

        return number
    except ValueError:
        return -1


def nomeValido(input):  # verifica se o nome é válido (!número e >3 letras)
    try:
        float(input)  # se o input puder ser um float, é um número
        return '\n(!) Nome não pode ser um número\n'
    except ValueError:
        if (len(input) <= 2):
            return '\n(!) Nome precisa ter mais de 2 letras\n'
        else:
            return True


# ALUNO -------------------------------------------------------

def novoAluno():  # --- CASO 1 ---
    verificacao = False
    nome = ''
    while (verificacao != True):
        nome = input('Nome do aluno: ')
        verificacao = nomeValido(nome)
        if (verificacao != True):  # se o nome for inválido
            print(verificacao)  # printa a mensagem dizendo o que tá errado

    cpf = input('CPF do aluno: ')
    peso = input('Peso do aluno: ')
    altura = input('Altura do aluno: ')
    listaAlunos.append(Aluno(nome, cpf, peso, altura, False))
    listaTreinos.append([])
    print('Aluno cadastrado com sucesso')
    return menu()


def relatorio():  # --- CASO 6 ---
    if (not listaAlunos):
        print('Não há alunos cadastrados no momento')
        return menu()
    print('Menu de relatório de alunos')
    print('  1 - Todos os alunos')
    print('  2 - Alunos ativos')
    print('  3 - Alunos inativos')
    caso = numeroValido('int', input('Digite uma opção: '))
    print()

    listaAlunos.sort(key=lambda x: x.nome)
    match caso:
        case 1:
            print('------ LISTA ------')
            for aluno in listaAlunos:
                printAluno(aluno)
        case 2:
            print('------ LISTA ------')
            for aluno in listaAlunos:
                if aluno.status == True:
                    printAluno(aluno)
        case 3:
            print('------ LISTA ------')
            for aluno in listaAlunos:
                if aluno.status == False:
                    printAluno(aluno)
        case _:
            print('Opção inválida')
    return menu()


def buscaAlunoNome(nome):  # busca um aluno pelo nome
    for aluno in listaAlunos:
        if (aluno.nome.lower() == nome.lower()):
            return aluno
    return -1  # se não retornar com o aluno, quer dizer que não existe


def printAluno(aluno):
    print('Nome:', aluno.nome, '\nCPF:', aluno.cpf,
          '\nPeso:', aluno.peso, '\nAltura:', aluno.altura,
          '\nStatus:', 'Ativo' if aluno.status == True else 'Inativo')
    print('     -----')

# TREINO -------------------------------------------------------


def menuTreino(idAluno):
    print('Menu de Treino')
    print('  1 - Cadastrar novo exercício')
    print('  2 - Alterar exercício')
    print('  3 - Excluir exercício específico')
    print('  4 - Excluir treino todo')
    caso = numeroValido('int', input('Digite uma opção: '))
    print()
    match caso:
        case 1:
            return novoExercicio(idAluno)
        case _:
            print('Opção inválida')


def novoExercicio(idAluno):
    nome = input('Nome do exercício: ')
    numRep = int(input('Numero de repetições: '))
    pesoExec = input('Peso usado no exercício: ')
    exer = Exercicio(nome, numRep, pesoExec)
    if exer in listaTreinos[idAluno]:
        print('Exercício já existente na lista')
        return menu()
    else:
        listaTreinos[idAluno].append(exer)
        print('Exercício adicionado com sucesso')
        # testa o id dos alunos ate achar o correto e seta o status pra true
        listaAlunos[idAluno].status = True
    return menu()


def printExer(exer):
    print('Exercício:', exer.nome,
          '\nRepetições:', exer.numRep,
          '\nPeso:', exer.pesoExec)
    print('     -----')


def main():
    return menu()


main()
