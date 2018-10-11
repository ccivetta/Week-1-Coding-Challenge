'''
Created on Oct 11, 2018

@author: ChrisCivetta
'''
def check(x):
    c = 0
    while True:
        b = False
        for i in x:
            #print(i)
            if c == i:
                b = True
        if b == False:
            return c 
        else:
            c += 1

lst = [0, 1, 2, 3]
print(check(lst))