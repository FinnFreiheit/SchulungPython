'''

0	0001101
1	0011001
2	0010011
3	0111101
4	0100011
5	0110001
6	0101111
7	0111011
8	0110111
9	0001011

'''

import turtle
stiftDicke = 5

t = turtle.Turtle()
t.speed(0)
t.pensize(stiftDicke)
t.hideturtle()

def startStriche():

    t.back(20)
    Linie(1, 120)
    Linie(0, 120)
    Linie(1, 120)

    t.penup()
    t.fd(20)
    t.pendown()

def mitteStriche():

    t.penup()
    t.back(20)
    t.pendown()
    Linie(0,120)
    Linie(1, 120)
    Linie(0, 120)
    Linie(1, 120)
    Linie(0,120)

    t.penup()
    t.fd(20)
    t.pendown()

def ausrichtenLinks():

    t.penup()
    t.left(180)
    t.fd(300)
    t.right(90)
    t.pendown()
    startStriche()



def Linie(wert,laenge):

    if wert == 1:
        t.fd(laenge)
        t.penup()
        t.back(laenge)
        t.right(90)
        t.fd(stiftDicke)
        t.left(90)
        t.pendown()
    else:
        t.penup()
        t.fd(laenge)
        t.back(laenge)
        t.right(90)
        t.fd(stiftDicke)
        t.left(90)
        t.pendown()


ausrichtenLinks()

feld = {}
feld[0] = 0b0001101
feld[1] = 0b0011001
feld[2] = 0b0010011
feld[3] = 0b0111101
feld[4] = 0b0100011
feld[5] = 0b0110001
feld[6] = 0b0101111
feld[7] = 0b0111011
feld[8] = 0b0110111
feld[9] = 0b0001011


eing = input()

if len(eing) == 12:

    for k in range(7):
        temp = 0b1000000
        for l in range(7):
            if feld[int(eing[k])] & temp:
                Linie(1,100)
            else:
                Linie(0,100)
            temp = temp >> 1

    mitteStriche()

    for k in range(6):
        k = k + 6
        temp = 0b1000000
        for l in range(7):
            if feld[int(eing[k])] & temp:
                Linie(1,100)
            else:
                Linie(0,100)
            temp = temp >> 1

    startStriche()
else:
    t.write("Fehler", font = ("Arial", 20, "normal"))

input()