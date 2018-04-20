str_1 = raw_input()
num_1 = int(str_1)
num_2 = int(str_1[0])**3 + int(str_1[1])**3 + int(str_1[2])**3
if (num_1 == num_2):
    print 'YES'
else :
    print 'NO'