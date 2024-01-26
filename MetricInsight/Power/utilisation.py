""" @package Power
Documentation for Power module.

More details.
Function for calculating the Power usage of a process.
"""

import time

from Read_File import Uptime, Hwmon
from shared import Result, flags


def utilisation_power(frequency, interval, result):
    """
    Find the Power usage of a process in files system.
    :param frequency: point per second wanted
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    vdd_gpu_soc = Hwmon()
    vdd_gpu_soc.__set_name__("3", "1")
    vdd_cpu_cv = Hwmon()
    vdd_cpu_cv.__set_name__("3", "2")
    vin_sys_5_v0 = Hwmon()
    vin_sys_5_v0.__set_name__("3", "3")
    vddq_vdd2_1_v8_ao = Hwmon()
    vddq_vdd2_1_v8_ao.__set_name__("4", "2")

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_power_vdd_gpu_soc = []
    list_power_vdd_cpu_cv = []
    list_power_vin_sys_5_v0 = []
    list_power_vddq_vdd2_1_v8_ao = []

    list_temps = []

    while (vdd_gpu_soc.read("3", "1") != -1 and vdd_cpu_cv.read("3", "2") != -1 and
           vin_sys_5_v0.read("3", "3") != -1 and vddq_vdd2_1_v8_ao.read("4", "2") != -1 and
            now - start < interval and
           (flags.THREAD_CPU_END_FLAG is False or flags.THREAD_MEM_END_FLAG is False)):
        now = time.clock_gettime(time.CLOCK_REALTIME)

        list_power_vdd_gpu_soc.append(vdd_gpu_soc.amps * vdd_gpu_soc.volts)
        list_power_vdd_cpu_cv.append(vdd_cpu_cv.amps * vdd_cpu_cv.volts)
        list_power_vin_sys_5_v0.append(vin_sys_5_v0.amps * vin_sys_5_v0.volts)
        list_power_vddq_vdd2_1_v8_ao.append(vddq_vdd2_1_v8_ao.amps * vddq_vdd2_1_v8_ao.volts)

        list_temps.append(now - start)

        time.sleep(1/frequency)

    result.append(
        Result("POWER_" + vdd_gpu_soc.name, "Consomation énergétique (mW)", [list_temps, list_power_vdd_gpu_soc]))
    result.append(
        Result("POWER_" + vdd_cpu_cv.name, "Consomation énergétique (mW)", [list_temps, list_power_vdd_cpu_cv]))
    result.append(
        Result("POWER_" + vin_sys_5_v0.name, "Consomation énergétique (mW)", [list_temps, list_power_vin_sys_5_v0]))
    result.append(Result("POWER_" + vddq_vdd2_1_v8_ao.name, "Consomation énergétique (mW)",
                         [list_temps, list_power_vddq_vdd2_1_v8_ao]))
    flags.THREAD_POWER_END_FLAG = True
    return 0
