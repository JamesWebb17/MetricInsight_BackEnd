"""!
@brief Documentation for proc/[PID]/statm file.

@section package File Information
- package : PID
- name : statm.py

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


class Statm:
    """!
    Documentation for Statm class

    @details The Statm class is used to read the /proc/[PID]/statm file and store the values in an object.
    """

    def __init__(self, pid):
        """!
        The constructor for Statm class.
        @param pid: pid of the process
        """

        ## pid of the process
        self.pid = pid

        ## total program size
        self.size = 0

        ## resident set size
        self.resident = 0

        ## shared pages
        self.share = 0

        ## text (code)
        self.text = 0

        ## library
        self.lib = 0

        ## data/stack
        self.data = 0

        ## dirty pages
        self.dt = 0

    def read_proc_statm(self):
        """!
        Read the values of the Statm object.
        @return status of the read (0 if successful, -1 if not)
        """

        pid = self.pid
        try:
            with open(f'/proc/{pid}/statm') as f:
            #with open(f'./MetricInsight/Files/21863/statm.txt') as f:
                data = f.read().split()
                if len(data) >= 7:  # Assurez-vous que suffisamment de données ont été lues
                    self.size = int(data[0])
                    self.resident = int(data[1])
                    self.share = int(data[2])
                    self.text = int(data[3])
                    self.lib = int(data[4])
                    self.data = int(data[5])
                    self.dt = int(data[6])
        except FileNotFoundError:
            print(f"Le fichier /proc/{pid}/statm n'existe pas.")
            return -1

    def display_info(self):
        """!
        Display the values of the Statm object.
        @return None
        """

        print(f"Taille totale : {self.size}")
        print(f"Taille résidente : {self.resident}")
        print(f"Taille partagée : {self.share}")
        print(f"Taille du segment de texte : {self.text}")
        print(f"Taille de la bibliothèque : {self.lib}")
        print(f"Taille des données : {self.data}")
        print(f"Taille du segment de données : {self.dt}")
