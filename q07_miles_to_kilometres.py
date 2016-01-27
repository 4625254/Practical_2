print("Miles Kilometers Kilometers Miles")

for i in range (1,11):
    kilometers = i * 1.609
    kilometers_2 = 20 + (i - 1) * 5
    miles = kilometers_2 / 1.609
    print("{0:<5}".format(i),"{0:<10.3f}".format(kilometers),"{0:<10}".format(kilometers_2),"{0:.3f}".format(miles))
