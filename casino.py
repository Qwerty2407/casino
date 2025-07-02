import random
import tkinter


class Game:
    def __init__(self, jackpot_spins) -> None:
        self.num = None
        self.victory_list = None
        self.jackpot_spins = jackpot_spins
        self.loss_list = ["banana.png", "cherry.png", "cigar.png", "grape.png", "limon.png", "raspberry.png",
                          "strawberry.png", "watermelon.png"]
        self.pictures = None

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
            self.pictures = ["diamond.png"] * 3
        elif result == self.victory_list[1]:
            self.num = random.randint(15, 25)
            self.pictures = ["crown.png"] * 3
        elif result == self.victory_list[1]:
            self.num = random.randint(5, 15)
            self.pictures = ["clover.png"] * 3
        else:
            self.num = random.randint(2, 5)
            self.pictures = ["coins.png"] * 3

    def loss(self) -> None:
        while self.pictures is None:
            self.pictures = [a, b, c] if len(
                {a := random.choice(self.loss_list) + ["crown.png", "coins.png"],
                 b := random.choice(self.loss_list + ["seven.png", "coins.png", "clover.png", "diamond.png"]),
                 c := random.choice(self.loss_list)}) == 3 else None


class GUI:
    def __init__(self, mode: str, pictures: list[str]) -> None:
        self.mode = mode
        self.pictures = pictures

    def create(self):
        pass


if __name__ == "__main__":
    Game(random.randint(3, 6)).victory_check(random.randint(1, 25))
