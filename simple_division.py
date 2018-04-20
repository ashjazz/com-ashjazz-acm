while 1:
    str_1 = raw_input()
    list_1 = str_1.split(' ')
    a,b = int(list_1[0]),int(list_1[1])
    if (b == 0):
        print 'error'
        continue
    remainder = a%b
    if (float(remainder) >= float(b)/2):
        print int(a/b) + 1
    else:
        print int(a/b)