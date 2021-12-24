# -*- encoding: utf-8 -*-
'''
Copyright (c) 2021 - ElVirtualJefe
'''

from re import match
from app import scanAgent
import sys

if len(sys.argv) > 1:
    for i,arg in enumerate(sys.argv):
        if i == 0:
            continue
        match arg:
            case "--discovery":
                pass
            case "--scan":
                scanAgent()
            case _:
                print(f"No such option found: {arg}")

#scanAgent()

