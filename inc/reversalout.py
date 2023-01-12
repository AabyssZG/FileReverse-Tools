#!/usr/bin/env python
# coding=utf-8

from inc import run
import argparse, sys, time, re, binascii

def split_str(string,length):
    """
    按照指定长度分割输入字符串，并以列表形式返回
    :param string: 待分割字符串
    :param length: 指定分割长度
    :return: 分割后的字符串列表
    """
    str_lst = re.findall(r'.{'+str(length)+ '}',string)
    str_lst.append(string[(len(str_lst) * length):])
    return str_lst

def reverse_lst(string_lst):
    """
    将列表中的字符串反转
    :param string_lst: 字符串列表
    :return: 反转后的字符串列表
    """
    reverse_str_lst = []
    for each in string_lst:
        reverse_str_lst.append(each[::-1])
    return reverse_str_lst

def gogogo(filename):
    """主程序"""
    # 指定分割长度
    SPLIT_LEN = 2
    # 指定要求字符串字符串长度，长度不足要求以F末尾填充
    #FIX_STRLEN = 99999999999999999999
    # 获取文件内容，以列表形式保存。文件内容格式为每行为188123456789723格式字符串
    fr = open('hex.txt', 'r')
    record_lst = fr.readlines()
    fr.close()

    reverse_record = ''
    reverse_record_lst = []
    for each_line in record_lst:
        each_line = each_line.strip()
        #len_telno = len(each_line)
        #if len_telno < FIX_STRLEN:
            #each_line = each_line + (FIX_STRLEN - len_telno) * 'F'
        reverse_record = ''.join(reverse_lst(split_str(each_line, SPLIT_LEN)))
        reverse_record_lst.append(reverse_record )

    fw = open('reversal.txt', 'w')
    fw.writelines(reverse_record_lst)
    fw.close()
    run.reversalput(filename)