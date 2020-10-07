import math
import sys
import os
from fractions import Fraction as fr
from random import randint
from random import uniform as uf#返回一个随机浮点数 N
space = '  '
def expression():#随机生成表达式
    symbol = ['+', '-', '*', '/']
    brackets = ['(', '', ')']
    # 随机产生计算符
    s1 = randint(0, 2)
    s2 = randint(0, 3)
    s3 = randint(0, 3)
    #随机产生括号bt表示左括号，br表示右括号
    bt1 = randint(0, 1)
    bt2 = randint(0, 1)
    bt3 = randint(0, 1)
    br1 = randint(1, 2)
    br2 = randint(1, 2)
    br3 = randint(1, 2)
    if bt1 == 0:
        bt2 = 1
        bt3 = 1
        if br1 == 2:
            br2 = 1
            br3 = 1
        else:
            br2 = 2
            br3 = 1
    else:
        if bt2 == 0:
            bt3 = 1
            br1 = 1
            if (br2 == 2):
                br3 = 1
            else:
                br3 = 2
        else:
            bt3 = 0
            br1 = 1
            br2 = 1
            br3 = 2
    num1 = uf(0, 1)
    # 对随机产生的分子分母做最大限制
    num1 = fr(num1).limit_denominator(10)
    num2 = uf(0, 1)
    num2 = fr(num2).limit_denominator(10)
    num3 = randint(1, 10)
    num4 = randint(1, 10)
    # 产生随机表达式
    ran_exp = brackets[bt1] + str(num1) + symbol[s1] + brackets[bt2] + str(num2) + brackets[br1] + \
              symbol[s2] + brackets[bt3] + str(num3) + brackets[br2] + symbol[s3] + str(num4) + brackets[br3]
    ran_exp = str(ran_exp)
    return ran_exp

def answer(eq):#利用eval算出表达式答案
    aws= fr(eval(eq)).limit_denominator(1000)#eval()函数用来执行一个字符串表达式，并返回表达式的值,limit_denominator求近似值
    answer = str(aws)
    return (answer)

def dict_split(str1):#将分子和分母分别存储到不同的两个字典中输出约分
    d1 = {}
    d2 = {}
    count1 = 0
    count2 = 0
    pred = 1
    sign = 0
    for s in str1:
        if s == '-':
            sign = s
            continue
        if s == '/':
            pred = 0
            continue
        if pred == 1:
            d1[count1] = s
            count1 = count1 + 1
        else:
            d2[count2] = s
            count2 = count2 + 1
    numerator = take_integer(d1)
    # 分母
    denominator = take_integer(d2)
    answer1 = -10000
    if denominator == 0:
        return numerator
    else:
        we1 = numerator // denominator
        we2 = numerator % denominator
        if sign == '-':    #判断结果是否为负
            if we1 == 0:
                answer1 = sign + str(we2) +'/' + str(denominator)
                return answer1
            else:
                answer1 = sign + str(we1) + ' ' + str(we2) + '/' + str(denominator)
                return answer1
        else:
            if we1 == 0:
                answer1 = str(we2) + '/' + str(denominator)
                return answer1
            else:
                answer1 = str(we1) + ' ' + str(we2) + '/' + str(denominator)
                return answer1

def take_integer(dicts={}):#将字典存储的数还原为十进制数
    a1 = dicts
    j = len(a1) - 1
    sum1 = 0
    for ss in range(0, len(a1)):
        if j < 0:
            break
        sum1 = int(a1[j]) * int(math.pow(10, ss)) + sum1
        j = j - 1
    return sum1

def fixed(): #固定20道题目
    right = 0
    for j in range(20):
        exp = expression()
        print(exp,"=")
        in_answ = input("?")
        re_answ = answer(exp)
        if in_answ == re_answ:
           print("答对了你真是一个天才")
           right = right +1
        else:
            print("你答案错了，再算一算吧，答案是", end= ' ')
            print(dict_split(re_answ))
    print("一共20道题，你一共答正确了", right, "道题")

def deft_input(num):#指定输入多少个题目
    right = 0
    data = open("data.txt",'w+')
    if str.isdigit(str(num)):
        num1 = int(num)
        for i in range(num1):
            exp = expression()
            exp1 = exp + '='
            re_answ = answer(exp)
            print('{:<50}{:<25}'.format(exp1, dict_split(re_answ)))
            print('{:<50}{:<25}'.format(exp1, dict_split(re_answ)), file=data)
    else:
        print("题目数量必须是 正整数。")
if __name__ == "__main__":
    import argparse  #argparse是一个{命令行参数解析}模块
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cin")
    args = parser.parse_args()
    if args.cin == None:
        fixed()
    else:
        deft_input(args.cin)






