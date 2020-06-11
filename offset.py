from argparse import ArgumentParser


def offset(message: str, direction: str, steps: int) -> str:

    modifier = 1 if direction == "r" else -1
    new_message = []

    for word in message.split(" "):
        new_word = []

        for index, char in enumerate(word, start=1):

            if char.isalpha():
                lb = 65 if char.isupper() else 97
                nc = chr((ord(char) - lb + index * steps * modifier) % 26 + lb)
                new_word.append(nc)

            else:
                new_word.append(char)

        new_message.append("".join(new_word))

    return " ".join(new_message)


def main():
    parser = ArgumentParser(description="Encrypts/Decrypts a message.")

    mh = "message to be encoded/decoded"
    dh = "direction of encoding/decoding"
    sh = "encoding/decoding step modifier"

    parser.add_argument("--message", help=mh, required=True, type=str)
    parser.add_argument("--direction", help=dh, choices="lr", default="r", type=str)
    parser.add_argument("--steps", help=sh, default=1, type=int)

    args = parser.parse_args()

    print(offset(args.message, args.direction, args.steps))


if __name__ == "__main__":
    main()
