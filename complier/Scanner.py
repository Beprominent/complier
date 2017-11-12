# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
class Scanner:
    def __init__(self, filename, src_filename, Key, Symbol):
        self.filename = filename
        self.src_filename = src_filename
        self.Key = Key
        self.Symbol = Symbol
        self.KT = []
        self.temp_KT = []
        self.PT = []
        self.temp_PT = []
        self.iT = []
        self.temp_iT = []
        self.cT = []
        self.temp_cT = []
        self.ST = []
        self.temp_ST = []
        self.CT = []
        self.temp_CT = []
        self.Dict = {}
        self.sentences = []
        self.strings = []
        self.calcu = ['+', '-', '*', '/']

    def error(self):
        print 'error!'
        sys.exit()

    def read(self):
        file = open(self.filename)
        for line in file:
            strs = str(line)
            for word in strs:
                # print word
                self.sentences.append(word)
        self.length = len(self.sentences)
        i = 0
        while i <= self.length - 1:
            new_word = []
            newword = []
            # frist step: judge whether it's a key word
            if ((self.sentences[i] >= 'a' and self.sentences[i] <= 'z') or (self.sentences[i] >= 'A' and self.sentences[i] <= 'Z')):
                new_word.append(self.sentences[i])
                i += 1
                while ((self.sentences[i] >= 'a' and self.sentences[i] <= 'z') | (self.sentences[i] >= 'A' and self.sentences[i] <= 'Z')):
                    new_word.append(self.sentences[i])
                    i += 1
                newword = ''.join(new_word)
                if newword in self.Key:
                    self.temp_KT.append(newword)
                else:
                    self.temp_iT.append(newword)
            # third step to judge whether it's a sign
            elif (str(self.sentences[i]) == str('\'')):
                i += 2
                if (self.sentences[i] == '\''):
                    new_word.append(self.sentences[i - 1])
                    newword = ''.join(new_word)
                    self.temp_cT.append(newword)
                    i += 1
                else:
                    print 'It\'s wrong defination'
                    exit()
            # firth step to judge whether it's a string
            elif (self.sentences[i] == '"'):
                i += 1
                while (self.sentences[i] != '"'):
                    new_word.append(self.sentences[i])
                    i += 1
                i += 1
                newword = ''.join(new_word)
                self.temp_ST.append(newword)
            # fifth step to judge whether it's a symbol
            elif (self.sentences[i] in self.Symbol):
                symbol = []
                temp = []
                symbol.append(self.sentences[i])
                temp.append(self.sentences[i])
                i += 1
                if (i <= self.length -2):
                    temp.append(self.sentences[i])
                if (''.join(temp) in self.Symbol):
                    symbol = temp
                    i += 1
                newword = ''.join(symbol)
                self.temp_PT.append(newword)
            elif ((self.sentences[i] >= '1') and (self.sentences[i] <= '9')):  # 判断首字母是否是数字
                new_word.append(self.sentences[i])
                i += 1
                while ((self.sentences[i] >= '0') and (self.sentences[i] <= '9')):  # 持续判断下一个输入是否为数字
                    new_word.append(self.sentences[i])
                    i += 1
                if (self.sentences[i] == '.'):  # 判断下一个字符是不是小数点
                    new_word.append(self.sentences[i])
                    i += 1
                    if ((self.sentences[i] >= '1') and (self.sentences[i] <= '9')):  # 小数点后的输入是否为数字
                        new_word.append(self.sentences[i])
                        i += 1
                        while ((self.sentences[i] >= '1') and (
                            self.sentences[i] <= '9')):  # 持续判断下一个输入是否为数字
                            new_word.append(self.sentences[i])
                            i += 1
                        if (self.sentences[i] == 'e'):  # 判断下一个输入是否为e
                            new_word.append(self.sentences[i])
                            i += 1
                            if ((self.sentences[i] >= '1') and (self.sentences[i] <= '9')):  # 判断下一个输入是否为数字
                                new_word.append(self.sentences[i])
                                i += 1
                                while ((self.sentences[i] >= '0') and (self.sentences[i] <= '9')):  # 持续判断有没有数字继续输入
                                    new_word.append(self.sentences[i])
                                    i += 1
                                self.judge_false(i)
                            elif ((self.sentences[i] == '-') or (self.sentences[i] == '+')):  # 判断尾数正负
                                new_word.append(self.sentences[i])
                                i += 1
                                if ((self.sentences[i] >= '1') and (self.sentences[i] <= '9')):  # 判断接下来输入的是否为数字
                                    new_word.append(self.sentences[i])
                                    i += 1
                                    while ((self.sentences[i] >= '0') and (self.sentences[i] <= '9')):  # 持续判断后续输入是否是数字
                                        new_word.append(self.sentences[i])
                                        i += 1
                                    self.judge_false(i)
                                else:
                                    self.error()
                            self.judge_false(i)
                        self.judge_false(i)
                    else:  # 小数点后不是数字就报错
                        self.error()
                elif (self.sentences[i] == 'e'):
                    new_word.append(self.sentences[i])
                    i += 1
                    if ((self.sentences[i] >= '1') and (self.sentences[i] <= '9')):
                        new_word.append(self.sentences[i])
                        i += 1
                        while ((self.sentences[i] >= '0') and (self.sentences[i] <= '9')):
                            new_word.append(self.sentences[i])
                            i += 1
                        self.judge_false(i)
                    elif ((self.sentences[i] == '-') or (self.sentences[i] == '+')):
                        new_word.append(self.sentences[i])
                        i += 1
                        if ((self.sentences[i] >= '1') and (self.sentences[i] <= '9')):
                            new_word.append(self.sentences[i])
                            i += 1
                            while ((self.sentences[i] >= '0') and (self.sentences[i] <= '9')):
                                new_word.append(self.sentences[i])
                                i += 1
                                self.judge_false(i)
                        else:
                            self.error()
                    self.judge_false(i)
                self.judge_false(i)
                newword = ''.join(new_word)
                self.temp_CT.append(newword)
            else:
                i += 1
            self.strings.append(newword)

    def judge_false(self, i):
        if ((self.sentences[i] >= 'a' and self.sentences[i] <= 'd') or (
                self.sentences[i] >= 'A' and self.sentences[i] <= 'D')):
            self.error()  # 下一个输入为字母
        if ((self.sentences[i] >= 'f' and self.sentences[i] <= 'z') or (
                self.sentences[i] >= 'F' and self.sentences[i] <= 'Z')):
            self.error()  # 下一个输入为字母
        if ((self.sentences[i] in self.calcu) and not (
            ((self.sentences[i + 1] >= '0') and (self.sentences[i + 1] <= '9')) or self.sentences[i + 1] in self.iT)):
            self.error()  # 运算符后面不是数字或者变量标识符
        pass

    def delete_duplication(self, array):
        template = []
        for element in array:
            if element in template:
                del element
            else:
                template.append(element)
        return template

    def output_result(self):
        self.read()
        self.KT = self.delete_duplication(self.temp_KT)
        self.iT = self.delete_duplication(self.temp_iT)
        self.cT = self.delete_duplication(self.temp_cT)
        self.ST = self.delete_duplication(self.temp_ST)
        self.PT = self.delete_duplication(self.temp_PT)
        self.CT = self.delete_duplication(self.temp_CT)
        self.strings = filter(lambda x: x != [], self.strings)
        for x in self.iT:
            self.Dict[x] = '{:02d}'.format(00)
        for x in self.cT:
            self.Dict[x] = '{:02d}'.format(01)
        for x in self.ST:
            self.Dict[x] = '{:02d}'.format(02)
        for x in self.CT:
            self.Dict[x] = '{:02d}'.format(03)
        for x in self.KT:
            self.Dict[x] = '{:02d}'.format(self.Key.index(x) + 4)
        for x in self.PT:
            self.Dict[x] = '{:02d}'.format(self.Symbol.index(x) + 11)
        if os.path.exists(self.src_filename):
            os.remove(self.src_filename)
        with open(self.src_filename, 'a') as f:
            for string in self.strings:
                line = string + '--------' + '<{}>\n'.format(self.Dict[string])
                f.write(line)
        f.close()



