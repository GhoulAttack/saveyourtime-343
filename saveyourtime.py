import texttable
import os

scheduler_list = ['fifo_sched', 'sjf_sched', 'srpt_sched', 'priority_sched', 'rr_sched', 'stride_sched']
workload_list = os.listdir('workloads')
os.mkdir('This_is_a_folder')
for scheduler in scheduler_list:
    for workload in workload_list:
        os.system(
            './queuesim ' + scheduler + ' workloads/' + workload + ' > This_is_a_folder/' + scheduler + '_' + workload)

for scheduler in scheduler_list:
    Table = texttable.Texttable()
    Table.set_cols_dtype(['t', 't', 't', 't', 't'])
    Table.add_row(['workload', 'avg_turnaround_time', 'std_turnaround_time', 'avg_slowdown_time', 'std_slowdown_time'])
    for workload in workload_list:
        with open('This_is_a_folder/' + scheduler + '_' + workload) as f:
            content = f.read()
            avg_turnaround_time = content.split('average turnaround time:                ')[1].split('\n')[0]
            std_turnaround_time = content.split('stddev turnaround time:                 ')[1].split('\n')[0]
            avg_slowdown_time = content.split('average slowdown:                       ')[1].split('\n')[0]
            std_slowdown_time = content.split('stddev slowdown:                        ')[1].split('\n')[0]
            Table.add_row([workload, avg_turnaround_time, std_turnaround_time, avg_slowdown_time, std_slowdown_time])
    with open('This_is_a_result.txt', 'a') as f1:
        f1.write(scheduler + ':\n')
        f1.write(Table.draw()+'\n')
