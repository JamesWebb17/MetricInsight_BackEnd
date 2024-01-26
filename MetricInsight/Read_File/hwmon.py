""" @package read_file
Documentation for hwmon module.

More details.
Class for reading hwmon files and create object Hwmon.
"""


class Hwmon:
    def __init__(self):
        """
        The constructor for Hwmon class.
        """
        self.name = ""
        self.volts = 0
        self.amps = 0

    def __set_name__(self, hwmon_id, file_id):
        """
        Set the name of the Hwmon object.
        :param hwmon_id: id of the hwmon folder
        :param file_id: id of the file
        :return:
        """

        file_label = "/sys/class/hwmon/hwmon" + hwmon_id + "/in" + file_id + "_label"
        try:
            with open(file_label, "r") as f:
                self.name = str(f.read())
        except FileNotFoundError:
            print(f"Le fichier {file_label} n'existe pas.")
            return -1

    def read(self, hwmon_id, file_id):
        """
        Read the values of the Hwmon object.
        :param hwmon_id: id of the hwmon folder
        :param file_id: id of the file
        :return:
        """

        file_in = "/sys/class/hwmon/hwmon" + hwmon_id + "/in" + file_id + "_input"
        file_curr = "/sys/class/hwmon/hwmon" + hwmon_id + "/curr" + file_id + "_input"
        try:
            with open(file_in, "r") as f:
                self.amps = float(f"{int(f.read()) / 1000:,.3f}")
        except FileNotFoundError:
            print(f"Le fichier {file_in} n'existe pas.")
            return -1

        try:
            with open(file_curr, "r") as f:
                self.volts = int(f.read())
        except FileNotFoundError:
            print(f"Le fichier {file_curr} n'existe pas.")
            return -1

