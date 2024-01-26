"""
This is the main file of the project. It is used to launch the program.

More details.

"""

import threading

import shared
from CPU import utilisation_cpu, utilisation_cpus
from GPU.utilisation import utilisation_gpu
from Memory import utilisation_mem, utilisation_mems
import Arguments
from Power import utilisation_power
from shared import flags, Result


def main():
    """
    Main function of the program.
    :return: status of the program
    """

    threads = []
    result = []

    args = Arguments.usage()

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
                shared.plot_data(shared.smooth_data(result, args.Smoothing))
            else:
                print("Plotting data...")
        else:
            shared.plot_data(result)

    if args.Save:
        if flags.VERBOSE_MODE_FLAG:
            print("Saving data...")
        shared.save_data(args.Save, result)

    if args.Read is not None:
        if flags.VERBOSE_MODE_FLAG:
            print("Reading data...")
        if args.Smoothing > 1:
            if flags.VERBOSE_MODE_FLAG:
                print(f"Smoothing data with {args.Smoothing} points...")
                shared.plot_data(
                    shared.smooth_data([shared.read_data(args.Read, Result("test", "test", []))], args.Smoothing))
            else:
                print("Plotting data...")
        else:
            shared.plot_data([shared.read_data(args.Read, Result("test", "test", []))])

    return 0


if __name__ == "__main__":
    main()

import queue
import time
from copy import deepcopy
def produire(queue):
    for i in range(100):
        item = f"Produit {i}"
        queue.put(item)
        print(f"Produit: {item}")
        time.sleep(0.1)
    queue.put("END")
    return 0

