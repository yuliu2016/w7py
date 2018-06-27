import argparse
import os
import sys
import shutil

_d_pfx = "w7"

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

setup_parser = subparsers.add_parser("setup", help="Set up the system")
setup_parser.add_argument("-d", "--dir", help="The directory to setup", default=os.getcwd(), dest="dp")

subparsers.add_parser("remove", help="Remove the system")


def _confirm(s):
    print(s)
    yn = input("Proceed?[y/N] ")
    return yn == "y" or yn == "Y"


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

args = parser.parse_args()

if args.command == "setup":
    os.chdir(args.dp)
    if os.path.exists(_d_pfx):
        do_rm = _confirm("Path already exists. "
                         "It will be removed and a new one recreated")
        if not do_rm:
            sys.exit()
        shutil.rmtree(_d_pfx)
    os.mkdir(_d_pfx)
    os.chdir(_d_pfx)
    for i in ["in", "out", "boards", "db", "scripts"]:
        os.mkdir(i)
    if sys.platform == "win32":
        with open("install.bat", "w") as v_inst:
            # Setup env
            pass
    os.chdir("scripts")


elif args.command == "rm":
    do_rm = _confirm("Remove the entire system?")
    if not do_rm:
        sys.exit()
    shutil.rmtree(_d_pfx)
