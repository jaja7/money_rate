'''
计算等额本息
'''

import math 


def transYearMonth(rateYear):
    '''
    年华利率转月利率
    '''
    return (rateYear)/12


def sameAll(base, rateT, numT):
    '''
    计算等额本息
    输入：本金、周期T的利率，还款周期
    输出：每个周期的总额
    '''
    a = base * rateT * math.pow(1+rateT, numT)
    b = math.pow(1+rateT, numT) - 1
    return a/b


def calBase(rateT, numT, huank):
    '''
    input: 周期利率、周期数、每个周期的还款
    output：等效本金
    '''
    tmp = math.pow(1+rateT, numT)
    base = huank * (tmp - 1) / tmp / rateT
    return base 

def huanKuan(base, rateYear, numYear):
    '''
    计算每个周期的还款额
    '''
    rateT = transYearMonth(rateYear)
    numT = numYear * 12
    return sameAll(base, rateT, numT)
    

if __name__ == '__main__':
    rateMon = transYearMonth(0.05)
    print(rateMon)

    # 计算每个月的按揭还款，以验证相关函数
    mon = huanKuan(700000, 0.049, 30)
    print(mon)
    
    # 通过按揭以及利率，计算本金
    base2 = calBase(0.049/12, 30*12, mon)
    print('test等效本金：', base2)


    rateY = 0.09
    base2 = calBase(rateY, 30, 1460)
    print('渤海30年等效本金：', base2)

    base2 = calBase(rateY, 30, 1580)
    print('越女推荐30年等效本金：', base2)

    base3 = calBase(rateY, 19, 2020)
    print('小雨伞19年等效本金：', base3)

    
