# -*- coding: UTF-8 -*-
import datetime

def get_push_time(push_info):
    minutes = push_info[0].split(':')[1]
    hours = push_info[0].split(':')[0]
    return datetime.timedelta(minutes = int(minutes), hours = int(hours))

while 1:
    push_count = input()
    # 提交记录列表
    push_list = []
    # 包含成功AC题目的提交记录 18:00 A RE 19:00 A AC
    push_ac_list = []
    # 状态为AC 的有效提交记录列表
    ac_list = []
    error_count = 0
    ac_all_time = datetime.timedelta(minutes = 0, hours = 0)
    for i in range(push_count):
        push_each = raw_input()
        # 逐条获取提交信息
        push_info = push_each.split(' ')
        push_list.append(push_info)
    # 按照时间进行排序
    for m in range(len(push_list)):
        for n in range(len(push_list)):
            ac_time_n = get_push_time(push_list[n])
            ac_time_m = get_push_time(push_list[m])
            if (ac_time_n > ac_time_m):
                push_info_ex = push_list[m]
                push_list[m] = push_list[n]
                push_list[n] = push_info_ex

    # 找到所有包含AC题目且有效的提交记录
    for push_info in push_list:
        if (push_info[2] == 'AC' and push_info[1] not in ac_list):
            ac_list.append(push_info[1])
            this_ac_time = get_push_time(push_info)
            for push_info_sheep in push_list:
                this_sheep_ac_time = get_push_time(push_info_sheep)
                if (push_info_sheep[1] == push_info[1] and this_sheep_ac_time <= this_ac_time):
                    push_ac_list.append(push_info_sheep)
    for push_info in push_ac_list:
        if(push_info[2] == 'AC'):
            ac_time = get_push_time(push_info)
            ac_all_time += ac_time - datetime.timedelta(minutes = 0,hours = 18)
        else:
            ac_all_time += datetime.timedelta(minutes = 20,hours = 0)
    print '0' + str(ac_all_time)[:4]
            
