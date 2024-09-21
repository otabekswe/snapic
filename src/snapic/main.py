from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        prog='snapic',
        usage='',
        description='',
        epilog='',
        add_help=''   
    )
    path = parser.add_argument('path', type=str, help='Path to the image')
    width = parser.add_argument('-w', '--width', type=int, help='width of the image: 1048')
    height = parser.add_argument('-h', '--height', type=int, help='height of the image: 1048')
    box = parser.add_argument('-b', '--box', type=tuple, help='size in the following format: (width, height) -> (1024, 2048)')
    size = parser.add_argument('-s', '--size', type=str, help='size in the following format: 1024x2048')

    args = parser.parse_args()
    


if __name__ == "__main__":
    main()