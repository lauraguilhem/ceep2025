#Laura Guilhem 25 1E
print("Vamos fazer uma conta de subtração ou adição!")
conta = input("Digite que conta você quer fazer: ").lower()

if conta == "adição":
N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
resultado = N1 + N2
    print(f"O resultado da adição é {resultado}")
elif conta == "subtração":
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resultado = n1 - n2
    print(f"O resultado da subtração é {resultado}")
else:
    print("Digite uma conta válida, por favor!")