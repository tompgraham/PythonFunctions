import numpy as np

def main():

    x = 0
    y = 100
    h = .5

    solution = Euler(df, y, h, 30)
    print(solution)

def df(x):
    return 100 - 10 * x
    

def Euler(df, yinit, h, nsteps):
    y = [yinit]
    for i in range(nsteps):
        x = i*h
        ynew = y[-1] + df(x) *h
        y.append(ynew)
    return y
    
main()