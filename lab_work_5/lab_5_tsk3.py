"""
Вычислить суммы
"""
import math as m

def make_x(a,b,h) -> list:
    res=[a]
    while a+h<=b:
        a=a+h
        res.append(a)
    return res

def sum(s_1,s_2,a,b,h, k=0):
    for x in make_x(a,b,h):
        i=1
        s=0
        while (abs(s_1(x, i))>=0.0001):
            s+=s_1(x,i)
            i+=1
        print(s+k, s_2(x))

def form_1(x,i):
    return m.cos(i*x)/m.factorial(i)

def form_1_test(x):
    return (m.e**m.cos(x))*m.cos(m.sin(x))

def form_2(x, i):
    return (((-1)**i)*m.cos(i*x))/i**2

def form_2_test(x):
    return (x**2-(m.pi**2)/3)/4


print("Значение для первой функции >>")
sum(form_1, form_1_test, 0.1, 1, 0.1, 1)
print()
print("Значение для второй функции >>")
sum(form_2, form_2_test, m.pi/5 ,m.pi, m.pi/25)