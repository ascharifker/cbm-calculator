import argparse
from cbm_calculator import Box, Container, containers_needed

DEFAULT_CONTAINER = Container(length=5.9, width=2.35, height=2.39)

def parse_args():
    parser = argparse.ArgumentParser(description="CBM container calculator")
    parser.add_argument('--box', action='append', nargs=4, metavar=('L','W','H','Q'),
                        help='Box dimensions in meters and quantity',
                        required=True)
    parser.add_argument('--container', nargs=3, metavar=('L','W','H'),
                        help='Container dimensions in meters',
                        type=float)
    return parser.parse_args()


def main():
    args = parse_args()
    boxes = [Box(float(l), float(w), float(h), int(q)) for l, w, h, q in args.box]
    if args.container:
        container = Container(*map(float, args.container))
    else:
        container = DEFAULT_CONTAINER
    count = containers_needed(boxes, container)
    print(f"Containers needed: {count}")

if __name__ == "__main__":
    main()
