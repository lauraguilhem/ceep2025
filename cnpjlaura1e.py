# Main
TAM_CNPJ = 18  
cnpj = input("Insira o CNPJ (formato XX.XXX.XXX/XXXX-XX): ")
flag = True


if len(cnpj) != TAM_CNPJ:
    flag = False
elif cnpj[2] != "." or cnpj[6] != "." or cnpj[10] != "/" or cnpj[15] != "-":
    flag = False
else:
   
    for i in range(TAM_CNPJ):
        if (i != 2 and i != 6 and i != 10 and i != 15):  
            if not cnpj[i].isdigit():  
                flag = False
                break

if flag:
    print("Formato de CNPJ válido.")
else:
    print("O CNPJ informado não tem um formato válido.")
