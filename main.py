from domino.falling import Falling


def main():
    falling = Falling()
    falling.domino_alg(iterations=1, domino=r"||//||\||/\|")
    falling.domino_alg(iterations=2, domino=r"||////\\\|////|", reverse=True)

if __name__ == "__main__":
    main()
