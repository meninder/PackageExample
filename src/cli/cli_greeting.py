import argparse
from src.greeting import greet


def parse_args():
    """
    Parse CLI arguments

    :return: object with arguments

    """

    parser = argparse.ArgumentParser(description="Printing hello from a greeter ")

    # name
    parser.add_argument('-g', '--greeter', metavar="<greeter>", type=str, help="Put your name", default="[Default]: Meninder")

    return parser.parse_args()


def main():
    args = parse_args()
    try:
        greet(
            greeter=args.greeter
        )
    except Exception as e:
        print("This didn't work for you")


if __name__ == '__main__':
    main()
