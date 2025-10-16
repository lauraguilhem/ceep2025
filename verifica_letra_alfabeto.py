#Laura Guilhem 25 1E
print("Vamos ver se uma letra é vogal ou consoante!")
letra = input("Digite uma letra do alfabeto: ").lower()
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra válida do alfabeto.")
elif letra in 'aeiou':
    print("A letra '{letra}' é uma vogal.")
else:
    print("A letra '{letra}' é uma consoante.")
