#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output, console, run
import re, binascii, argparse, sys, time

def get_parser():
    parser = argparse.ArgumentParser(usage='python3 FileReverse-Tools.py',description='FileReverse-Tools: 基于Python3的文件反转、倒置处理框架',)
    p = parser.add_argument_group('FileReverse-Tools 的参数')
    p.add_argument("-b", "--baseout", type=str, help="读取Base64的TXT文件解密并导出为文件")
    p.add_argument("-hh", "--hhex", type=str, help="读取文件导出为16进制TXT")
    p.add_argument("-uh", "--unhex", type=str, help="读取16进制TXT导出为文件")
    p.add_argument("-i", "--inversion", type=str, help="按照双字节读取文件并倒置导出")
    p.add_argument("-r", "--reverse", type=str, help="读取文件十六进制并倒置导出")
    p.add_argument("-re", "--reversal", type=str, help="读取文件将双字节反转并导出")
    p.add_argument("-a", "--arrayout", type=str, help="读取文件导出为16进制数组TXT")
    args = parser.parse_args()
    return args

def main():
    output.logo()
    args = get_parser()
    console.filereverse_console(args)

if __name__ == '__main__':
    main()
