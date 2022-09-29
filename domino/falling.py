from typing import Dict


class Falling:
    def domino_alg(self, iterations: int, domino: str, reverse: bool = False):
        """
        Main class method calling other to concduct algorithm
        param iterations: int
            number of iterations of algorithm
        param domino: str
            input domino consisting of '/|\\'
        reverse: bool= False
            choose reverse algorithm or forward
        returns: domino on stdout
        """
        self.domino = list(domino)
        if reverse:
            for _ in range(iterations):
                self.change_domino(changes=self.mark_reverse_changes())
        else:
            for _ in range(iterations):
                self.change_domino(changes=self.mark_forward_changes())
        self.print_domino()

    def mark_forward_changes(self) -> Dict:
        """
        Choose domino pieces to fall either back or forward
        returns: a dictionary consisting of the domino pieces mapped to the direction
        """
        changes: Dict = {"/": [], "\\": []}
        for i in range(len(self.domino) - 1):
            if self.domino[i] == "/" and self.domino[i + 1] == "|":
                changes["/"].append(i + 1)
            if self.domino[i] == "|" and self.domino[i + 1] == "\\":
                changes["\\"].append(i)
        return changes

    def mark_reverse_changes(self) -> Dict:
        """
        Choose domino pieces that have fallen in last iteration
        returns a dictionary consisting of the domino pieces to reverse
        """
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
        """
        Modify domino pieces with given indexes
        """
        for key in changes:
            for el in changes[key]:
                self.domino[el] = str(key)

    def print_domino(self):
        """
        Print final domino
        """
        print("".join(self.domino))
