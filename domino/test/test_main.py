from domino.falling import Falling


def test_domino0():
    falling = Falling()
    falling.domino_alg(iterations=1, domino=r"||//||\||/\|")

    assert "".join(falling.domino) == r"||///\\||/\|", "Źle się przewróciło"

def test_domino1():
    falling = Falling()
    falling.domino_alg(iterations=2, domino=r"||////\\\|////|", reverse=True)
    assert "".join(falling.domino) == r"||//||||\|//|||", "Źle się przewróciło"
