""" @package PID
Documentation for statm module.

More details.
Class for reading hwmon files and create object Statm.
"""


class Statm:

    def __init__(self, pid):
        """
        The constructor for Statm class.
        :param pid: pid of the process
        """

        self.pid = pid
        self.size = 0
        self.resident = 0
        self.share = 0
        self.text = 0
        self.lib = 0
        self.data = 0
        self.dt = 0

    def read_proc_statm(self):
        """
        Read the values of the Statm object.
        :return:
        """

        pid = self.pid
        try:
            with open(f'/proc/{pid}/statm') as f:
            #with open(f'./Files/21863/statm.txt') as f:
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
        """
        Display the values of the Statm object.
        :return:
        """

        print(f"Taille totale : {self.size}")
        print(f"Taille résidente : {self.resident}")
        print(f"Taille partagée : {self.share}")
        print(f"Taille du segment de texte : {self.text}")
        print(f"Taille de la bibliothèque : {self.lib}")
        print(f"Taille des données : {self.data}")
        print(f"Taille du segment de données : {self.dt}")
