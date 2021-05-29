import matplotlib.pyplot as plt

def DDA(a, b):
    print("METODO DDA")
    x1 = a
    y1 = b
    x2= x1
    y2= y1 + 4
    x3= x1 + 4
    y3= y1
    x4= x3 
    y4=y2 
    s=0

    dx= abs(x2-x1)
    dy= abs(y2-y1)
    dx1= abs(x4-x3)
    dy1= abs(y4-y3)
    dx2= abs(x3-x1)
    dy2= abs(y3-y1)
    dx3= abs(x4-x2)
    dy3= abs(y4-y2)

    if dx > dy:
        steps= dx
    else:
        steps= dy


    if dx1 > dy1:
        steps= dx1
    else:
        steps= dy1

    if dx2 > dy2:
        steps= dx2
    else:
        steps= dy2

    if dx3 > dy3:
        steps= dx3
    else:
        steps= dy3

    incx= dx/steps
    incy= dy/steps
    incx1= dx1/steps
    incy1= dy1/steps
    incx2= dx2/steps
    incy2= dy2/steps
    incx3= dx3/steps
    incy3= dy3/steps
    f=x2
    ff=x4
    g= x3
    gg=x1
  

    for i in range (s, steps +1):
        #DIBUJAMOS LOS PIXELES
        plt.plot(round(x1), round(y1),marker="8",color="Red")
        plt.plot(round(x3), round(y3),marker="8",color="Red")
        plt.plot(round(f), round(ff),marker="8",color="Red")
        plt.plot(round(y1), round(gg),marker="8",color="Red")

        x1= x1+incx
        y1= y1+incy

        x3= x3+incx1
        y3= y3+incy1

        f= f+incx2
        ff= ff+incy2

        g= g+incx3
        gg= gg+incy3 
    return 0

def BRESENHAMS(a, b):
    print("METODO BRESENHAMS")

    x1 = a
    y1 = b

    x3= x1
    y3= y1 + 4

    x2= x1 + 4
    y2= y1

    x4= x3 
    y4=y2 

    dx1= abs(x2 - x1)
    dy1 =abs(y2 -y1)
    p= (2 * dy1) -dx1

    dx2= abs(x3 - x1)
    dy2 =abs(y3 -y1)
    p2= (2 * dy2) -dx2

    while x1 < x2:
        plt.plot(round(x1),round(y1), marker="8", color="Blue")
        plt.plot(round(x2),round(y2), marker="8", color="Blue")
        plt.plot(round(y2),round(x2), marker="8", color="Blue")
        plt.plot(round(y1),round(x1), marker="8", color="Blue")
        x1= x1 + 1
              
        if p < 0:
            p= p + (2 * dy1)
        else:
            p= p + (2 * dy1) - (2 * dx1)
            y1= y1 + 1
        if p2 < 0:
            p2= p2 + (2 * dy2)
        else:
            p2= p2 + (2 * dy2) - (2 * dx2)
            y2= y2 + 1
    return 0

def error():
   print ("Opcion Invalida")

def menu():
   print("--Presione 1 para el metodo DDA Y 2 para BRESENHAM--")
   
def switch(case, a, b):
    if case == 1:
        DDA(a,b)
    elif case == 2:
        BRESENHAMS(a,b)
    else:
        return error()

if __name__=='__main__':
   a=1
   b=1
   menu()
   case=0
   case = int(input("SELECCIONE EL METODO: ")) 
   switch(case, a, b)
   plt.grid()
   plt.show()