import random
import tkinter


class Game:
    def __init__(self, jackpot_spins):
        self.num = None
        self.victory_list = None
        self.jackpot_spins = jackpot_spins

    def victory_check(self, result: int) -> None:
        while self.victory_list is None:
            self.victory_list = [a, b, c, d] if len(
                {a := random.randint(1, 12), b := random.randint(1, 12), c := random.randint(1, 12),
                 d := random.randint(1, 12)}) == 4 else None

        if result == 13:
            self.jackpot()
        elif result in self.victory_list:
            self.victory(result)
        else:
            self.loss()

    def jackpot(self) -> None:
        pass

    def victory(self, result: int) -> None:
        if result == self.victory_list[0]:
            self.num = random.randint(25, 40)
            picture = "diamond.png"
        elif result == self.victory_list[1]:
            self.num = random.randint(15, 25)
            picture = "crown.png"
        elif result == self.victory_list[1]:
            self.num = random.randint(5, 15)
            picture = "clover.png"
        else:
            self.num = random.randint(2, 5)
            picture = "coins.png"

    def loss(self) -> None:
        pass


class GUI:
    def create(self):
        window = tkinter.Tk()
        window.geometry("600x700")
        window.title('Paper, scissors, stone')

        c = tkinter.Canvas(window, width=600, height=700, bg='green')
        c.pack()

        seven = tkinter.PhotoImage(file="images/seven.png")
        c.create_image(190, 60, anchor=tkinter.NW, image=seven)

        window.mainloop()


if __name__ == "__main__":
    # GUI().create()
    Game(random.randint(3, 6)).victory_check(random.randint(1, 13))
