import emoji


def emijizer(msg):
    return emoji.emojize(msg)


if __name__ == "__main__":
    msg = input("TYPE YOUR MESSAGE:\n")
    print(emijizer(msg))
