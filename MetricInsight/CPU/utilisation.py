""" @package CPU
Documentation for CPU module.

More details.
Function for calculating the CPU usage of a process.
"""

import time

from Read_File.PID import Stat as ProcStat
from Read_File.stat import Stat
from Read_File import Uptime
from shared import Result, flags


def calcul_utilisation_cpu(stat, uptime, clock_ticks_per_second):
    """
    Calculate the CPU usage of a process.
    :param stat: Object Stat read from /proc/[pid]/stat
    :param uptime: Object Uptime read from /proc/uptime
    :param clock_ticks_per_second: Number of clock ticks per second
    :return: CPU usage of a process (in %)
    """

    process_utime_sec = stat.utime / clock_ticks_per_second
    process_stime_sec = stat.stime / clock_ticks_per_second
    process_start_sec = stat.starttime / clock_ticks_per_second

    system_uptime_sec = uptime.total_operational_time

    process_elapsed_sec = system_uptime_sec - process_start_sec
    process_cpu_usage = 100 * ((process_utime_sec + process_stime_sec) / process_elapsed_sec)

    return process_cpu_usage


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

        time.sleep(1/frequency)

    list_charge_cpu = calcul_charge_cpu(list_cpu, list_uptime)
    result.append(Result("CPU", "Utilisation du cpu (%)", [list_temps[:-1], list_charge_cpu]))
    flags.THREAD_CPU_END_FLAG = True
    return 0


def calcul_charge_cpu(list_utime, list_uptime):
    list_charge_cpu = []
    for i in range(0, len(list_uptime) - 1):
        cpu_utime = (list_utime[i + 1] - list_utime[i])/100
        cpu_time = list_uptime[i + 1] - list_uptime[i]

        list_charge_cpu.append(cpu_utime / cpu_time * 100)

    return list_charge_cpu


def calcul_utilisation_cpu_systeme(cpu, clock_ticks_per_second):
    """
    Calculate the CPU usage for each heart.
    :param cpu:
    :param clock_ticks_per_second:
    :return:
    """

    utime_sec = cpu.utime / clock_ticks_per_second
    stime_sec = cpu.stime / clock_ticks_per_second
    idle_sec = cpu.idle[0] / clock_ticks_per_second

    cpu_usage = 100 * ((utime_sec + stime_sec) / (utime_sec + stime_sec + idle_sec))

    return cpu_usage


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
            list_cpu[i].append(process_info.cpu_stats.get(f"cpu{i-1}").utime + process_info.cpu_stats.get(f"cpu{i-1}").stime)

        list_temps.append(now - start)

        time.sleep(1/frequency)
        list_uptime.append(uptime_info.total_operational_time)

    result.append(Result(f"CPU", "Utilisation du cpu (%)", [list_temps[:-1], calcul_charge_cpu(list_cpu[0], list_uptime)]))
    for i in range(1, len(list_cpu)):
        result.append(Result(f"CPU{i-1}", "Utilisation du cpu (%)", [list_temps[:-1], calcul_charge_cpu(list_cpu[i], list_uptime)]))
    flags.THREAD_CPU_END_FLAG = True
    return 0
