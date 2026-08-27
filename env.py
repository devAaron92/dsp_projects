e = 2.718281828459045
k = 5
t = 0
samplesPerSecond = 10
n = 0

while n >= 0:
    envDecay = e**-(k*t)
    n += 1
    t = n/samplesPerSecond
    print(envDecay)
    if n > 4:
        break
