print("Olá! Vamos comparar dois números?")

num1 = int(input("Por favor, me informe o primeiro número: "))
num2 = int(input("Por favor, me informe o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num1 < num2:
    print(f"O número {num1} é menor que o número {num2}")
elif num1 == num2:
    print(f"Os dois números, {num1} e {num2} são iguais.")    