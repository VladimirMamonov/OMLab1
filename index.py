
import math
class Polynom:
    def __init__(self,coef):
        self.coef = coef[::-1]

    def f(self,x):
        y = 0
        for i in range(len(self.coef)):
            y += self.coef[i]*(x**i)
        return y
    def bisection(self,x0, x1, e):
        print('Метод бисекции:')
        n = 1
        condition = True
        while condition:
            x2 = (x0 + x1) / 2
            print('Итерация - %.0f xn = %.15f и f(xn) = %.15f'%(n,x2,self.f(x2)))

            if self.f(x0) * self.f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            n += 1
            condition = abs(self.f(x2)) > e

        print('Результат работы метода бисекции: ',x2,'f(x) = ',self.f(x2))

    def horda(self, x0, x1, e):
        print('Метод хорд:')
        x = lambda a, b: (a*self.f(b)-b*self.f(a)) / (self.f(b) - self.f(a))
        n = 0;
        if self.f(x0) * self.f(x(x0, x1)) <= 0:
            x1 = x(x0, x1)
        else:
            x0 = x(x0, x1)
        while (math.fabs(self.f(x(x0, x1))) > e):
            if self.f(x0) * self.f(x(x0, x1)) <= 0:
                x1 = x(x0, x1)
                print('Итерация - %.0f xn = %.15f и f(xn) = %.15f'%(n+1,x1,self.f(x1)))
                n += 1
        else:
            x0 = x(x0, x1)
        print('Результат работы метода хорд: ',x0,'f(x) = ',self.f(x0))
        n += 1
    def Df(self,xn):
        y = 0
        for i in range(len(self.coef)):
            if i>0:
                y += i*self.coef[i] * (xn ** (i-1))
        return y
    def Newton(self,x0,e):
        print('Метод Ньютона:')
        xn = x0
        for n in range(0, 1000):
            fxn = self.f(xn)
            print('Итерация - %.0f xn = %.15f и f(xn) = %.15f'%(n+1,xn,fxn))
            if abs(fxn) < e:
                print('Нашлось решение после', n+1, 'итераций. X = ',xn, 'f(x) = ', self.f(xn))
                return xn
            Dfxn = self.Df(xn)
            if Dfxn == 0:
                print('Производная равна нулю. Решений нет.')
                return None
            xn = xn - fxn / Dfxn
        print('Достигнуто максимальное количество итераций. Решения не найдено.')
        return None
polynom = Polynom([2,-2,-4,0,2,7])
# arr = input().strip().split()
polynom.Newton(-1,0.00001)
print("\n\n\n")

polynom.horda(-2,-1,0.00001)
print("\n\n\n")

polynom.bisection(-2,-1,0.00001)
