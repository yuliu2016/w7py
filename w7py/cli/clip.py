"""Command Line Interface Parser"""
import argparse

clip = argparse.ArgumentParser()
subparsers = clip.add_subparsers(dest="command")

qms = subparsers.add_parser("qms", help="Displays the qualification match schedule")
qms.add_argument("event_key")
qms.add_argument("-df", "--use-data-frame", required=False, dest="df", action="store_true")
qms.add_argument("-t", "--transpose", required=False, dest="transpose", action="store_true")
