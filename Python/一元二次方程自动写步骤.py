#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#变量shortx1和shortx2为多余臃肿变量，待优化！

from fractions import Fraction
import math
from def_equation import quadratic

print('欢迎进入一元二次方程求解程序')
print('''-----------------------------------------
此简易一元二次方程求解器最后更新于2019/4/26
1.对可用因式分解法的方程另附有因式分解法步骤
2.优化代码结构
软件作者：苏耀峰
-----------------------------------------''')
print('在进行计算前，请确认方程已经化为一般形式')
n = 1

t = 1
while t != 0:
    t = input('是否需要显示计算过程？（T/F)')
    if t == 'F' or t == 'f':
        n = 1
        while n != 0:
            print('---第%s个方程---' % n)
            a1 = float(input('请输入二次项系数：'))
            b2 = float(input('请输入一次项系数：'))
            c3 = float(input('请输入常数项：'))
            if b2 < 0 and c3 < 0:
                print('方程%sx²%sx%s=0的解为：' % (a1, b2, c3))
            elif c3 < 0:
                print('方程%sx²+%sx%s=0的解为：' % (a1, b2, c3))
            elif b2 < 0:
                print('方程%sx²%sx+%s=0的解为：' % (a1, b2, c3))
            else:
                print('方程%sx²+%sx+%s=0的解为：' % (a1, b2, c3))
            print(quadratic(a1, b2, c3))
            n = n + 1
        break
    elif t == 'T' or t == 't':#此处开始显示步骤
        print('---默认使用公式法，如可用因式分解法将另附步骤')
        n = 1
        while n != 0:
            print('---第%s个方程---' % n)
            a1 = float(input('请输入二次项系数：'))
            b2 = float(input('请输入一次项系数：'))
            c3 = float(input('请输入常数项：'))
            if a1 != 0:
                if b2 < 0 and c3 < 0:
                    print('%sx²%sx%s=0' % (a1, b2, c3))
                elif c3 < 0:
                    print('%sx²+%sx%s=0' % (a1, b2, c3))
                elif b2 < 0:
                    print('%sx²%sx+%s=0：' % (a1, b2, c3))
                else:
                    print('%sx²+%sx+%s=0：' % (a1, b2, c3))
                delta = b2 * b2 - 4 * a1 * c3
                doubleA = 2 * a1
                print('△ =b²-4ac\n   =%s' % delta)#以上为计算根的判别式
                if delta > 0:#以下是有两个不等根的计算步骤——4/26开始增加因式分解法，未完成，待调试
                    x1 = (-(b2)+math.sqrt(delta))/(2 * a1)
                    x2 = (-(b2)-math.sqrt(delta))/(2 * a1)
                    fra1 = x1 % 1
                    fra2 = x2 % 1
                    if fra1 == 0 and fra2 == 0:
                        x1 = int(x1)
                        x2 = int(x2)
                        print('''x=[-b±√(b²-4ac)]/(2a)
x=[-(%s)±√%s]/%s
x1=%s,x2=%s''' % (b2,delta,doubleA,x1,x2))
                        print('\n此方程可用更简单的因式分解法：')
                        if x1 < 0 and x2 < 0:
                            shortx1 = -x1
                            shortx2 = -x2
                            print('(x+%s)(x+%s)=0' % (shortx1, shortx2))
                        elif x1 > 0 and x2 > 0:
                            print('(x-%s)(x-%s)=0' % (x1, x2))
                        elif x1 < 0 and x2 > 0:
                            shortx1 = -x1
                            print('(x+%s)(x-%s)=0' % (shortx1, x2))
                        elif x1 > 0 and x2 < 0:
                            shortx2 = -x2
                            print('(x-%s)(x+%s)=0' % (x1, shortx2))
                        elif x1 == 0 and x2 > 0:
                            print('x(x-%s)=0' % x2)#此处暂未重构完成
                        elif x1 == 0 and x2 < 0:
                            shortx2 = -x2
                            print('x(x+%s)=0' % shortx2)
                        elif x2 == 0 and x1 > 0:
                            print('x(x-%s)=0' % x1)
                        elif x2 == 0 and x1 < 0:
                            print('x(x%s)=0' % x1)
                        else:
                            print('如发现此提示请联系开发者：vip@syf.ink')
                        print('x1=%s,x2=%s\n' % (x1, x2))
                    else:
                        if fra1 == 0:
                            x1 = x1
                        else:
                            x1 = Fraction(x1)
                        if fra2 == 0:
                            x2 = x2
                        else:
                            x2 = Fraction(x2)
                        print('''x=[-b±√(b²-4ac)]/(2a)
x=[-(%s)±√%s]/%s
x1=%s,x2=%s''' % (b2,delta,doubleA,x1,x2))#以上是有两个不等根的计算步骤
                elif delta == 0:#以下是有两个等根的计算步骤
                    x1 = (-(b2)+math.sqrt(delta))/(2 * a1)
                    fra1 = x1 % 1
                    if fra1 == 0:
                        x1 = int(x1)
                        print('''x=[-b±√(b²-4ac)]/(2a)
x=[-(%s)±√%s]/%s
x1=x2=%s''' % (b2,delta,doubleA,x1))
                        print('\n此方程可用更简单的因式分解法：')
                        if x1 < 0:
                            shortx1 = -x1
                            print('(x+%s)²=0' % shortx1)
                        elif x1 > 0:
                            print('(x-%s)²=0' % x1)
                        else:
                            print('x²=0')
                        print('x1=x2=%s\n' % x1)
                    else:
                        if fra1 == 0:
                            x1 = x1
                        else:
                            x1 = Fraction(x1)
                        print('''x=[-b±√(b²-4ac)]/(2a)
x=[-(%s)±√%s]/%s
x1=x2=%s''' % (b2,delta,doubleA,x1))#以上是有两个等根的计算步骤
                else:#以下是无根的显示结果
                    print('∵△ <0\n∴此方程无实数根')
                n = n + 1
            else:#此处为一元一次特殊情况
                x = -(c3)/b2
                fra = x % 1
                if fra == 0:
                    x = int(x)
                    if x == 0:
                        print('x=0')
                    else:
                        print('x=%s' % x)
                else:
                    x = Fraction(x)
                    print('x=%s' % x)
                n = n + 1
    else:
         t = 1

