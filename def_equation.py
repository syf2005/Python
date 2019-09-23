from fractions import Fraction
import math

def quadratic(a, b, c):
    if not isinstance(a+b+c, (int, float)):
        raise TypeError('bad operand type')
    if a == 0:
        if b == 0:
            if c == 0:
                return'恒成立'
            else:
                return'无解'
        else:
            x = -c/b
            fra = x % 1
            if fra == 0:
                x = int(x)
                if x == 0:
                    return 'x=0'
                else:
                    return x
            else:
                x = Fraction(x)
                return x
    else:
        s = b*b-4*a*c
        if s >= 0:
            x1 = (-b+math.sqrt(s))/(2*a)
            x2 = (-b-math.sqrt(s))/(2*a)
            fra1 = x1 % 1
            if fra1 == 0:
                x1 = x1
            else:
                x1 = Fraction(x1)
            fra2 = x2 % 1
            if fra2 == 0:
                x2 = x2
            else:
                x2 = Fraction(x2)
            return x1, x2
        else:
            return'无解'