from typing import Dict


class Domino:
    def domino_alg(self, iterations: int, domino: str, reverse: bool = False):
        self.domino = list(domino)
        if reverse:
            for _ in range(iterations):
                self.change_domino(changes=self.mark_reverse_changes())
        else:
            for _ in range(iterations):
                self.change_domino(changes=self.mark_forward_changes())
        self.print_domino()

    def mark_forward_changes(self) -> Dict:
        changes: Dict = {"/": [], "\\": []}
        for i in range(len(self.domino) - 1):
            if self.domino[i] == "/" and self.domino[i + 1] == "|":
                changes["/"].append(i + 1)
            if self.domino[i] == "|" and self.domino[i + 1] == "\\":
                changes["\\"].append(i)
        return changes

    def mark_reverse_changes(self) -> Dict:
        changes: Dict = {"|": []}
        for i in range(len(self.domino) - 1):
            if self.domino[i] == "/" and self.domino[i + 1] == "\\":
                changes["|"].extend([i, i + 1])
            if self.domino[i] == "/" and self.domino[i + 1] == "|":
                changes["|"].append(i)
            if self.domino[i] == "|" and self.domino[i + 1] == "\\":
                changes["|"].append(i + 1)
        return changes

    def change_domino(self, changes):
        for key in changes:
            for el in changes[key]:
                self.domino[el] = str(key)

    def print_domino(self):
        print("".join(self.domino))

if __name__ == "__main__":
    domino = Domino()
    domino.domino_alg(iterations=1, domino=r"||//||\||/\|")
    domino.domino_alg(iterations=2, domino=r"||////\\\|////|", reverse=True)
