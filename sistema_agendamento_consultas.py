# Sistema de Agendamento de Consultas

# Inicializações
consultas_agendadas = {}

# Função para exibir as opções do menu
def exibir_menu():
    print("\n===== Sistema de Agendamento de Consultas =====")
    print("1. Agendar Consulta")
    print("2. Visualizar Consultas Agendadas")
    print("3. Sair")

# Loop principal
while True:
    exibir_menu()

    # Solicita a escolha do usuário
    escolha = input("Escolha uma opção (1/2/3): ")

    # Verifica a escolha do usuário
    if escolha == '1':
        # Opção: Agendar Consulta
        nome_paciente = input("Digite o nome do paciente: ")
        data_consulta = input("Digite a data da consulta (DD/MM/YYYY): ")

        # Verifica se a data já está agendada
        if data_consulta in consultas_agendadas:
            print("Desculpe, a data já está ocupada. Escolha outra data.")
        else:
            consultas_agendadas[data_consulta] = nome_paciente
            print(f"Consulta agendada para {nome_paciente} na data {data_consulta}.")

    elif escolha == '2':
        # Opção: Visualizar Consultas Agendadas
        if not consultas_agendadas:
            print("Nenhuma consulta agendada.")
        else:
            print("\nConsultas Agendadas:")
            for data, paciente in consultas_agendadas.items():
                print(f"{data}: {paciente}")

    elif escolha == '3':
        # Opção: Sair
        print("Saindo do Sistema de Agendamento de Consultas. Até logo!")
        break

    else:
        # Opção inválida
        print("Opção inválida. Escolha uma opção válida (1/2/3).")