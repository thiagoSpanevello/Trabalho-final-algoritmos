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


listaAlunos = []
listaExerc = []


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
                    return menuTreino()
                else:
                    print('Aluno não encontrado')

            case 3:
                nomeAluno = input('Digite o nome do aluno: ')
                aluno = buscaAlunoNome(nomeAluno)
                if (aluno != -1):
                    print('------ ALUNO ------')
                    print('Nome:', aluno.nome, '\nCPF:', aluno.cpf,
                          '\nPeso:', aluno.peso, '\nAltura:', aluno.altura)
                    print('----- TREINO -----')
                else:
                    print('Aluno não encontrado')

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
        if (len(input) <= 3):
            return '\n(!) Nome precisa ter mais de 3 letras\n'
        else:
            return True


# ALUNO -------------------------------------------------------

def novoAluno():  # --- CASO 1 ---
    new = Aluno()

    verificacao = False
    while (verificacao != True):
        new.nome = input('Nome do aluno: ')
        verificacao = nomeValido(new.nome)
        if (verificacao != True):  # se o nome for inválido
            print(verificacao)  # printa a mensagem dizendo o que tá errado

    new.cpf = input('CPF do aluno: ')
    new.peso = input('Peso do aluno: ')
    new.altura = input('Altura do aluno: ')
    listaAlunos.append(new)
    listaExerc.append([])
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
                print('Nome:', aluno.nome, '\nCPF:', aluno.cpf,
                      '\nPeso:', aluno.peso, '\nAltura:', aluno.altura)
                print('     -----')
        case 2:
            print('------ LISTA ------')
            for aluno in listaAlunos:
                if aluno.status == True:
                    print('Nome:', aluno.nome, '\nCPF:', aluno.cpf,
                          '\nPeso:', aluno.peso, '\nAltura:', aluno.altura)
                    print('     -----')
        case 3:
            print('------ LISTA ------')
            for aluno in listaAlunos:
                if aluno.status == False:
                    print('Nome:', aluno.nome, '\nCPF:', aluno.cpf,
                          '\nPeso:', aluno.peso, '\nAltura:', aluno.altura)
                    print('     -----')
        case _:
            print('Opção inválida')
    return menu()


def buscaAlunoNome(nome):  # busca um aluno pelo nome
    for aluno in listaAlunos:
        if (aluno.nome.lower() == nome.lower()):
            return aluno
    return -1  # se não retornar com o aluno, quer dizer que não existe


# TREINO -------------------------------------------------------

def menuTreino():
    print('Menu de Treino')
    print('  1 - Cadastrar novo exercício')
    print('  2 - Alterar exercício')
    print('  3 - Excluir exercício específico')
    print('  4 - Excluir treino todo')
    caso = numeroValido('int', input('Digite uma opção: '))
    print()
    match caso:
        case 1:
            print('n ta feito')
        case _:
            print('Opção inválida')


def novoExercicio(idAluno):
    x = int(input('Digite 9 para sair'))
    while True:
        if x == 9:
            break
        else:
            exer = Exercicio()
            exer.nome = input('Nome do exercício: ')
            exer.numRep = int(input('Numero de repetições: '))
            exer.pesoExec = input('Peso usado no exercício: ')
            if exer in listaExerc[idAluno]:
                print('Exercício já existente na lista')
                return menu()
            else:
                listaExerc[idAluno].append(exer)
                print('Exercício adicionado com sucesso')
                # testa o id dos alunos ate achar o correto e seta o status pra true
                for i in range(listaAlunos):
                    if i == idAluno:
                        listaAlunos[i].status == True
    return menu()


def main():
    return menu()


main()
