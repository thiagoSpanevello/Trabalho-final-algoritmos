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


listaAlunos = [Aluno('lucas', 11111111111, 65, 165, True)]

listaTreinos = [[Exercicio('exe1', 12, 50), Exercicio(
    'exe2', 24, 25), Exercicio('exe3', 6, 100)]]


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
                return novoAluno(None)

            case 2:  # acha o id do aluno usando o nome dele e então entra no
                nomeAluno = input(
                    'Para gerenciar um treino, digite o nome do aluno: ')
                aluno = buscaAlunoNome(nomeAluno)
                if (aluno != -1):
                    idAluno = listaAlunos.index(aluno)
                    return menuTreino(idAluno)
                else:
                    print('(!) Aluno não encontrado')
                    return menu()

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
                        print('(!) O aluno não possui treino')
                    else:
                        for exer in treino:
                            printExercicio(exer)

                else:
                    print('\n(!) Aluno não encontrado')
            case 4:
                nomeAluno = input('Digite o nome do aluno: ')
                aluno = buscaAlunoNome(nomeAluno)
                if (aluno != -1):
                    novoAluno(aluno)
                else:
                    print('\n(!) Aluno não encontrado')
            case 5:
                nomeAluno = input('Digite o nome do aluno: ')
                aluno = buscaAlunoNome(nomeAluno)
                if (aluno != -1):
                    return excluirAluno(aluno)
                else:
                    print('(!) Aluno não encontrado')
                    return menu()
            case 6:  # entra no menu de relatórios
                return relatorio()
            case 9:  # sai do programa
                print('Saindo do programa...')
                return
            case _:  # caso default
                print('(!) Opção inválida')
                return menu()


# VERIFICAÇÕES -------------------------------------------------------

def numeroValido(tipo, input):  # permite somente números positivos como entrada
    try:
        if (tipo == 'int'):
            number = int(input)
        elif (tipo == 'float'):
            number = float(input)

        if (number < 0):
            return -1

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

def novoAluno(aluno):  # --- CASO 1 ---
    if (aluno):
        print('\n------ ALUNO ------')
        printAluno(aluno)
    verificacao = False
    nome = ''
    while (verificacao != True):
        nome = input('Nome do aluno: ')
        verificacao = nomeValido(nome)
        if (verificacao != True):  # se o nome for inválido
            print(verificacao)  # printa a mensagem dizendo o que tá errado

    cpf = input('CPF do aluno: ')

    peso = -1
    while peso == -1:
        peso = numeroValido('float', input('Peso do aluno: '))
        if (peso == -1):
            print('Peso inválido')

    altura = -1
    while altura == -1:
        altura = numeroValido('float', input('Altura do aluno: '))
        if (altura == -1):
            print('Altura inválida')

    if (aluno):
        idAluno = listaAlunos.index(aluno)
        listaAlunos[idAluno] = Aluno(nome, cpf, peso, altura, aluno.status)
        print('Aluno atualizado com sucesso')
    else:
        listaAlunos.append(Aluno(nome, cpf, peso, altura, False))
        listaTreinos.append([])
        print('\nAluno cadastrado com sucesso')
    return menu()


def relatorio():  # --- CASO 6 ---
    if (not listaAlunos):
        print('(!) Não há alunos cadastrados no momento')
        return menu()
    print('Menu de relatório de alunos')
    print('  1 - Todos os alunos')
    print('  2 - Alunos ativos')
    print('  3 - Alunos inativos')
    caso = numeroValido('int', input('Digite uma opção: '))

    listaAlunos.sort(key=lambda x: x.nome)
    match caso:
        case 1:
            print('\n------ LISTA ------')
            for aluno in listaAlunos:
                printAluno(aluno)
        case 2:
            print('\n------ LISTA ------')
            for aluno in listaAlunos:
                if aluno.status == True:
                    printAluno(aluno)
        case 3:
            print('\n------ LISTA ------')
            for aluno in listaAlunos:
                if aluno.status == False:
                    printAluno(aluno)
        case _:
            print('(!) Opção inválida')
    return menu()


def excluirAluno(aluno):
    printAluno(aluno)
    print('\nTem certeza que quer excluir o aluno?')
    caso = numeroValido('int', input(
        '1- Sim | 0- Não: '))
    print()
    match caso:
        case 1:
            idAluno = listaAlunos.index(aluno)
            listaAlunos.remove(aluno)
            listaTreinos.pop(idAluno)

            print('Aluno excluído com sucesso')
            return menu()
        case 0:
            return menu()
        case _:
            print('(!) Opção inválida')
            excluirAluno(aluno)


def buscaAlunoNome(nome):  # busca um aluno pelo nome
    for aluno in listaAlunos:
        if (aluno.nome.lower() == nome.lower()):
            return aluno
    return -1  # se não retornar com o aluno, quer dizer que não existe


def printAluno(aluno):
    print('Nome:', aluno.nome, '\nCPF:', aluno.cpf,
          '\nPeso:', aluno.peso, '\nAltura:', aluno.altura,
          '\nStatus:', 'Ativo' if aluno.status == True else 'Inativo')
    print('     ---------')


# TREINO -------------------------------------------------------

def menuTreino(idAluno):
    while True:
        print('\nMenu de Treino')
        print('  1 - Cadastrar novo exercício')
        print('  2 - Alterar exercício')
        print('  3 - Excluir exercício específico')
        print('  4 - Excluir treino todo')
        print('  9 - Voltar ao menu')
        caso = numeroValido('int', input('Digite uma opção: '))
        print()

        match caso:
            case 1:
                return novoExercicio(idAluno)
            case 2:
                return alterarExercicio(idAluno)
            case 3:
                nome = input('Nome do exercício: ')
                return excluirTreino(idAluno, nome)
            case 4:
                return excluirTreino(idAluno, None)
            case 9:
                return menu()
            case _:
                print('(!) Opção inválida')


def novoExercicio(idAluno):
    nome = input('Nome do exercício: ')
    numRep = int(input('Numero de repetições: '))
    pesoExec = float(input('Peso usado no exercício: '))
    exer = Exercicio(nome, numRep, pesoExec)

    for exc in listaTreinos[idAluno]:
        if exer.nome == exc.nome:
            print('\n(!) Exercício já existente na lista')
            return menuTreino(idAluno)

    listaTreinos[idAluno].append(exer)
    print('\nExercício adicionado com sucesso')
    # testa o id dos alunos ate achar o correto e seta o status pra true
    listaAlunos[idAluno].status = True
    return menuTreino(idAluno)


def buscaExercicioNome(idAluno, nome):
    for exercicio in listaTreinos[idAluno]:
        if (exercicio.nome.lower() == nome.lower()):
            return exercicio
    return -1  # se não retornar um exercício, não existe


def alterarExercicio(idAluno):
    nomeExer = input('Nome do exercício: ')
    exercicio = buscaExercicioNome(idAluno, nomeExer)
    if (exercicio == -1):
        print('\n(!) Exercício não encontrado')
        return menuTreino(idAluno)
    else:
        print('\n----- EXERCÍCIO -----')
        printExercicio(exercicio)
        idTreino = listaTreinos[idAluno].index(exercicio)

        novoNome = input('Novo nome: ')
        novaReps = numeroValido('int', input('Novo número de repetições: '))
        novoPeso = numeroValido('float', input('Novo peso: '))

        listaTreinos[idAluno][idTreino] = Exercicio(
            novoNome, novaReps, novoPeso)

        print('\n Exercício alterado com sucesso')
        return menuTreino(idAluno)


def excluirTreino(idAluno, nomeExer):
    if (nomeExer):  # se tiver o nome, vai excluir um exercício específico
        exer = buscaExercicioNome(idAluno, nomeExer)
        if (exer != -1):
            # idTreino = listaTreinos[idAluno].index(exer)
            print('\nTem certeza que quer excluir o exercício?')
            caso = numeroValido('int', input(
                '1- Sim | 0- Não: '))
            print()
            match caso:
                case 1:
                    listaTreinos[idAluno].remove(exer)
                    print('Exercício excluído com sucesso')
                    return menuTreino(idAluno)
                case 0:
                    return menuTreino(idAluno)
                case _:
                    print('(!) Opção inválida')
                    excluirTreino(idAluno, nomeExer)
    else:
        print('Tem certeza que quer excluir o treino todo?')
        caso = numeroValido('int', input(
            '1- Sim | 0- Não: '))
        print()
        match caso:
            case 1:
                listaTreinos[idAluno] = []
                print('O treino do aluno foi excuído')
                return menuTreino(idAluno)
            case 0:
                return menuTreino(idAluno)
            case _:
                print('(!) Opção inválida')
                excluirTreino(idAluno, nomeExer)


def printExercicio(exer):
    print('Exercício:', exer.nome,
          '\nRepetições:', exer.numRep,
          '\nPeso:', exer.pesoExec)
    print('    ----------')


def main():
    return menu()


main()
