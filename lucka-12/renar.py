for i in range(2, 400+1):
    if i < 10:
        if i * i % 10 == i:
            print(i)
    elif i < 100:
        if i * i % 100 == i:
            print(i)
    else:
        if i * i % 1000 == i:
            print(i)
