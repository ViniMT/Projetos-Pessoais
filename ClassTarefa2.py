class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

loop = -1
tarefas = []
while loop != 0:
    print("Bem-vindo ao Programa de Gerenciamento de Tarefas!")
    print("Opções Disponíveis:")
    print("1. Adicionar uma nova tarefa.")
    print("2. Marcar uma tarefa como concluída.")
    print("3. Remover uma tarefa.")
    print("4. Exibir a lista de tarefas pendentes.")
    print("5. Sair do programa.\n")

    opcao = int(input("Digite o número correspondente à opção desejada: "))
    if opcao == 1:
        print("Opção selecionada: Adicionar uma nova tarefa.\n")
        descricao = input("Por favor, insira a descrição da nova tarefa: ")
        tarefas.append(Tarefa(descricao))
        print(f'Tarefa "{descricao}" adicionada com sucesso!\n')
    elif opcao == 2:
        print("Opção selecionada: Marcar uma tarefa como concluída.\n")
        if not tarefas:
            print("Não há tarefas disponíveis para marcar como concluídas.\n")
        else:
            print("Lista de Tarefas Pendentes:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa.titulo}")
            numero_tarefa = int(input("\nPor favor, insira o número da tarefa a ser marcada como concluída: "))
            if 1 <= numero_tarefa <= len(tarefas):
                tarefas[numero_tarefa - 1].concluida = True
                print(f'Tarefa "{tarefas[numero_tarefa - 1].titulo}" marcada como concluída!\n')
            else:
                print("Número de tarefa inválido.\n")
    elif opcao == 3:
        print("Opção selecionada: Remover uma tarefa.\n")
        # Implementar remoção de tarefa, se desejado.
        pass
    elif opcao == 4:
        print("Opção selecionada: Exibir a lista de tarefas pendentes.\n")
        if not tarefas:
            print("Não há tarefas pendentes.\n")
        else:
            print("Lista de Tarefas Pendentes:")
            for i, tarefa in enumerate(tarefas, 1):
                if not tarefa.concluida:
                    print(f"{i}. {tarefa.titulo}")
            print()
    elif opcao == 5:
        print("Opção selecionada: Encerrando o programa...\n")
        loop = 0
    else:
        print("Opção inválida. Tente novamente.\n")
