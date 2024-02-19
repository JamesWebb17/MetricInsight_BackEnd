"""!
@brief Documentation for proc/uptime file.

@section package File Information
- package : Read_File
- name : uptime.py

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


class Uptime:
    """!
    Documentation for Uptime class

    @details The Uptime class is used to read the /proc/uptime file and store the values in an object.
    """

    def __init__(self):
        """!
        The constructor for Uptime class.
        """

        ## Total operational time
        self.total_operational_time = 0

        ## Idle time
        self.idle_time = 0

    def read_proc_uptime(self):
        """!
        Read the values of the Uptime object.
        @return status of the file reading (0 if successful, -1 if not)
        """

        try:
            with open('/proc/uptime') as f:
            #with open('./MetricInsight/Files/uptime') as f:
                data = f.read().split()
                self.total_operational_time = float(data[0])
                self.idle_time = float(data[1])
        except FileNotFoundError:
            print("Le fichier /proc/uptime n'existe pas.")
            return -1

    def display_info(self):
        """!
        Display the values of the Uptime object.
        """

        print(f"Temps total de fonctionement: {self.total_operational_time}")
        print(f"Temps d'inactivité : {self.idle_time}")
