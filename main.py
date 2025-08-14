import random
import tkinter as tk


class MemoryGame:
    def __init__(self, n=4, square_width=80, space=6):
        # Parameters
        self.n = n
        self.moves = 0
        self.square_width = square_width
        self.space = space

        # Couleurs
        self.btn_color = "gray"
        self.txt_color = "black"
        self.border_color = "black"
        self.colors = [
            "red", "blue", "green", "orange",
            "purple", "cyan", "magenta", "brown"
        ] * 2

        self.root = tk.Tk()
        self.root.title("Jeu de la mémoire")

        self.btn = []
        self.returned_btn = []
        self.temp_returned_btn = []
        self.create_game()

    def create_game(self):
        random.shuffle(self.colors)
        for r in range(self.n):
            ligne = []
            for c in range(self.n):
                btn = tk.Button(
                    self.root,
                    width=self.square_width // 5,
                    height=self.square_width // 10,
                    bg=self.btn_color,
                    fg=self.txt_color,
                    highlightbackground=self.border_color,
                    command=lambda r=r, c=c: self.flip_btn(r, c)
                )
                btn.grid(row=r, column=c, padx=self.space, pady=self.space)
                ligne.append(btn)
            self.btn.append(ligne)

    def flip_btn(self, r, c):
        """Action au clic d'un bouton"""
        index = r * self.n + c
        self.btn[r][c].config(bg=self.colors[index])
        if self.btn[r][c] not in self.returned_btn and self.btn[r][c] not in self.temp_returned_btn:
            self.moves += 1
            self.temp_returned_btn.append(self.btn[r][c])

        if len(self.temp_returned_btn) == 2:
            self.check_matching_colors(self.btn[r][c])

        if len(self.temp_returned_btn) > 2:
            self.flip_back_btn(self.btn[r][c])

    def flip_back_btn(self, btn):
        self.temp_returned_btn[0].config(bg=self.btn_color)
        self.temp_returned_btn[1].config(bg=self.btn_color)
        self.temp_returned_btn = []
        self.temp_returned_btn.append(btn)

    def check_matching_colors(self, btn):
        if self.temp_returned_btn[0].cget('bg') == btn.cget('bg'):
            self.returned_btn.append(btn)
            self.returned_btn.append(self.temp_returned_btn[0])
            self.temp_returned_btn = []

        if len(self.returned_btn) == self.n * self.n:
            victoire_label = tk.Label(
                self.root,
                text=f"Victoire en : {self.moves} coups",
                font=("Arial", 16),
                fg="green"
            )
            victoire_label.grid(row=self.n, column=0, columnspan=self.n, pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    jeu = MemoryGame(n=4)
    jeu.run()
