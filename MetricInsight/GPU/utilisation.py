""" @package Memory
Documentation for GPU module.

More details.
Function for calculating the GPU charge.
"""

import time

from MetricInsight.Read_File.PID.gpu import GPU
from MetricInsight.Shared import flags
from MetricInsight.Shared.result import Result


def utilisation_gpu(frequency, interval, result):
    """
    Find the Memory usage of a process in files /proc/[pid]/statm and /proc/uptime.
    :param frequency: frequency of the points
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    process_info = GPU()

    list_gpu = []
    list_temps = []

    while process_info.read() != -1 and now - start < interval and flags.THREAD_CPU_END_FLAG is False and flags.THREAD_MEM_END_FLAG is False:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        list_gpu.append(process_info.load / 10)
        list_temps.append(now - start)

        time.sleep(1 / frequency)

    result.append(Result("GPU", "Utilisation GPU (%)", [list_temps, list_gpu]))
    flags.THREAD_GPU_END_FLAG = True
    return 0


def web_utilisation_gpu(shared_queue, configuration):
    """
    Find the Memory usage of a process in files /proc/[pid]/statm and /proc/uptime.
    :param shared_queue: queue for sending the result to the main thread
    :param configuration: configuration of the program
    :return: status of the function
    """

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    process_info = GPU()

    interval = int(configuration['IntervalInput'])
    frequency = int(configuration['FreqInput'])

    while process_info.read() != -1 and now - start < interval and not flags.END_FLAG:
        now = time.clock_gettime(time.CLOCK_REALTIME)
        shared_queue.put([now - start, process_info.load / 10])

        time.sleep(1 / frequency)
    shared_queue.put("END")
    print("Fin du thread GPU.")
    flags.THREAD_GPU_END_FLAG = True
    return 0
