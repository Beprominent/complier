
from Scanner import *
import tmp


tmp_sentence=[]#temporary
tmp_exp=[]
simpleDict={}
exp_table=[]
rawSentences={}

ErrorCode={}
ErrorCode['Undefined Identifier']=66
ErrorCode['expect BEGIN']=9
ErrorCode['expect :']=12
ErrorCode['expect .']=19
ErrorCode['expect END']=10
ErrorCode['Expression Error']=77
def getRawSentence(rawStr):

    #pop and judge 'begin'
    tmpword=rawStr.pop()
    if tmpword!='begin':
        print "Fatal Error:expect a \"begin\"\n"
        exit(9)

    # pop and judge ':'
    tmpword = rawStr.pop()
    if tmpword!=':':
        print "Error:expect a \":\" after  \"begin\"\n"
        exit(12)

    if rawStr[0]!='.':
        print "Error:expect a \".\" after  \"end\"\n"
        exit(19)
    else:
        del rawStr[0]
    if rawStr[0]!='end':
        print "Fatal Error:expect a \"end\"\n"
        exit(10)
    else:
        del rawStr[0]
        return rawStr
    return None
def getSingleSentence(rawSs):
    tmplist=[]
    tmpS=[]
    while rawSs:
        tmpword=rawSs.pop()
        if tmpword ==';':
            tmplist.append(tmpS)
            tmpS=[]
            continue
        if (tmpword not in t.Dict.keys())&(t.Scan.Dict[tmpword]=='00'):
            print "Error:Undefined Identifier \"",tmpword,"\"\n"
            exit(ErrorCode['Undefined Identifier'])
        tmpS.append(tmpword)
    # print "tmplist is",tmplist[0],"\nEND"
    return tmplist
def getExpression(tmpS):
    if len(tmpS)>2:
        tmphead=tmpS[0]
        del tmpS[0]
        del tmpS[0]
        tmpS.append('#')
        return tmpS, tmphead
    else:
        print "Error:Expression Error\n"
        exit(ErrorCode['Expression Error'])
def getSimpleDict(tmp1):
    simple_dict={}
    for i in tmp1:
        if not t.Scan.Dict.has_key(i):
            continue
        if t.Scan.Dict[i]=='00':
            simple_dict[i]=1
        elif t.Scan.Dict[i]=='03':
            simple_dict[i] = 2
        else:
            simple_dict[i] = 3
    return simple_dict
def getQuaternion(exp):
    quat=tmp.syntax()
    result=[]
    for cnter in range(len(exp)):
        exptmp,exphead=getExpression(exp[cnter])
        result+=quat.SyntaxAnalysis(exptmp,exphead,getSimpleDict(exp[cnter]))
    for cnter in range(len(result)):
        print result[cnter]
    return result
def getQuaternions():

    # q=quaternion.quaternion()

    t.Program()
    # t.Scan.Strings.pop()
    print t.Scan.Strings
    rawSentences = getRawSentence(t.Scan.Strings)
    SentenceList = getSingleSentence(rawSentences)
    quaternions=getQuaternion(SentenceList)
    return quaternions
    pass
# if __name__ == '__main__':
#     getQuaternions()

