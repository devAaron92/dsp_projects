e = 2.718281828459045
k = 5
t = 0
sample_rate = 10


while t >= 0:
    envDecay = e**-(k*t)
    t += 1
    print(envDecay)
    if t > 4:
        break
