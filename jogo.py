#Biblioteca que irá gerar um valor aleatório da lista de palavras
import random

#Class para definir a lista de palavras
class WordGuessGame:
    def __init__(self):
        self.word_bank = [
            "paralelepipedo",
            "ornitorrinco",
            "estetoscopio",
            "catecismo",
            "python",
            "software",
            "biblioteca",
            "desenvolvimento",
            "dicionario"
        ]
        self.restart()
        
#Função para iniciar uma partida nova
    def restart(self):
        self.word = random.choice(self.word_bank) #comando para sortear uma palavra aleatória da lista
        self.guessed_word = ["_"] * len(self.word) #comando para ocultar a palavra somente com "_"
        self.attempts = 10 #Quantidade de tentativas para acertar a letra
        self.guesses = set() #Cria um conjunto vazio para armazenar as letras já usadas
    
    #Função para adivinhar a letra
    def guess_letter(self, letter):

        #verifica uma tentativa e retorna: mensagem, status

        letter = letter.lower().strip() 

        #Verifica se a letra é válida, se já foi usada ou se é repetida
        if len(letter) != 1 or not letter.isalpha():
            return "Digite apenas uma letra: ", "invalido"
        
        if letter in self.guesses:
            return "Você já tentou essa letra colega!", "repetido"
        
        #Adiciona a letra ao conjunto de letras já usadas
        self.guesses.add(letter) 

        if letter in self.word:
            for index, character in enumerate(self.word):
                if character == letter:
                    self.guessed_word[index] = letter

            if "_" not in self.guessed_word:
                return f"Parabéns! Você acertou a palavra: {self.word}", "vitoria"
            
            return "Boa, encontrou a letra!", "correto"
    
    #Caso a letra não esteja na palavra, diminui o número de tentativas e verifica se o jogador perdeu
        self.attempts -= 1

        if self.attempts == 0:
            return f"Você perdeu! A palavra era: {self.word}", "derrota"
    
        return (
        f"Letra incorreta! Ainda restam {self.attempts} tentativas.", "incorreto"

        )

    #Função para mostrar a palavra oculta com espaços entre as letras
    def visible_word(self):
        return " ".join(self.guessed_word)

    #Função para mostrar as letras já usadas e em ordem alfabética
    def used_letters(self):
        return "Letras já usadas: " + ", ".join(sorted(self.guesses))