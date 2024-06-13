#!/usr/bin/env python
# coding=utf-8

from inc import output,console,reversalout
import argparse, sys, time, re, binascii, os

def baseout(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    if(len(content)%3 == 1):
        content += b'=='
    elif(len(content)%3 == 2):
        content += b'='
    f2 = open("baseout.bin", "wb+")
    f2.write(binascii.a2b_base64(content))
    f2.close()
    print(f"[+] 读取Base64加密的{filename}文件解密并导出成功:导出为baseout.bin")
    sys.exit()

def hhex(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("hex.txt", "wb+")
    f2.write(binascii.hexlify(content))
    f2.close()
    print(f"[+] 将{filename}文件转换为16进制TXT成功:导出为hex.txt")
    sys.exit()

def unhex(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        if len(content) % 2 != 0:
            content = content + b'e'
    f2 = open("unhex.bin", "wb+")
    f2.write(binascii.unhexlify(content))
    f2.close()
    print(f"[+] 读取十六进制{filename}文件导出为文件成功:导出为unhex.bin")
    sys.exit()

def inversion(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("inversion.bin", "wb+")
    payload = binascii.hexlify(content[::-1])
    f2.write(binascii.unhexlify(payload))
    f2.close()
    print(f"[+] 按照双字节读取{filename}文件并倒置导出成功:导出为inversion.bin")
    sys.exit()

def reverse(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("reverse.bin", "wb+")
    payload = binascii.hexlify(content)
    f2.write(binascii.unhexlify(payload[::-1]))
    f2.close()
    print(f"[+] 将{filename}转换为十六进制倒置并导出成功:导出为reverse.bin")
    sys.exit()

def reversal(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("hex.txt", "wb+")
    f2.write(binascii.hexlify(content))
    f2.close()
    reversalout.gogogo(filename)

def reversalput(filename):
    with open('reversal.txt', 'rb') as f:
        content = f.read()
    f2 = open("reversal.bin", "wb+")
    f2.write(binascii.unhexlify(content))
    f2.close()
    print(f"[+] 读取{filename}文件将双字节反转并导出成功:导出为reversal.bin")
    sys.exit()

def arrayout(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    f2 = open("hex.txt", "wb+")
    f2.write(binascii.hexlify(content))
    f2.close()
    print(f"[+] 将{filename}文件转换为16进制TXT成功:导出为hex.txt")
    with open('hex.txt', 'r') as input_file:
        content = input_file.read()
    result = ',0x'.join([content[i:i+2] for i in range(0, len(content), 2)])
    result = '0x' + result
    with open('arrayout.txt', 'w') as output_file:
        output_file.write(result)
    print(f"[+] 将{filename}文件转换为16进制数组TXT成功:导出为arrayout.txt")
    sys.exit()
