import sys

from .clip import clip


def cli_main():
    if len(sys.argv) == 1:
        clip.print_help()
        return
    args = clip.parse_args()
    if args.command == "qms":
        print("qms")
