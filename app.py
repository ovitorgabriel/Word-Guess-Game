from email.mime import image

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from jogo import WordGuessGame
from PIL import Image, ImageTk

#Inicio do app
class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly") #definição  do tema do app

        self.title("Word Guessing Game") #titulo do app
        self.geometry("500x400") #dimensao do app

        self.jogo = WordGuessGame() #instancia do jogo

        # Rotulo para exibir a mensagem de boas-vindas
        ttk.Label(
            self,
            text = "Bem vindo ao Word Guessing Game!",
            font = ("Arial", 24, "bold")
        ).pack(pady=30)

        # Rotulo para exibir a palavra oculta
        self.word_label = ttk.Label(
            self,
            text = self.jogo.visible_word(),
            font=("Consolas", 25, "bold")
        )
        self.word_label.pack(pady=20)

        # Rotulo para exibir a mensagem de status do jogo
        self.entry = ttk.Entry(
            self,
            width=10,
            font=("Arial", 20),
            justify="center"
        )
        self.entry.pack(pady=20)

        # Botão para verificar a letra digitada
        ttk.Button(
            self,
            text="Verificar",
            bootstyle = SUCCESS,
            command=self.try_letter
        ).pack(pady=10)

        # Rotulo para exibir a mensagem de status do jogo
        self.message_label = ttk.Label(self, text="")
        self.message_label.pack(pady=15)

        self.image_label = ttk.Label(self)
        self.image_label.pack(pady=10)

        self.restart_button = ttk.Button(
            self,
            text = "Jogar novamente",
            bootstyle = PRIMARY,
            command = self.restart_game
        )

    def try_letter(self):
        letter = self.entry.get()

        message, status = self.jogo.guess_letter(letter)

        self.message_label.config(text=message)
        self.word_label.config(text=self.jogo.visible_word())

        self.entry.delete(0, "end")

        if status in ("vitoria", "derrota"):
            self.entry.config(state="desabilitado")
            self.restart_button.pack(pady=10)

        if status == "vitoria":
            self.entry.config(state="desabilitado")
            self.restart_button.pack(pady=10)
            self.show_result_image("imagens/vitoria.jpg")
        
        elif status == "derrota":
            self.entry.config(state="desabilitado")
            self.restart_button.pack(pady=10)
            self.show_result_image("imagens/derrota.png")

    def restart_game(self):
        self.jogo.restart()

        self.word_label.config(text=self.jogo.visible_word())
        self.message_label.config(text="")

        self.entry.config(state="normal")
        self.entry.delete(0, "end")
        self.entry.focus()

        self.restart_button.pack_forget()
    
    def show_result_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((200, 200))

        self.result_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.result_image)

if __name__ == "__main__":
    app = App()
    app.mainloop()