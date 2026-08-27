sample = float(input("Enter sample: "))

gain = float(input("Enter gain: "))

out = sample * gain

if out > 1:
    print('The number is outside the range')

elif out < -1:
    print("The number is outside the range")

else:
    print(out)