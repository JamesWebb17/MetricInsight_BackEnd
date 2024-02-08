""" @package CPU
Documentation for CPU module.

More details.
Function for calculating the CPU usage of a process.
"""

import time

from MetricInsight.Read_File.PID.stat import Stat as ProcStat
from MetricInsight.Read_File.stat import Stat
from MetricInsight.Read_File.uptime import Uptime
from MetricInsight.Shared import flags
from MetricInsight.Shared.result import Result


def utilisation_cpu(pid, frequency, interval, result):
    """
    Find the CPU usage of a process in files /proc/[pid]/stat and /proc/uptime.
    :param pid: pid of the process
    :param frequency: point per second wanted
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    process_info = ProcStat(pid)
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_cpu = []
    list_uptime = []
    list_temps = []
    while process_info.read_proc_stat() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)
        list_cpu.append(process_info.utime + process_info.stime)
        list_uptime.append(uptime_info.total_operational_time)
        list_temps.append(now - start)

        time.sleep(1 / frequency)

    list_charge_cpu = calcul_charge_cpu(list_cpu, list_uptime)
    result.append(Result("CPU", "Utilisation du cpu (%)", [list_temps[:-1], list_charge_cpu]))
    flags.THREAD_CPU_END_FLAG = True
    return 0


def web_utilisation_cpu(shared_queue, configuration):
    """
    Find the Memory usage of a process in files /proc/[pid]/statm and /proc/uptime.
    :param shared_queue: queue for sending the result to the main thread
    :param configuration: configuration of the program
    :return: status of the function
    """

    flags.THREAD_CPU_END_FLAG = False

    interval = int(configuration['IntervalInput'])
    frequency = int(configuration['FreqInput'])
    pid = int(configuration['pidInput'])

    process_info = ProcStat(pid)
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    temps_cpu = 0
    temps_uptime = 0

    while process_info.read_proc_stat() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        temps_cpu_t = process_info.utime + process_info.stime
        temps_uptime_t = uptime_info.total_operational_time

        time.sleep(1 / frequency)

        list_charge_cpu = calcul_charge_cpu([temps_cpu, temps_cpu_t], [temps_uptime, temps_uptime_t])
        shared_queue.put([now - start, list_charge_cpu[-1]])

        temps_cpu = temps_cpu_t
        temps_uptime = temps_uptime_t

    shared_queue.put("END")
    print("Fin du thread CPU.")
    flags.THREAD_CPU_END_FLAG = True
    return 0


def calcul_charge_cpu(list_utime, list_uptime):
    list_charge_cpu = []
    for i in range(0, len(list_uptime) - 1):
        cpu_utime = (list_utime[i + 1] - list_utime[i]) / 100
        cpu_time = list_uptime[i + 1] - list_uptime[i]

        list_charge_cpu.append(cpu_utime / cpu_time * 100)

    return list_charge_cpu

def web_utilisation_cpus(shared_queue, configuration):
    """
    Find the Memory usage of a process in files /proc/[pid]/statm and /proc/uptime.
    :param shared_queue: queue for sending the result to the main thread
    :param configuration: configuration of the program
    :return: status of the function
    """

    flags.THREAD_CPU_END_FLAG = False

    interval = int(configuration['IntervalInput'])
    frequency = int(configuration['FreqInput'])

    process_info = Stat()
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    temps_cpu = [0 for i in range(0, 13)]
    temps_cpu_t = [0 for i in range(0, 13)]
    list_charge_cpu = []

    temps_uptime = 0

    while process_info.read_stat() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        temps_uptime_t = uptime_info.total_operational_time
        temps_cpu_t[0] = process_info.cpu_stats.get(f"cpu").utime + process_info.cpu_stats.get(f"cpu").stime

        for i in range(1, len(temps_cpu)):
            temps_cpu_t[i] = process_info.cpu_stats.get(f"cpu{i - 1}").utime + process_info.cpu_stats.get(f"cpu{i - 1}").stime

        for i in range(0, len(temps_cpu)):
            t = calcul_charge_cpu([temps_cpu[i], temps_cpu_t[i]], [temps_uptime, temps_uptime_t])
            list_charge_cpu.append(t[-1])

        print([now - start]+ list_charge_cpu)
        print()
        print()

        #shared_queue.put(shared_queue.put([now - start] + list_charge_cpu))

        temps_cpu = list(temps_cpu_t)
        temps_cpu_t = [0 for i in range(13)]

        temps_uptime = temps_uptime_t

        time.sleep(1 / frequency)

    shared_queue.put("END")
    print("Fin du thread CPU.")
    flags.THREAD_CPU_END_FLAG = True
    return 0

def utilisation_cpus(frequency, interval, result):
    """
    Find the CPU usage of a process in files /proc/stat and /proc/uptime.
    :param frequency: point per second wanted
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    process_info = Stat()
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_cpu = [[] for i in range(0, 13)]
    list_temps = []
    list_uptime = []
    while process_info.read_stat() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        process_info.cpu_stats.get("cpu").starttime = uptime_info.total_operational_time
        list_cpu[0].append(process_info.cpu_stats.get(f"cpu").utime + process_info.cpu_stats.get(f"cpu").stime)

        for i in range(1, len(list_cpu)):
            list_cpu[i].append(
                process_info.cpu_stats.get(f"cpu{i - 1}").utime + process_info.cpu_stats.get(f"cpu{i - 1}").stime)

        list_temps.append(now - start)

        time.sleep(1 / frequency)
        list_uptime.append(uptime_info.total_operational_time)

    result.append(
        Result(f"CPU", "Utilisation du cpu (%)", [list_temps[:-1], calcul_charge_cpu(list_cpu[0], list_uptime)]))
    for i in range(1, len(list_cpu)):
        result.append(Result(f"CPU{i - 1}", "Utilisation du cpu (%)",
                             [list_temps[:-1], calcul_charge_cpu(list_cpu[i], list_uptime)]))
    flags.THREAD_CPU_END_FLAG = True
    return 0
