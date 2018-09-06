with open('./6-type.txt') as f:
    lines = f.read().splitlines()
    for a in lines:
        a = a.split('?')
        c = a[0].split('.')
        if c[-1].find('/') > -1:
            print('Unknown')
        elif c[-1].find('-') > -1:
            print('Unknown')
        elif c[-1].find('_') > -1:
            print('Unknown')
        elif c[-1].find('=') > -1:
            print('Unknown')
        elif c[-1].find('%') > -1:
            print('Unknown')
        elif c[-1].find(',') > -1:
            print('Unknown')
        elif c[-1].find('~') > -1:
            print('Unknown')
        else:
            print(c[-1])
        