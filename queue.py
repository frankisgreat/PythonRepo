#!/usr/bin/env python
#-*- encoding: utf-8 -*-
"""
@File    :   Queue.py
@Version :   1.0.0
@Author  :   oldLuckyKing
@License :   (C) Copyright 2006-2019
@Software:   vsCode
@Time    :   2019/9/26
@Desc    :
"""
import sys

a = 0
b = 0
c = 0
list_A = [] # 1人就餐
list_B = [] # 2人就餐
list_C = [] # 4人就餐

pos_dict = {"一人座位": list_A,
            "二人座位": list_B,
            "四人座位": list_C}


def append_queue():
    """
    排队系统
    :return:
    """
    global a, b, c
    while True:
        choice = int(input("请选择业务类型：1.一人座位 2.二人座位 3.四人座位 4.退出 \n"))

        if choice == 1:
            a += 1
            A_num = "A" + str(a)
            list_A.append(A_num)
            pos_dict["一人座位"] = list_A
            print ("你的排队号码是A%d,当前你选择的是一人座位。\n" % a)
            return
        elif choice == 2:
            b += 1
            B_num = "B" + str(b)
            list_B.append(B_num)
            pos_dict["二人座位"] = list_B
            print ("你的排队号码是B%d,当前你选择的是二人座位。\n" % b)
            return 
        elif choice == 3:
            c += 1
            C_num = "C" + str(c)
            list_C.append(C_num)
            pos_dict["四人座位"] = list_C
            print ("你的排队号码是C%d,当前你选择的是四人座位。\n" % c)
        else:
            return


def pop_queue():
    """
    叫号系统   
    :return:
    """

    while True:
        choice = int(input('请输入当前座位类型：1.一人座位 2.二人座位 3.四人座位 4.退出 \n'))

        if choice == 1:
            if len(list_A) == 0:
                print ("目前一人就餐座位空闲，无人排队")
            else:
                pop_num = list_A.pop(0)
                print ("请%s号客人前往一人就餐座位就餐，当前排队人数为%d人\n" % (pop_num, len(list_A)))

        elif choice == 2:
            if len(list_B) == 0:
                print ("目座位二人座位空闲，无人排队")
            else:
                pop_num = list_B.pop(0)
                print ("请%s号客人前二人座位就餐，当前排队人数为%d人\n" % (pop_num, len(list_B)))

        elif choice == 3:
            if len(list_C) == 0:
                print ("目前四人座位空闲，无人排队")
            else:
                pop_num = list_C.pop(0)
                print ("请%s号客人前往四人座位就餐，当前排队人数为%d人\n" % (pop_num, len(list_C)))
        else:
            return


if __name__ == '__main__':
    """
    主程序
    """
    while True:
        choice = int(input('请选择您需求：1.取号 2.叫号 3.退出 \n'))

        if choice == 1:
            append_queue()
        elif choice == 2:
            pop_queue()
        else:
            break