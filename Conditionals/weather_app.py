temp = 65
isSunOut = False
precip = 'rainy'

if temp > 80:
    print("It's very hot")
elif temp > 70 or isSunOut == True:
    print("It's hot")
elif temp >= 50 and temp <= 70:
    print("It's cool")
elif temp < 50:
    print("It's cold")
else:
    print("It's nice outside")

if temp >= 100:
    print("It's a new heat record")

if precip != 'rain':
    print("It's dry")