from domino.falling import Falling


class ManageFlow:
    falling = Falling()

    def input(self):
        print("Enter domino")
        self.domino = input()
        print("Enter no of iterations")
        self.iterations = input()
        print("Reverse algoritms? yes/no")
        self.reverse = input()

    def call_domino(self):
        if self.reverse == "yes":
            self.falling.domino_alg(
                iterations=int(self.iterations), domino=rf"{self.domino}", reverse=True
            )
        else:
            self.falling.domino_alg(
                iterations=int(self.iterations), domino=rf"{self.domino}"
            )
