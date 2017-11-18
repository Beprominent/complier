# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from generate_table import *
from Scanner import *

class Optimizer:
    def __init__(self):
        table = Table()
        print table.Scan.Strings
        self.formula = table.formula
        self.final_formula = []    #最终的四元式
        self.variable = []
        for x in xrange(1, 100):
            self.variable.append('t{}'.format(x))

    def optimizer(self):
        tmp_formula = []  #临时四元式组
        for formula in self.formula:
            tmp_formula.append([formula[0], formula[1], formula[2], formula[3], {formula[3]: [formula[3]]}])
        for formula in tmp_formula:
            # 出现等号的时候,删除重复的赋值
            if (formula[0] == '='):
                formula[4][formula[3]].append(formula[1])
                for new_formula in self.final_formula:
                    if (formula[3] == new_formula[3]):
                        position1 = self.final_formula.index(new_formula)
                        del self.final_formula[position1]
            self.replace(self.final_formula)
            #先换中间变量的名字
            # new_formula[4].values()是一个list,list里只有一个list数组
            for new_formula in self.final_formula:
                if formula[1] in new_formula[4].values()[0]:
                    formula[1] = new_formula[4].values()[0][0]
                if formula[2] in new_formula[4].values()[0]:
                    formula[2] = new_formula[4].values()[0][0]
            # self.final_formula.append([formula[0], formula[1], formula[2], formula[3], formula[4]])
            self.delete_repeat_formula(formula)
            # self.replace(final_formula)
            #符号两边都是常数
            if(formula[1] in self.Scan.Strings and formula[2] in self.Scan.Strings):
                if(self.Scan.Dict[formula[1]] == '03' and self.Scan.Dict[formula[2]] == '03'):
                    formula[4][formula[3]].append(str(eval(formula[1] + formula[0] + formula[2])))
        tmp_formula = self.final_formula
        self.final_formula = []
        #将formula转化成四维
        for formula in tmp_formula:
            self.final_formula.append([formula[0], formula[1], formula[2], formula[3]])
        self.generate_final_formula()

    def replace(self, formulas):
        for formula in formulas:
            formula[4][formula[3]] = sorted(formula[4][formula[3]])
            for value in formula[4][formula[3]]:
                # 常数
                if (value in self.Scan.Strings and self.Scan.Dict[value] == '03'):
                    position = formula[4][formula[3]].index(value)
                    formula[4][formula[3]][0], formula[4][formula[3]][position] = formula[4][formula[3]][position], formula[4][formula[3]][0]
                    break
                # 变量
                elif (value in self.Scan.Strings and self.Scan.Dict[value] == '00'):
                    position = formula[4][formula[3]].index(value)
                    formula[4][formula[3]][0], formula[4][formula[3]][position] = formula[4][formula[3]][position], formula[4][formula[3]][0]
                    break
                else:
                    pass

    def delete_repeat_formula(self, new_formula):  #删除重复的四元式
        record = False
        strings = []
        strings.append(new_formula[1])
        strings.append(new_formula[2])
        for formula in self.final_formula:
            new_strings1 = []
            new_strings2 = []
            new_strings1.append(formula[1])
            new_strings1.append(formula[2])
            new_strings2.append(formula[2])
            new_strings2.append(formula[1])
            if(formula[0] == '-' or formula[0] == '/'):
                if(strings == new_strings1 and new_formula[0] == formula[0]):
                    record = True
                    formula[4][formula[3]].append(new_formula[3])
            if(formula[0] == '+' or formula[0] == '*'):
                if((strings == new_strings1 or strings == new_strings2) and new_formula[0] == formula[0]):
                    record = True
                    formula[4][formula[3]].append(new_formula[3])
        if(record == False):
            self.final_formula.append([new_formula[0], new_formula[1], new_formula[2], new_formula[3], new_formula[4]])

    def generate_final_formula(self):
        #删除没有作用的临时变量
        for formula in self.final_formula:
            if(formula[1] in self.Scan.Strings and formula[2] in self.Scan.Strings):
                if(self.Scan.Dict[formula[1]] == '03' and self.Scan.Dict[formula[2]] == '03' and formula[3] in self.variable):
                    del self.final_formula[self.final_formula.index(formula)]
        #删除临时变量与变量之间的赋值
        tmp_formula = self.final_formula
        self.final_formula = []
        for formula in tmp_formula:
            if(formula[0] == '=' and formula[1] in self.variable):
                for new_formula in self.final_formula:
                    for element in new_formula:
                        if(new_formula[new_formula.index(element)] == formula[1]):
                            new_formula[new_formula.index(element)] = formula[3]
            else:
                self.final_formula.append([formula[0], formula[1], formula[2], formula[3]])
        print self.final_formula

optimizer = Optimizer()
optimizer.optimizer()