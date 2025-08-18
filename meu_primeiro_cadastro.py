print("Laura Guilhem Alonso")

print("**************************")
print("**** Faça seu cadastro****")
print("**************************")
      
nome_completo = input("Digite seu nome completo: ")
def validar_nome(nome):
 
    if all(c.isalpha() or c.isspace() for c in nome):
        return True
    return False

cpf = input("Digite seu CPF: ")
# Main
TAM_CPF = 11
flag = True


if len(cpf) != TAM_CPF:
    flag = False

elif cpf[3] != "." or cpf[7] != "." or cpf[-3] != "-":
    flag = False
else:
    
    for i in range(TAM_CPF):
        if (i != 3) and (i != 7) and (i != 11):  
            c = cpf[i]
            if not c.isdigit():  
                flag = False
                break

if flag:
    print("Formato de CPF válido.")
else:
    print("O CPF informado não tem um formato válido.")


data_nascimento = input("Digite sua data de nascimento: ")

colegio_que_estuda = input("Digite o nome do colégio em que estuda: ")

endereço = input("Digite seu endereço: ")

CEP = input("Digite o seu CEP: ")