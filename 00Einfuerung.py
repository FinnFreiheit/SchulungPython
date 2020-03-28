import math

def creat():
    m = input("m Eingabe ")
    n = input("n Eingabe ")
    matrix = [[ [] for j in range(int (n))] for i in range(int(m))]
    for k in range(int(m)):
        print(matrix[k])




def umrechnung():
    temp = input("Temperatur Eingabe")
    if temp[-1] == 'C':
        temp = temp[:-1]
        temp = int(temp)
        temp = temp * 9/5 + 32
        print(temp,'F')
    elif temp[-1] == 'F':
        temp = temp[:-1]
        temp = int(temp)
        temp = temp * 5/9 - 32
        print(temp,'C')
    else: print("Fehler")


def pi_Berechnung():
    x = 1
    i = 1
    j = 3
    dif = 1
    cout = 0

    while (dif > 0.0000001) or (dif < 0.00000001):
        x = x + (-1) ** i / j
        i += 1
        j += 2
        dif = x*4 - math.pi
        cout += 1
    print(x*4)
    print(cout)



def Sortieren():
    feld = []
    x = 1

    while x != '0':
        x = input("Zahl eingeben")
        feld.append(x)
    print(feld[:-1])


def prim():
    i = int(input("Range: "))
    feld = list(range(i+1))
    print(feld)
    for q in range(2, i+1):
        j = 2

        while q*j <= i:
            feld[q*j] = 0
            j += 1

    print(feld)
    for i in range(feld.count(0)):
        feld.remove(0)
    feld.remove(1)
    print(feld)

class Quadrat(object):
    def quadr(self):
        a = int(input("Eingabe a: "))
        b = int(input("Eingabe b: "))
        c = int(input("Eingabe c: "))

        y = ((-b) + ((b ** 2) - 4 * a * c) ** (1/2)) / (2 * a)
        z = ((-b) - ((b ** 2) - 4 * a * c) ** (1/2)) / (2 * a)

        print("x1 = ", y)
        print("x2 = ", z)

obj = Quadrat()
obj.quadr()

def aufg_sieben():
    x = int(input("Bitte Zahl eingeben "))
    while x != 0:
        if x % 3 == 0:
            x = x + 4
        elif x % 4 == 0:
            x = x // 2
        else:
            x = x - 1
        print(x)


def schildkroete():

    import turtle

    t = turtle.Turtle()

    x = 250
    for k in range(20):
        for k in range(4):
            t.rt(90)
            t.fd(x)


        t.rt(75)
        x = x - 13

    input()
