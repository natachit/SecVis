with open('./time.txt') as f:
    top = []
    lines = f.read().splitlines()
    for a in lines:
        top.append(a)
    print(top)
        