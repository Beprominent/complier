# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from Scanner import *

class Table:
    def __init__(self):
        self.type_length_dict = {'integer': 4, 'float': 4, 'char': 1}
        self.Dict = {}
        self.position = 0  #标识符在符号表中的位置
        filename = 'example.txt'
        src_filename = 'result.txt'
        Key = ['program', 'var', 'integer', 'float', 'char', 'begin', 'end']
        Symbol = [',', ':', ';', ':=', '*', '/', '+', '-', '.', '(', ')']
        self.Scan = Scanner(filename, src_filename, Key, Symbol)
        self.Scan.output_result()
        self.Scan.Strings = self.Scan.strings[::-1]
        # select集合
        # self.select = {'E': {'i': ['E1', 'T'], 'w0': ' ', 'w1': ' ', '(': ['E1', 'T'], ')': ' ', '#': ' '},
        #           'E1': {'i': ' ', 'w0': ['E1', '{w0}', 'T', 'w0'], 'w1': ' ', '(': ' ', ')': '\x00', '#': ' '},
        #           'T': {'i': ['T1', 'F'], 'w0': ' ', 'w1': ' ', '(': ['T1', 'F'], ')': ' ', '#': ' '},
        #           'T1': {'i': ' ', 'w0': '\x00', 'w1': ['T1', '{w1}', 'F', 'w1'], '(': ' ', ')': '\x00', '#': '\x00'},
        #           'F': {'i': 'i', 'w0': ' ', 'w1': ' ', '(': [')', 'E', '('], ')': ' ', '#': ' '}}
        # self.end_arrays = ['i', 'w0', 'w1', '(', ')', '#']   #终结符
        # self.start_arrays = ['E', 'E1', 'T', 'T1', 'F']   #非终结符
        # self.variable = []
        # for x in xrange(1, 100):
        #     self.variable.append('t{}'.format(x))
        # self.variable = reversed(self.variable)
        # print self.variable


    def error(self):
        print 'error!'
        sys.exit()

    def add(self, name, position, type, category):    #将标识符加入符号表中
        self.Dict[name] = {}
        self.Dict[name]['position'] = position
        self.Dict[name]['type'] = type
        self.Dict[name]['category'] = category
        if type in self.type_length_dict.keys():
            self.Dict[name]['length'] = self.type_length_dict[type]
        else:
            self.Dict[name]['length'] = ' '

    def Program(self):
        word = self.Scan.Strings.pop()
        if (self.Scan.Dict[word] == '04'):
            identify = self.Scan.Strings.pop()   #标识符
            if (self.Scan.Dict[identify] == '00'):
                self.add(identify, self.position, ' ', 'f')   #将符号名字加入符号表中
                self.position += 1
                self.Sub_program()
            else:
                self.error()
        else:
            self.error()

    def Sub_program(self):
        self.Variable()
        self.Com_sentence()

    def Variable(self):  #变量声明
        word = self.Scan.Strings.pop()
        if (self.Scan.Dict[word] == '05'):  # 标识符var
            identify = self.Scan.Strings[-1]
            if (self.Scan.Dict[identify] == '00'):  #标识符
                self.Sub_variable()
                identify = self.Scan.Strings[-1]
                while(self.Scan.Dict[identify] == '00'):
                    self.Sub_variable()
                    identify = self.Scan.Strings[-1]
            else:
                self.error()
        else:
            self.error()
        print self.Dict


    def Sub_variable(self):     #自变量声明
        self.variable_list = []
        self.variable_Dict = {}  # 记录所有定义的变量
        identify = self.Scan.Strings.pop()  # 标识符var
        # print identify
        self.variable_list.append(identify)
        comma = self.Scan.Strings[-1]
        identify = self.Scan.Strings[-2]
        while (self.Scan.Dict[comma] == '11' and self.Scan.Dict[identify] == '00'):
            self.Scan.Strings.pop()
            self.Scan.Strings.pop()
            self.variable_list.append(identify)
            # self.add()  # 将符号名字加入符号表中
            comma = self.Scan.Strings[-1]
            identify = self.Scan.Strings[-2]
        if (self.Scan.Dict[comma] == '11' and self.Scan.Dict[identify] != '00'):
            self.error()
        elif (self.Scan.Dict[comma] == '12'):
            self.Scan.Strings.pop()
        else:
            self.error()
        type = self.Scan.Strings.pop()
        if (self.Scan.Dict[type] == '06' or self.Scan.Dict[type] == '07' or self.Scan.Dict[type] == '08'):
            # self.add()  # 将符号名字的type加入符号表中
            for variable in self.variable_list:
                self.add(variable, self.position, type, 'v')
                self.position += 1
            comma = self.Scan.Strings.pop()
            if (self.Scan.Dict[comma] == '13'):
                pass
            else:
                self.error()
        else:
            self.error()
        # print self.Dict


    def Com_sentence(self):
        word = self.Scan.Strings.pop()
        if(self.Scan.Dict[word] == '09'):
            pass
        else:
            self.error()

Table().Program()
