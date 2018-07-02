import contextlib
import hashlib
import os
import pickle
import sys
import typing

try:
    from pathlib import Path
except ImportError:
    Path = None
_join = os.path.join
if Path:
    mdi_home = str(Path.home())
else:
    mdi_home = os.path.expanduser("~")
if len(sys.argv) > 1:
    _root = sys.argv[1]
    if _root == ".":
        mdi_root = os.getcwd()
    elif os.path.isdir(_root):
        mdi_root = _root
    else:
        raise FileNotFoundError
elif sys.platform.startswith("win"):
    mdi_root = _join(mdi_home, "AppData/Local/")
elif sys.platform.startswith("darwin"):
    mdi_root = _join(mdi_home, "Library/Application Support/")
else:
    mdi_root = mdi_home
mdi_root = _join(mdi_root, "w7-mdi/")
mdi_id = hashlib.md5(mdi_home.encode()).hexdigest()
mdi_ucf = _join(mdi_root, mdi_id)
_secrets = "secret-file.dat"
_secrets_fp = _join(mdi_ucf, _secrets)
mdi_files = [_secrets]
mdi_fp = [_secrets_fp]
if not os.path.isdir(mdi_ucf):
    os.makedirs(mdi_ucf)


@contextlib.contextmanager
def _reg():
    if os.path.isfile(_secrets_fp):
        with open(_secrets_fp, "rb") as sec_f:
            reg = pickle.load(sec_f)
    else:
        reg = {}
    yield reg
    with open(_secrets_fp, "wb") as sec_f:
        pickle.dump(reg, sec_f)


def str_reg(key: "str",
            prompt: "typing.Union[str, None]" = None) -> "typing.Union[str, None]":
    with _reg() as reg:
        if key in reg.keys():
            return str(reg[key])
        if prompt is None:
            return None
        val = input(prompt).strip()
        reg[key] = val
        return val
