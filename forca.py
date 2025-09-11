print("Vamos jogar!")

palavra = "girafa"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]
tentativas = 6

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra:
        index = 0
        for letra in palavra:
            if palpite == letra:
                letras_acertadas[index] = letra
            index += 1
    else:
        tentativas -= 1
        print(f"Você tem {tentativas} tentativas restantes.")
    
    print(" ".join(letras_acertadas))

    if "_" not in letras_acertadas:
        print("Parabéns, você ganhou!")
        break
else:
    print(f"Que pena, você perdeu. A palavra era: {palavra}")
