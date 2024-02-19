"""!
@brief Documentation for MetricInsight file.

@section package File Information
- package : MetricInsight
- name : MetricInsight.py

@section author Author(s)
- Created by Simon Faucher on 2023-10-01.
- Modified by Simon Faucher on 2024-02-19.

@section libraries_main Libraries/Modules
- threading (https://docs.python.org/3/library/threading.html)
--> Access to the threading module
- CPU.utilisation (local)
--> Access to the utilisation_cpu function and the utilisation_cpus function
- GPU.utilisation (local)
--> Access to the utilisation_gpu function
- Memory.utilisation (local)
--> Access to the utilisation_mem function and the utilisation_mems function
- Arguments.usage (local)
--> Access to the usage function
- Power.utilisation (local)
--> Access to the utilisation_power function
- Shared.flags (local)
--> Access to the flags module
- Shared.result (local)
--> Access to the Result class, read_data function, save_data function, plot_data function and smooth_data function

@section version Current Version
- 1.0

@section date Date
- 2024-02-12

@section copyright Copyright
- Copyright (c) 2024 MetricInsight  All rights reserved.
"""

# Importation of the necessary libraries
import threading

from CPU.utilisation import utilisation_cpu, utilisation_cpus
from GPU.utilisation import utilisation_gpu
from Memory.utilisation import utilisation_mem, utilisation_mems
from Arguments.usage import usage
from Power.utilisation import utilisation_power

from Shared import flags
from Shared.result import Result
from Shared.result import read_data, save_data, plot_data, smooth_data


def main():
    """!
    Main function of the program.
    @return status of the program
    """

    threads = []
    result = []

    args = usage()

    if args.verbose:
        flags.VERBOSE_MODE_FLAG = True

    if args.PID != 0:
        print("Monitoring information for the process with PID " + str(args.PID))
        print("WARNING : Only CPU and Memory are specific to a process")
        if args.ALL:
            if flags.VERBOSE_MODE_FLAG:
                print("Mode selected is ALL : CPU, GPU, MEM, POWER")
            threads.append(
                threading.Thread(target=utilisation_cpu, args=(args.PID, args.Frequency, args.Interval, result),
                                 name="CPU"))
            threads.append(
                threading.Thread(target=utilisation_gpu, args=(args.Frequency, args.Interval, result),
                                 name="GPU"))
            threads.append(
                threading.Thread(target=utilisation_mem, args=(args.PID, args.Frequency, args.Interval, result),
                                 name="MEM"))
            threads.append(
                threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result), name="POWER"))

        else:
            if args.CPU:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is CPU")
                threads.append(
                    threading.Thread(target=utilisation_cpu, args=(args.PID, args.Frequency, args.Interval, result),
                                     name="CPU"))
            if args.GPU:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is GPU")
                threads.append(
                    threading.Thread(target=utilisation_gpu, args=(args.Frequency, args.Interval, result), name="GPU"))
            if args.MEM:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is MEM")
                threads.append(
                    threading.Thread(target=utilisation_mem, args=(args.PID, args.Frequency, args.Interval, result),
                                     name="MEM"))
            if args.POWER:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is POWER")
                threads.append(
                    threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result),
                                     name="POWER"))

    else:
        print("Monitoring CPU information without a focus on a process")
        if args.ALL:
            if flags.VERBOSE_MODE_FLAG:
                print("Mode selected is ALL : CPU, GPU, MEM, POWER")

            threads.append(
                threading.Thread(target=utilisation_cpus, args=(args.Frequency, args.Interval, result), name="CPU"))
            threads.append(
                threading.Thread(target=utilisation_gpu, args=(args.Frequency, args.Interval, result), name="GPU"))
            threads.append(
                threading.Thread(target=utilisation_mems, args=(args.Frequency, args.Interval, result), name="MEM"))
            threads.append(
                threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result), name="POWER"))
        else:
            if args.CPU:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is CPU")
                threads.append(
                    threading.Thread(target=utilisation_cpus, args=(args.Frequency, args.Interval, result), name="CPU"))
            if args.GPU:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is GPU")
                threads.append(
                    threading.Thread(target=utilisation_gpu, args=(args.Frequency, args.Interval, result), name="GPU"))
            if args.MEM:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is MEM")
                    threads.append(
                        threading.Thread(target=utilisation_mems, args=(args.Frequency, args.Interval, result),
                                         name="MEM"))
            if args.POWER:
                if flags.VERBOSE_MODE_FLAG:
                    print("Mode selected is POWER")
                threads.append(
                    threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result),
                                     name="POWER"))

    for t in threads:
        if flags.VERBOSE_MODE_FLAG:
            print(f"Beginning of thread {t.name}")
        t.start()

    for t in threads:
        t.join()
        if flags.VERBOSE_MODE_FLAG:
            print(f"End of thread {t.name}")

    if args.Plot:
        if args.Smoothing > 1:
            if flags.VERBOSE_MODE_FLAG:
                print(f"Smoothing data with {args.Smoothing} points...")
                plot_data(smooth_data(result, args.Smoothing))
            else:
                print("Plotting data...")
        else:
            plot_data(result)

    if args.Save:
        if flags.VERBOSE_MODE_FLAG:
            print("Saving data...")
        save_data(args.Save, result)

    if args.Read is not None:
        if flags.VERBOSE_MODE_FLAG:
            print("Reading data...")
        if args.Smoothing > 1:
            if flags.VERBOSE_MODE_FLAG:
                print(f"Smoothing data with {args.Smoothing} points...")
                plot_data(
                    smooth_data([read_data(args.Read, Result("test", "test", []))], args.Smoothing))
            else:
                print("Plotting data...")
        else:
            plot_data([read_data(args.Read, Result("test", "test", []))])

    return 0


if __name__ == "__main__":
    main()

