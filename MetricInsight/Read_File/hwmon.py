"""!
@brief Documentation for "/sys/class/hwmon/hwmon" + hwmon_id + "/in" + file_id + "_label" file.

@section package File Information
- package : Read_File
- name : hwmon.py

@section author Author(s)
- Created by Simon Faucher on 2023-10-01.
- Modified by Simon Faucher on 2024-02-19.

@section libraries_main Libraries/Modules
- None

@section version Current Version
- 1.0

@section date Date
- 2024-02-12

@section copyright Copyright
- Copyright (c) 2024 MetricInsight  All rights reserved.
"""


class Hwmon:
    """!
    Documentation for Hwmon class

    @details The Hwmon class is used to read the /sys/class/hwmon/hwmon[hwmon_id]/in[file_id]_input file and store the values in an object.
    """

    def __init__(self):
        """!
        The constructor for Hwmon class.
        """

        ## Name of the Hwmon object
        self.name = ""

        ## Volts of the Hwmon object
        self.volts = 0

        ## Amps of the Hwmon object
        self.amps = 0

    def __set_name__(self, hwmon_id, file_id):
        """!
        Set the name of the Hwmon object.
        @param hwmon_id: id of the hwmon folder
        @param file_id: id of the file
        @return status : 0 if the file exists, -1 if the file does not exist
        """

        file_label = "/sys/class/hwmon/hwmon" + hwmon_id + "/in" + file_id + "_label"
        try:
            with open(file_label, "r") as f:
                self.name = str(f.read())
        except FileNotFoundError:
            print(f"Le fichier {file_label} n'existe pas.")
            return -1

    def read(self, hwmon_id, file_id):
        """!
        Read the values of the Hwmon object.
        @param hwmon_id: id of the hwmon folder
        @param file_id: id of the file
        @return status : 0 if successful, -1 if not
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
