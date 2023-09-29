def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])    
    n = len(jobs)
    selected_jobs = []
    selected_jobs.append(jobs[0])
    prev_end_time = jobs[0][1]

    for i in range(1, n):
        if jobs[i][0] >= prev_end_time:
            selected_jobs.append(jobs[i])
            prev_end_time = jobs[i][1]

    return selected_jobs

jobs = [(1, 3, 5), (2, 5, 6), (6, 9, 8), (3, 8, 7), (5, 9, 9)]

selected_jobs = job_scheduling(jobs)
print("Selected Jobs:")
for job in selected_jobs:
    print("Start time:", job[0], "End time:", job[1], "Profit:", job[2])
