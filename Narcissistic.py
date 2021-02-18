for i in range(100, 1000):
    hundred = int(i / 100)
    ten = int((i % 100) / 10)
    one = i % 10
    if (hundred ** 3) + (ten ** 3) + (one ** 3) == i:
        print(i)
