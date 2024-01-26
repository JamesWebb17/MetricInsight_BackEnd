""" @package read_file
This file contains the Stat class which is used to read the /proc/stat file
"""


class CPU:
    """ Documentation for CPU class

    More details.
    Class which is used to represent lines containing CPU statistics in the /proc/stat file.
    """

    def __init__(self, system, user, nice, idle):
        """
        The constructor for CPU class.
        :param system: time spend in system
        :param user: time spend in user
        :param nice: time spend in nice
        :param idle: idle time
        """

        self.stime = system
        self.utime = user
        self.nice = nice
        self.idle = idle
        self.starttime = 0

    def __str__(self):
        """
        Return a string representation of the CPU object.
        :return: the string representation of the CPU object
        """

        return (
            f"Time spend in system: {self.stime}\n"
            f"Time spend in user: {self.utime}\n"
            f"Time spend booting : {self.starttime}\n"
            f"Time spend in nice: {self.nice}\n"
            f"Time spend in idle: {self.idle}\n"
        )

    def calculate_time_idle(self):
        """
        Calculate the time spend in idle.
        :return: the time spend in idle
        """
        cal = 0
        for elt in self.idle:
            cal += elt
        return cal


class Stat:
    """
    Documentation for Stat class

    More details.
    Class which is used to read the /proc/stat file.
    """

    def __init__(self):
        """
        The constructor for Stat class.
        """

        self.cpu_stats = {}
        self.intr = 0
        self.context_switches = 0
        self.boot_time = 0
        self.processes_created = 0
        self.running_processes = 0
        self.blocked_processes = 0

    def read_stat(self):
        """
        Read the /proc/stat file and store the data in the Stat object.
        :return: status of the read
        """

        try:
            with open('/proc/stat', 'r') as stat_file:
                for line in stat_file:
                    parts = line.split()
                    if 'cpu' in parts[0]:
                        self.cpu_stats[str(parts[0])] = CPU(int(parts[1]), int(parts[2]), int(parts[3]),
                                                            [int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7]),
                                                             int(parts[8]), int(parts[9]),
                                                             int(parts[10])])
                    elif parts[0] == 'intr':
                        self.intr = str(parts[1:])
                    elif parts[0] == 'ctxt':
                        self.context_switches = int(parts[1])
                    elif parts[0] == 'btime':
                        self.boot_time = int(parts[1])
                    elif parts[0] == 'processes':
                        self.processes_created = int(parts[1])
                    elif parts[0] == 'procs_running':
                        self.running_processes = int(parts[1])
                    elif parts[0] == 'procs_blocked':
                        self.blocked_processes = int(parts[1])
        except FileNotFoundError:
            print("Le fichier /proc/stat n'existe pas.")
            return -1

    def __str__(self):
        """
        Return a string representation of the Stat object.
        :return: the string representation of the Stat object
        """
        result_str = ""
        for key, value in self.cpu_stats.items():
            result_str += f"{key}: {value}\n"
        result_str += f"Interrupts: {self.intr}\n"
        result_str += f"Context Switches: {self.context_switches}\n"
        result_str += f"Boot Time: {self.boot_time}\n"
        result_str += f"Processes Created: {self.processes_created}\n"
        result_str += f"Running Processes: {self.running_processes}\n"
        result_str += f"Blocked Processes: {self.blocked_processes}\n"
        return result_str.strip()
