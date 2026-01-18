for i in range(1, 1000):
    if 2560*1440*i*200 <= 1*2**33:
        print(i, 2**i)