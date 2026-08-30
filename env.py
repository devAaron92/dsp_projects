import math
envSequence = []
waveForm = 0
pi = 3.14159265359

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
    envSequence.append(envDecay)
    
    if n > 4:
        break
thetaIndex = 0

theta = []
position = 0

for var in envSequence:

    intervals = (len(envSequence) - 1)

    theta.append((2 * pi / intervals) * position)

    position += 1

    if position > 4:
        break

print(theta)


