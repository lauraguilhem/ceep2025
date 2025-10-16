#Laura Guilhem 25 1E
print("Vamos classificar um triângulo!")
A = float(input("Digite o valor do primeiro lado: "))
B = float(input("Digite o valor do segundo lado: "))
C = float(input("Digite o valor do terceiro lado: "))
if A == B == C:
    print("O triângulo é equilátero.")
elif A == B or B == C or A == C:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")    
