print("Vamos calcular sua média!")
nota1 = float(input("Diga a 1a nota: "))
nota2 = float(input("Diga a 2a nota: "))
nota3 = nota1 + nota2 / 2

if nota3 >= 70:
    print(f"Sua média é {nota3}, passou!")
else:
    print(f"Sua média é {nota3}, não passou!")