
def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar nova tarefa ---")

    # Solicita um título válido
    while True:
        titulo = input("Título da tarefa: ").strip()

        if titulo:
            break

        print("Erro: o título não pode ficar vazio. Tente novamente.")

    # Solicita a descrição
    descricao = input("Descrição da tarefa: ").strip()

    # Solicita uma prioridade válida
    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()

        if prioridade == "alta":
            prioridade = "Alta"
            break
        elif prioridade in ("média", "media"):
            prioridade = "Média"
            break
        elif prioridade == "baixa":
            prioridade = "Baixa"
            break
        else:
            print("Erro: escolha Alta, Média ou Baixa.")

    # Solicita a data limite
    data_limite = input("Data limite: ").strip()

    # Cria o registro da tarefa
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")

    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    tarefas = []

    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
