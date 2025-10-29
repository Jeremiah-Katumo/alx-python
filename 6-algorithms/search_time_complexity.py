# import os
# import time
# import numpy as np
# import algorithms as alg
# #=================================================================================================
# #                                       TQDM Installation
# #=================================================================================================
# try:
#     from tqdm import tqdm
# except:
#     print("'tqdm' module not found.")
#     print("installing tqdm modle...")
#     os.system('pip install tqdm')

# #=================================================================================================
# #                                  FUNCTION TO RUN EXPERIMENTS
# #=================================================================================================

# def run_experiment(algorithm,desc='',STEP=1000, REPS_PER_ARR=100, MAX_ARR_LEN=100000):
#     len_of_arr = []
#     exec_times = []
#     for i in tqdm(range(1,MAX_ARR_LEN+STEP, STEP),desc='Experiment Progress '+'('+desc+')'):
#         array = np.random.randint(1000, size=i).tolist()
#         array.sort()
#         cumulative_execution_time=0
#         for j in range(REPS_PER_ARR):
#             target = array[np.random.randint(len(array))]  #Randomly select an element from the array
#             start = time.perf_counter()
#             algorithm(array,target)
#             end = time.perf_counter()
#             cumulative_execution_time = cumulative_execution_time + (end-start)
#         avg_execution_time = cumulative_execution_time/REPS_PER_ARR
#         len_of_arr.append(i)
#         exec_times.append(avg_execution_time)
#     return  len_of_arr,exec_times


import numpy as np
import time

# Try importing tqdm safely
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, desc=None):
        total = len(iterable)
        if desc:
            print(desc)
        for idx, item in enumerate(iterable, 1):
            if idx % max(1, total // 10) == 0:
                print(f"Progress: {int(idx / total * 100)}%")
            yield item

def run_experiment(algorithm, desc, STEP=1000, REPS_PER_ARR=1000, MAX_ARR_LEN=10000):
    len_of_arr = []
    exec_times = []

    for i in tqdm(range(1, MAX_ARR_LEN + STEP, STEP), desc='Experiment Progress (' + desc + ')'):
        array = np.random.randint(1000, size=i).tolist()
        array.sort()

        start_time = time.time()
        for _ in range(REPS_PER_ARR):
            target = np.random.choice(array)
            algorithm(array, target)
        elapsed = time.time() - start_time

        len_of_arr.append(i)
        exec_times.append(elapsed / REPS_PER_ARR)

    return exec_times, len_of_arr