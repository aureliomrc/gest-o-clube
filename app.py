import banco
import sys

def exibir_menu():
    print("\n" + "="*30)
    print("   GESTÃO DE SÓCIOS - CLUBE   ")
    print("="*30)
    print("1. Cadastrar Sócio")
    print("2. Listar Sócios")
    print("3. Atualizar Status (Ativar/Inativar)")
    print("4. Remover Sócio")
    print("5. Sair")
    print("-" * 30)

def main():
    # Garante que a tabela existe ao iniciar
    banco.criar_tabela()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome completo: ")
            cpf = input("CPF (apenas números): ")
            plano = input("Plano (Gold/Silver): ")
            banco.adicionar_socio(nome, cpf, plano)
            
        elif opcao == '2':
            socios = banco.listar_socios()
            print("\n--- LISTA DE SÓCIOS ---")
            print(f"{'ID':<5} {'NOME':<20} {'CPF':<15} {'PLANO':<10} {'STATUS'}")
            for s in socios:
                status = "Ativo" if s[4] == 1 else "Inativo"
                print(f"{s[0]:<5} {s[1]:<20} {s[2]:<15} {s[3]:<10} {status}")
                
        elif opcao == '3':
            id_socio = input("ID do sócio: ")
            status = input("Novo status (1 para Ativo, 0 para Inativo): ")
            banco.atualizar_status(id_socio, status)

        elif opcao == '4':
            id_socio = input("ID do sócio para remover: ")
            banco.deletar_socio(id_socio)

        elif opcao == '5':
            print("Saindo do sistema...")
            sys.exit()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()