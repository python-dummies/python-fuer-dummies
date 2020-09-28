#!/usr/bin/env python3
"""
Variable Argumente
==================

Ein Parameter darf mit einem Sternchen anfangen, ein Parameter mit 2.
Dadurch werden variable Argumente definiert.

Ein Stern erzeugt fasst die namenlosen Argumente einer Funktion als Liste
zusammen. Zwei Sternchen stehen für ein Dictionary, indem benannte Argumente
gruppiert werden.
"""


def log(*args):
    entry = " - ".join(str(arg) for arg in args)
    print(entry)


log(200, "[OK]", "/python/docs/args-kwargs.html")
log("Server rebooted")
log(404, "[Not Found]", "/python/docs/switch-case.html")


# Demo: Args
# ----------
# Eine Funktion, die ihre positionalen Argumente ausgibt.
def dump(*args):
    print(args)


dump("a", 1, True)


# Demo: Kwargs
# ------------
# Eine Funktion, die ihre benannten Argumente ausgibt.
def dump(**kwargs):
    print(kwargs)


dump(a=1, b=False, c=None, d="yes!")


# Args und kwargs können kombiniert werden
def log(*args, **env_vars):
    entry = " - ".join(str(arg) for arg in args)
    env = ", ".join(f"{k}={v}" for k, v in env_vars.items())
    print(f"{entry} ({env})")


log(200, "[OK]", "/python/shop/mousepads.html")
log("Fatal crash", USER="root", HOST="websrv2")
