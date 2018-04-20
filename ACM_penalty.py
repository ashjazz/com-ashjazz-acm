import datetime

while 1:
    push_count = input()
    error_count = 0
    ac_time = datetime.timedelta(minutes=0,hours=0)
    print ac_time
    for i in range(push_count):
        each_sign = raw_input()
        sign_list = each_sign.split(' ')
        time_push = sign_list[0]
        pro_num = sign_list[1]
        push_status = sign_list[2]
        if (push_status != 'AC'):
            error_count += 1
        else:
            
