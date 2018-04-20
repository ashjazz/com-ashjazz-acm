count = input()
for i in range(int(count)):
    str_1 = raw_input()
    str_2 = str_1[::-1]
    if (str_1 == str_2):
        print 'YES'
    else:
        print 'NO'