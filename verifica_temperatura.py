#Laura Guilhem 25 1E
print("Vamos verificar a temperatura!")
temperatura = float(input("Digite a temperatura em graus Celsius: "))
if temperatura < 0:
    print("Está congelando")
elif temperatura <= 15:
    print("Está frio")
elif  temperatura <= 30:
    print("A temperatura está normal")
else:
    print("Está calor")