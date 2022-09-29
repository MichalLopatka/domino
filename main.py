

def forward_alg():
    X = 2
    domino = r"||//||\||/\|"
    domino = list(domino)
    for _ in range(X):
        changes = {"/": [], "\\": []}
        for i in range(len(domino)-1):
            if domino[i] == "/" and domino[i+1] == "|":
                changes["/"].append(i+1)
            if domino[i] == "|" and domino[i+1] == "\\":
                changes["\\"].append(i)
        print(changes)
        for el in changes["/"]:
            domino[el] = "/"
        for el in changes["\\"]:
            domino[el] = "\\"
        print(''.join(domino))

def reverse_alg():
    X = 2
    domino = r"||////\\\|////|"
    domino = list(domino)
    for _ in range(X):
        changes = {"|": []}
        for i in range(len(domino)-1):
            if domino[i] == "/" and domino[i+1] == "\\":
                changes["|"].append(i+1)
                changes["|"].append(i)
            if domino[i] == "/" and domino[i+1] == "|":
                changes["|"].append(i)
            if domino[i] == "|" and domino[i+1] == "\\":
                changes["|"].append(i+1)
        for el in changes["|"]:
            domino[el] = "|"
        print(''.join(domino))



if __name__ == "__main__":
    # forward_alg()
    reverse_alg()
