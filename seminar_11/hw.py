import numpy
import matplotlib.pyplot as plt
def zad_1():
    x = numpy.linspace(-5,5,100) # используется для генерации последовательности чисел 
    y = 5*x**2 + 10 * x -30 # функция 
    plt.plot(x,y, 'r') # график функции красного цвета линии
    x = numpy.linspace(-5,5,100) 
    y = x * 0 # ось ОХ
    plt.plot(x,y, 'k')
    x = numpy.linspace(-50,150,10)
    y = x *0 # ось OY
    plt.plot(y,x, 'k')
    plt.text(4.8,3,'X')
    plt.text(-0.3,144,'Y')
    plt.show()

def zad_2():
    import random

    square = list(random.randint(100,300) for _ in range(15))
    price = list(random.randint(3000000,20000000) for _ in range(15))
    price_res = list(round(price[i]/square[i],0) for i in range(len(square)))
    
    plt.plot(price_res,'ro')
    plt.axhline(y=50000, color='g')

    plt.show()

zad_2()