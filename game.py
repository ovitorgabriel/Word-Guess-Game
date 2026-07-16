#Biblioteca que irá gerar um valor aleatório da lista de palavras
import random

#Lista de palavras que serão sorteadas
word_bank = ["paralelepipedo", "ornitorrinco", "estetoscopio", "catecismo", "python", "software", "biblioteca", "desenvolvimento", "dicionario"]
word = random.choice(word_bank) #comando para sortear uma palavra da lista

guessedWord = ["_"] * len(word) #comando para criar lista com o tamanho da palavra oculta por _
attempts = 10 #quantidade de tentativas para acertar a palavra

while attempts > 0: #laço while para rodar enquanto o jogador tiver chances
    print("\n Palavra atual é: " + " ".join(guessedWord)) 
    guess = input("Digite uma letra: ").lower()

    #Criar um laço if e for parra encontrar a posição da letra no jogo

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Boa, encontrou a letra!")
    else:
        attempts -= 1
        print("Letra incorreta! Você tem " + str(attempts) + " tentativas restantes.")

    #Agora vamos verificar a quantidade de _, se não houver mais, o jogador venceu

    if "_" not in guessedWord:
        print("\nParabéns! Você acertou a palavra: " + word)
        break

    #Caso o jogador perca todas as tentativas, ele perde o jogo

    if attempts == 0:
        print("\nVocê perdeu! A palavra era: " + word)
        