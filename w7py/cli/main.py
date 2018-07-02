import sys

from .clip import clip
from .. import tba_v3 as tba
from ..core import mdi
from ..tba_v3.client import client_instance


def cli_main():
    if len(sys.argv) == 1:
        clip.print_help()
        return
    args = clip.parse_args()
    if args.command == "qms":
        qms(args)


def qms(args):
    if not client_instance.auth_key:
        key = mdi.str_reg("tba_key", "Please enter your TBA key to continue: ")
        client_instance.set_key(key)
    with tba.session(overwrite_id="qms", event_key=args.event_key) as s:
        event = tba.event_helper(s)
        event.check_validity()
