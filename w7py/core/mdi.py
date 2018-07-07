import atexit
import hashlib
import os
import pickle
import shutil
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
if sys.platform.startswith("win"):
    mdi_root = _join(mdi_home, "AppData/Local/")
elif sys.platform.startswith("darwin"):
    mdi_root = _join(mdi_home, "Library/Application Support/")
else:
    mdi_root = mdi_home
mdi_root = _join(mdi_root, "w7-mdi/")
mdi_id = hashlib.md5(mdi_home.encode()).hexdigest()
mdi_ucf = _join(mdi_root, mdi_id)
if not os.path.isdir(mdi_ucf):
    os.makedirs(mdi_ucf)
_root_file = "{}.dat".format(mdi_id)
_root_fp = _join(mdi_ucf, _root_file)
_path_file = "{}.dat".format(hashlib.md5(os.getcwd().encode()).hexdigest())
_path_fp = _join(mdi_ucf, _path_file)
mdi_files = [_root_file, _path_file]
mdi_fp = [_root_fp, _path_fp]
if os.path.isfile(_root_fp):
    with open(_root_fp, "rb") as rf:
        mdi_reg = pickle.load(rf)
else:
    mdi_reg = {}
if os.path.isfile(_path_fp):
    with open(_path_fp, "rb") as rf:
        mdi_path_reg = pickle.load(rf)
else:
    mdi_path_reg = {}
_mdi_should_remove_all = False


def sys_reg_prompt(key: "str",
                   prompt: "typing.Optional[str]" = None) -> "typing.Optional[str]":
    if key in mdi_reg.keys():
        return str(mdi_reg[key])
    if prompt is None:
        return None
    val = input(prompt).strip()
    mdi_reg[key] = val
    return val


def clean():
    mdi_reg.clear()
    mdi_path_reg.clear()


def remove_all():
    global _mdi_should_remove_all
    _mdi_should_remove_all = True


@atexit.register
def _mdi_cleanup():
    if _mdi_should_remove_all:
        shutil.rmtree(mdi_root)
    else:
        with open(_root_fp, "wb") as wf:
            pickle.dump(mdi_reg, wf)
        with open(_path_fp, "wb") as wf:
            pickle.dump(mdi_path_reg, wf)
