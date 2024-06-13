#!/usr/bin/env python
# coding=utf-8

from inc import output,run
import sys

# 控制台-参数处理和程序调用
def filereverse_console(args):
    if args.baseout:
        run.baseout(args.baseout)
    if args.hhex:
        run.hhex(args.hhex)
    if args.unhex:
        run.unhex(args.unhex)
    if args.inversion:
        run.inversion(args.inversion)
    if args.reverse:
        run.reverse(args.reverse)
    if args.reversal:
        run.reversal(args.reversal)
    if args.arrayout:
        run.arrayout(args.arrayout)
    else:
        output.usage()
        sys.exit()
