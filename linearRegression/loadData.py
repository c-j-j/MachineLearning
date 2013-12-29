__author__ = 'Chris'

def load(filename):
    with open(filename) as f:
        content = f.readlines()

    x=[]
    Y=[]

    for line in content:
        elements = line.split(',')
        x.append(elements[0])
        Y.append(elements[1])

    return x,Y
