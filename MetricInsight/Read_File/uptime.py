""" @package read_file

Documentation for uptime module.

More details.
Class for reading hwmon files and create object Uptime.
"""


class Uptime:
    def __init__(self):
        """
        The constructor for Uptime class.
        """

        self.total_operational_time = 0
        self.idle_time = 0

    def read_proc_uptime(self):
        """
        Read the values of the Uptime object.
        :return:
        """

        try:
            with open('/proc/uptime') as f:
            #with open('./Files/uptime') as f:
                data = f.read().split()
                self.total_operational_time = float(data[0])
                self.idle_time = float(data[1])
        except FileNotFoundError:
            print("Le fichier /proc/uptime n'existe pas.")
            return -1

    def display_info(self):
        """
        Display the values of the Uptime object.
        :return:
        """

        print(f"Temps total de fonctionement: {self.total_operational_time}")
        print(f"Temps d'inactivité : {self.idle_time}")
