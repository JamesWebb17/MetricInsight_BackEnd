""" @package PID
Documentation for gpu module.

More details.
Class for reading gpu files and create object GPU.
"""


class GPU:
    """ Documentation for GPU class

    More details.
    Class which is used to represent lines containing GPU statistics in the /sys/devices/gpu.0/load file.
    """

    def __init__(self, load=0, name="gpu.0"):
        """
        The constructor for GPU class.
        :param name: name of the gpu
        :param load: load of the gpu
        """

        self.name = name
        self.load = load

    def __str__(self):
        """
        Return a string representation of the GPU object.
        :return: the string representation of the GPU object
        """

        return (
            f"Name: {self.name}\n"
            f"Load: {self.load}\n"
        )

    def read(self):
        """
        Read the /sys/devices/gpu.0/load file.
        :return:
        """

        try:
            with open("/sys/devices/gpu.0/load", "r") as file:
                self.load = int(file.readline())
        except FileNotFoundError:
            print(f"Le fichier /sys/devices/gpu.0/load n'existe pas.")
            return -1
