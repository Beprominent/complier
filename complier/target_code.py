# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from optimizer import *

class Target_code:
    def __init__(self):
        optimizer = Optimizer()
        optimizer.optimizer()
        self.formula = optimizer.final_formula
        #定义符号与汇编指令对应表
        self.symbol_to_letter = {'+': 'ADD',
                                 '-': 'SUB',
                                 '*': 'MUL',
                                 '/': 'DIV'}

    def generate_tmp_code(self):
        for formula in self.formula:
            #遇到一个独立的函数模块的处理
            #这里比较复杂一些，需要利用符号表
            #赋值语句
            if(formula[0] == 'program'):
                print '{} SEGMENT'.format(formula[1])
                print 'ASSUME CS:{}, DS:{}'.format(formula[1], formula[1])
            if(formula[0] == '='):
                print '\tMOV AX, {}'.format(formula[1])
                print '\tMOV {}, AX'.format(formula[3])
            #遇到+,-,*,/运算的时候的处理
            elif(formula[0] == '+' or formula[0] == '-' or formula[0] == '*' or formula[0] == '/'):
                print '\tMOV AX, {}'.format(formula[1])
                print '\t{} AX, {}'.format(self.symbol_to_letter[formula[0]], formula[2])
                print '\tMOV {}, AX'.format(formula[3])
            #遇到end时候的运算处理
            elif():
                pass
            else:
                print 'INT 21H'
                print 'RET'

    def generate_target_code(self):
        #这个函数是用来生成最终的汇编代码
        pass

target = Target_code()
target.generate_tmp_code()

