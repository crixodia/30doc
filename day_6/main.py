from random import shuffle

# Objeto Tarjeta de Jugador
class Card(object):
    def __init__(self, player="Jugador"):
        B = self.gen_row(1, 16)
        I = self.gen_row(16, 31)
        N = self.gen_row(31, 46, free=True)
        G = self.gen_row(46, 61)
        O = self.gen_row(61, 76)

        self.card = [B, I, N, G, O]
        self.player = player
        self.played = [[0] * 5 for i in range(5)]
        self.win = []

        T = []
        for i in range(5):
            T.append([0] * 5)
            for j in range(5):
                T[i][j] = self._f(self.card[j][i])

        self.T = T
        self.play(0)

    def gen_row(self, a, b, free=False) -> list:
        L = list(range(a, b))
        shuffle(L)
        if free:
            L[2] = 0
        return L[:5]

    def _f(self, n: int) -> str:
        if n > 9:
            return "0" + str(n)
        return "00" + str(n)

    def str(self):
        d = "┌───" + "───".join(["┬"] * 4) + "───┐\n"
        s = [d]
        s += ["│ B │ I │ N │ G │ O │\n"]
        d = d.replace("┌", "├").replace("┐", "┤").replace("┬", "┼")
        s += [d]
        for i, row in enumerate(self.T):
            s += ["│" + "│".join(row) + "│\n"]
            if i == len(row) - 1:
                d = d.replace("├", "└").replace("┤", "┘").replace("┼", "┴")
            s += [d]
        return ["\033[7;34m" + self.player.center(21) + "\033[0;37m\n"] + s

    def __str__(self):
        d = "┌───" + "───".join(["┬"] * 4) + "───┐\n"
        s = d + "│ B │ I │ N │ G │ O │\n"
        d = d.replace("┌", "├").replace("┐", "┤").replace("┬", "┼")
        s += d
        for i, row in enumerate(self.T):
            s += "│" + "│".join(row) + "│\n"
            if i == len(row) - 1:
                d = d.replace("├", "└").replace("┤", "┘").replace("┼", "┴")
            s += d
        return "\033[7;34m" + self.player.center(21) + "\033[0;37m\n" + s

    # Juega el turno
    def play(self, n: int):
        i, j = 0, 0
        while i < 5:
            j = 0
            while j < 5:
                if self.card[i][j] == n:
                    self.played[i][j] = 1
                    self.T[j][i] = "\033[7;31m" + self.T[j][i] + "\033[0;37m"
                j += 1
            i += 1

        # Columna
        for i, row in enumerate(self.played):
            if sum(row) == 5 and f"c{i}" not in self.win:
                self.win.append(f"c{i}")

        s = 0
        playedT, D1, D2 = [], [], []
        inv = self.played[::-1]
        for i in range(5):
            playedT.append([0] * 5)
            for j in range(5):
                playedT[i][j] = self.played[j][i]
                s += playedT[i][j]
                if i == j:
                    D1.append(self.played[j][i])
                    D2.append(inv[i][j])

        # Fila
        for i, col in enumerate(playedT):
            if sum(col) == 5 and f"r{i}" not in self.win:
                self.win.append(f"r{i}")

        # Diagonal 1
        if sum(D1) == 5 and "d1" not in self.win:
            self.win.append("d1")

        # Diagonal 2
        if sum(D2) == 5 and "d2" not in self.win:
            self.win.append("d2")

        if s == 25:
            self.win.append("b")

        if (
            self.played[0][0]
            + self.played[4][4]
            + self.played[4][0]
            + self.played[0][4]
            + self.played[2][2]
            == 5
        ) and "x" not in self.win:
            self.win.append("x")
        return self.win


# Bingo completo
class Bingo(object):
    def __init__(self, n: int) -> None:
        self.n = n
        self.cards = []
        self.balls = list(range(1, 76))
        self.played = []
        self.wins = {}

        # Crea n jugadores con sus respectivas cartas
        for i in range(n):
            self.cards.append(Card(f"Jugador {i}"))
            self.wins[f"Jugador {i}"] = []

    # Jugar aleatoriamente
    def play(self):
        shuffle(self.balls)
        ball = self.balls.pop()
        for card in self.cards:
            self.played.append(ball)
            card.play(ball)
            self.wins[card.player] = card.win
        return ball

    def __str__(self):
        s = ""
        for i in range(len(self.cards[0].str())):
            for card in self.cards:
                s += str(card.str()[i]).replace("\n", "") + " "
            s += "\n"

        return s


if __name__ == "__main__":
    bingo = Bingo(int(input("Numero de jugadores: ")))
    while bingo.balls:
        print(bingo)
        option = input("[1] Siguiente bola\n[2] Mostrar estados\n[3] Ayuda\n<< ")
        print()
        if option == "1":
            print(f"Jugando: {bingo.play()}")
            print(f"Bolas restantes: {len(bingo.balls)}\n")
        elif option == "2":
            print(bingo.wins, "\n")
        elif option == "3":
            print("Fila:", "r")
            print("Columna: ", "c")
            print("Esquinas: ", "x")
            print("Diagonal: ", "d")
            print("Completo: ", "b\n")
        else:
            print("Opcion incorrecta")
