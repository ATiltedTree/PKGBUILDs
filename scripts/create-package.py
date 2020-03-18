#!/usr/bin/env python

import argparse
import enum
import os
import shutil
import types


def log_info(string: str):
    print("[INFO]: " + string)


def log_warn(string: str):
    print("[WARN]: " + string)


def log_err(string: str):
    print("[ERR]: " + string)


class ARCH(enum.Enum):
    AARCH64 = "aarch64"
    X64 = "x86_64"
    X32 = "i686"


class OS(enum.Enum):
    LINUX = "linux"
    NONE = "none"
    WINDOWS = "w64"


class SYSTEMTYPE(enum.Enum):
    GNU = "gnu"
    EABI = "eabi"
    MINGW = "mingw32"
    ELF = "elf"


parser = argparse.ArgumentParser(description="Create a package")

parser.add_argument("--arch", "-a", type=ARCH, default=ARCH.X64)
parser.add_argument("--os", "-o", type=OS, default=OS.LINUX)
parser.add_argument("--system-type",
                    "-s",
                    type=SYSTEMTYPE,
                    default=SYSTEMTYPE.GNU)
parser.add_argument("package_name", type=str)

args = parser.parse_args()

triple = "{arch}-{os}-{systemtype}".format(arch=args.arch.value,
                                           os=args.os.value,
                                           systemtype=args.system_type.value)

log_info("{CREATEPKG}: " + triple + "-" + args.package_name)

try:
    os.mkdir(os.path.join(os.getcwd(), triple))
except Exception as e:
    pass

try:
    os.mkdir(os.path.join(os.getcwd(), triple, args.package_name))
except Exception as e:
    log_err("{CREATEPKG}: " + triple + "-" + args.package_name +
            " already exists")
    os._exit(1)

shutil.copy2(os.path.join(os.getcwd(), "templates", triple, "PKGBUILD"),
             os.path.join(os.getcwd(), triple, args.package_name))
