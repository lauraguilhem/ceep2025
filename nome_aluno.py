# Nome correto
nome_certo = "Ana"

# Contador de tentativas
tentativas = 0

# Pergunta como o usuário quer tentar
print("Escolha uma opção:")
print("1 - Digitar o nome completo")
print("2 - Montar o nome letra por letra")
print("Digite 'sair' para encerrar.")
opcao = input("Digite 1, 2 ou 'sair': ")

# Laço para tentar 6 vezes
while tentativas < 6:
    if opcao == "sair":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        # Opção 1: Digitar o nome completo
        nome = input("Digite o nome: ")
        if nome.lower() == nome_certo.lower():
            print("Nome correto! Parabéns!")
            break
        else:
            tentativas += 1
            print(f"Nome errado! Restam {6 - tentativas} tentativa(s).")
    elif opcao == "2":
        # Opção 2: Montar letra por letra
        nome_montado = ""
        print(f"Monte o nome com {len(nome_certo)} letras.")
        for i in range(len(nome_certo)):
            letra = input(f"Digite a letra {i+1}: ")
            # Validar se é uma única letra
            if len(letra) != 1:
                print("Por favor, digite apenas uma letra.")
                break
            nome_montado += letra
        else:  # Executa se o laço for completado sem break
            if nome_montado.lower() == nome_certo.lower():
                print("Nome correto! Parabéns!")
                break
            else:
                tentativas += 1
                print(f"Nome errado! Restam {6 - tentativas} tentativa(s).")
    else:
        print("Opção inválida! Escolha 1, 2 ou 'sair'.")
        opcao = input("Digite 1, 2 ou 'sair': ")
        continue

if tentativas == 6:
    print("Acabaram as tentativas. O nome correto era:", nome_certo)