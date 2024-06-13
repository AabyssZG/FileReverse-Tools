#!/usr/bin/env python
# coding=utf-8

import random, time, os, sys

def logo():
    logo0 = r'''
+-----------------------------------------------------------------------------+
+                                                                             +
+  ______ _ _      _____                                  _______          _  +
+ |  ____(_) |    |  __ \                                |__   __|        | | +
+ | |__   _| | ___| |__) |_____   _____ _ __ ___  ___ ______| | ___   ___ | | +
+ |  __| | | |/ _ \  _  // _ \ \ / / _ \ '__/ __|/ _ \______| |/ _ \ / _ \| | +
+ | |    | | |  __/ | \ \  __/\ V /  __/ |  \__ \  __/      | | (_) | (_) | | +
+ |_|    |_|_|\___|_|  \_\___| \_/ \___|_|  |___/\___|      |_|\___/ \___/|_| +
+                                                                             +
+                                                                             +
+                               Version: 1.03                                 +
+                         Author:  曾哥（@AabyssZG）                          +
+              Whoami:  https://github.com/AabyssZG/FileReverse-Tools         +
+-----------------------------------------------------------------------------+
'''
    print(logo0)

def usage():
    print('''
用法:
        读取Base64的TXT文件解密并导出为文件:   python3 FileReverse-Tools.py -b base64.txt
        读取文件导出为十六进制TXT:        python3 FileReverse-Tools.py -hh bin 
        读取十六进制TXT导出为文件:        python3 FileReverse-Tools.py -uh hex.txt
        按照双字节读取文件并倒置导出:       python3 FileReverse-Tools.py -i bin
        读取文件十六进制并倒置导出:    python3 FileReverse-Tools.py -r bin
        读取文件将双字节反转并导出:    python3 FileReverse-Tools.py -re bin
参数:
        -b  --baseout   读取Base64的TXT文件解密并导出为文件
        -hh --hhex      读取文件导出为16进制TXT  
        -uh --unhex     读取16进制TXT导出为文件
        -i  --inversion 按照双字节读取文件并倒置导出
        -r  --reverse   读取文件十六进制并倒置导出
        -re --reversal  读取文件将双字节反转并导出
        ''', end='')
