

with open('domain.txt', 'r+') as file:
    for line in file:
        print('www.%s' % line.strip('\n'))
        print('*.%s' % line.strip('\n'))
        print('%s' % line.strip('\n'))