"""!
@brief Documentation for GPU file class.

@section package File Information
- package : PID
- name : gpu.py

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


class GPU:
    """!
    Documentation for GPU class

    @details Class which is used to represent lines containing GPU statistics in the /sys/devices/gpu.0/load file.
    """

    def __init__(self, load=0, name="gpu.0"):
        """!
        The constructor for GPU class.
        @param name: name of the gpu
        @param load: load of the gpu
        """

        ## The name of the GPU
        self.name = name

        ## The load of the GPU
        self.load = load

    def __str__(self):
        """!
        Override the string representation of the GPU object
        @return the string representation of the GPU object
        """

        return (
            f"Name: {self.name}\n"
            f"Load: {self.load}\n"
        )

    def read(self):
        """!
        Read the /sys/devices/gpu.0/load file.
        @return the status of the function (0 if successful, -1 otherwise)
        """

        try:
            with open("/sys/devices/gpu.0/load", "r") as file:
            #with open("./MetricInsight/Files/gpu.0/load", "r") as file:

                self.load = int(file.readline())
        except FileNotFoundError:
            print(f"Le fichier /sys/devices/gpu.0/load n'existe pas.")
            return -1
