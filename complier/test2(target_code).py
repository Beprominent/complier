# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Target_code:
    def __init__(self):
        self.formula = [('*', 'a', 'b', 't1'),
                        ('/', 'c', 'd', 't2'),
                        ('+', 't1', 't2', 't3'),
                        (':=', 't3', ' ', 'e')]
        #定义符号与汇编指令对应表
        self.symbol_to_letter = {'+': 'ADD',
                                 '-': 'SUB',
                                 '*': 'MUL',
                                 '/': 'DIV'}
        self.acc = []  #记录寄存器的名字

    def generate_tmp_code(self):
        self.acc.append('0')
        for formula in self.formula:
            #遇到一个独立的函数模块的处理
            #这里比较复杂一些，需要利用符号表
            if(formula[0] == 'program'):
                print '{} SEGMENT'.format(formula[1])
                print 'ASSUME CS:{}, DS:{}'.format(formula[1], formula[1])
            # 赋值语句
            if(formula[0] == ':='):
               if(self.acc[self.formula.index(formula)] == '0'):
                   print 'MOV   AX, {}'.format(formula[1])
                   print 'MOV   {}, AX'.format(formula[3])
               else:
                   print 'MOV   {}, AX'.format(formula[3])
            if(formula[0] == '')

    def generate_target_code(self):
        #这个函数是用来生成最终的汇编代码
        pass

target = Target_code()
target.generate_tmp_code()