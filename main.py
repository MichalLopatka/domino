from domino.manage import ManageFlow


def main():
    manage = ManageFlow()
    manage.input()
    manage.call_domino()


if __name__ == "__main__":
    main()
