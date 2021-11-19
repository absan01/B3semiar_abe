import random
l = []

def randlist(n):
    for i in range(n + 1):
        l.append(int(random.random()*100))
    print(l)