"""!
@brief Documentation for Memory module.

@section package File Information
- package : Memory
- name : utilisation.py

@section author Author(s)
- Created by Simon Faucher on 2023-10-01.
- Modified by Simon Faucher on 2024-02-19.

@section libraries_main Libraries/Modules
- time (https://docs.python.org/3/library/time.html)
- MetricInsight.Read_File.PID.statm.Statm (local)
--> Access to Statm class.
- MetricInsight.Read_File.meminfo.MemInfo (local)
--> Access to MemInfo class.
- MetricInsight.Shared.flags (local)
--> Access to THREAD_MEM_END_FLAG and END_FLAG.
- MetricInsight.Shared.result.Result (local)
--> Access to Result class.

@section version Current Version
- 1.0

@section date Date
- 2024-02-12

@section copyright Copyright
- Copyright (c) 2024 MetricInsight  All rights reserved.
"""

import time

from MetricInsight.Read_File.PID.statm import Statm
from MetricInsight.Read_File.meminfo import MemInfo
from MetricInsight.Shared import flags
from MetricInsight.Shared.result import Result


def utilisation_mem(pid, frequency, interval, result):
    """!
    Find the Memory usage of a process in files /proc/[pid]/statm and /proc/uptime.
    @param pid: pid of the process
    @param frequency: frequency of the points
    @param interval: interval of time wanted
    @param result: array for sending the result to the main thread
    @return status of the function
    """

    process_info = Statm(pid)

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_mem = []
    list_temps = []

    while process_info.read_proc_statm() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        list_mem.append(process_info.size)
        list_temps.append(now - start)

        time.sleep(1 / frequency)

    result.append(Result("MEM", "Utilisation mémoire (kB)", [list_temps, list_mem]))
    flags.THREAD_MEM_END_FLAG = True
    return 0


def utilisation_mems(frequency, interval, result):
    """!
    Find the Memory usage without a focus on a process in file /proc/meminfo and /proc/uptime.
    @param frequency: frequency of the points
    @param interval: interval of time wanted
    @param result: array for sending the result to the main thread
    @return status of the function
    """

    process_info = MemInfo()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_mem = []
    list_temps = []

    while process_info.read_meminfo() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        list_mem.append(process_info.mem_total - process_info.mem_free)
        list_temps.append(now - start)

        time.sleep(1 / frequency)

    result.append(Result("MEM", "Utilisation mémoire (kB)", [list_temps, list_mem]))
    flags.THREAD_MEM_END_FLAG = True
    return 0


def web_utilisation_memory(shared_queue, configuration):
    """!
       Find the Memory usage without a focus on a process in file /proc/meminfo and /proc/uptime.
       @param shared_queue: queue for sending the result to the main thread
       @param configuration: configuration of the program
       @return status of the function
   """

    flags.THREAD_MEM_END_FLAG = False

    interval = int(configuration['IntervalInput'])
    frequency = int(configuration['FreqInput'])
    pid = int(configuration['pidInput'])

    process_info = Statm(pid)

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    while process_info.read_proc_statm() != -1 and now - start < interval and not flags.END_FLAG:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        shared_queue.put([now - start, process_info.size])

        time.sleep(1 / frequency)

    shared_queue.put("END")
    print("Fin du thread Memory.")
    flags.THREAD_MEM_END_FLAG = True
    return 0


def web_utilisation_all_memory(shared_queue, configuration):
    """!
       Find the Memory usage without a focus on a process in file /proc/meminfo and /proc/uptime.
       @param shared_queue: queue for sending the result to the main thread
       @param configuration: configuration of the program
       @return status of the function
   """

    flags.THREAD_MEM_END_FLAG = False

    process_info = MemInfo()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    interval = int(configuration['IntervalInput'])
    frequency = int(configuration['FreqInput'])

    while process_info.read_meminfo() != -1 and now - start < interval and not flags.END_FLAG:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        shared_queue.put([now - start, process_info.mem_total - process_info.mem_free])

        time.sleep(1 / frequency)

    shared_queue.put("END")
    print("Fin du thread Memory.")
    flags.THREAD_MEM_END_FLAG = True
    return 0
