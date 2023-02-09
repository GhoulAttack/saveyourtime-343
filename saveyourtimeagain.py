import os

scheduler_list = ['sjf_sched', 'srpt_sched', 'priority_sched', 'rr_sched', 'stride_sched']
workload_list = os.listdir('workloads')
os.mkdir('This_is_yours')
os.mkdir('This_is_instructor')
for scheduler in scheduler_list:
    for workload in workload_list:
        os.system(
            './queuesim ' + scheduler + ' workloads/' + workload + ' > This_is_yours/' + scheduler + '_' + workload)
for scheduler in scheduler_list:
    for workload in workload_list:
        os.system(
            './queuelab_solution ' + scheduler + ' workloads/' + workload + ' > This_is_instructor/' + scheduler + '_' + workload)

for scheduler in scheduler_list:
    error_flag = 0
    for workload in workload_list:
        with open('This_is_yours/' + scheduler + '_' + workload) as f:
            content = f.read()
        with open('This_is_instructor/' + scheduler + '_' + workload) as f:
            content_instructor = f.read()
            if content != content_instructor:
                print('Oops! Something wrong!\n')
                print('scheduler: ' + scheduler +'workload:'+workload+ '\n')
                error_flag = 1
    if error_flag == 0:
        print('We are safe...for now\n')

