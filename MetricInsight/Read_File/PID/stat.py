"""!
@brief Documentation for proc/[PID]/stat file.

@section package File Information
- package : PID
- name : stat.py

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


class Stat:
    """!
    Documentation for Stat class

    @details The Stat class is used to read the /proc/[PID]/stat file and store the values in an object.
    """
    def __init__(self, pid):
        """!
        The constructor for Stat class.
        @param pid : pid of the process
        """

        ## PID of the process
        self.pid = pid

        ## Name of the process
        self.name = ""

        ## State of the process
        self.state = ""

        ## PID of the parent process
        self.ppid = 0

        ## Group ID of the process
        self.pgrp = 0

        ## ID of the session
        self.session = 0

        ## Number of the controlling terminal
        self.tty_nr = 0

        ## Group ID of the controlling terminal
        self.tpgid = 0

        ## Flags of the process
        self.flags = 0

        ## Page of minor faults
        self.minflt = 0

        ## Page of minor faults of the child
        self.cminflt = 0

        ## Page of major faults
        self.majflt = 0

        ## Page of major faults of the child
        self.cmajflt = 0

        ## Time of user (jiffies)
        self.utime = 0

        ## Time of system (jiffies)
        self.stime = 0

        ## Time of user of the child (jiffies)
        self.cutime = 0

        ## Time of system of the child (jiffies)
        self.cstime = 0

        ## Priority
        self.priority = 0

        ## Nice value
        self.nice = 0

        ## Number of threads
        self.num_threads = 0

        ## Value of the real timer
        self.itrealvalue = 0

        ## Start time (jiffies)
        self.starttime = 0

        ## Virtual size in bytes
        self.vsize = 0

        ## Resident size in pages
        self.rss = 0

        ## Limits of the processor in octets
        self.rsslim = [0, 0]

        ## Start address of the code
        self.startcode = 0

        ## End address of the code
        self.endcode = 0

        ## Start address of the stack
        self.startstack = 0

        ## Current stack pointer of the kernel
        self.kstkesp = 0

        ## Instruction pointer of the kernel stack
        self.kstkeip = 0

        ## Mask of signals pending
        self.signal = 0

        ## Mask of blocked signals
        self.blocked = 0

        ## Mask of ignored signals
        self.sigignore = 0

        ## Mask of signals caught
        self.sigcatch = 0

        ## Location of the system (if dormant)
        self.wchan = 0

        ## Number of pages swapped
        self.nswap = 0

        ## Number of pages swapped of the child
        self.cnswap = 0

        ## Exit signal of the process
        self.exit_signal = 0

        ## Last processor executed
        self.processor = 0

        ## Real-time scheduling priority
        self.rt_priority = 0

        ## Scheduling policy
        self.policy = 0

        ## Cumul of input and output delays, measured in top clock (hundredth of a second)
        self.delayacct_blkio_ticks = 0

        ## Time of user of the guest (jiffies)
        self.cguest_time = 0

    def read_proc_stat(self):
        """!
        Read the values of the Stat object.
        @return status : -1 if the file does not exist
        """

        pid = self.pid

        try:
            with open(f'/proc/{pid}/stat') as f:
            #with open(f'./MetricInsight/Files/21863/stat.txt') as f:
                data = f.read().split()
                if len(data) >= 44:  # Assurez-vous que suffisamment de données ont été lues
                    self.name = data[1][1:-1]  # Nom du processus sans les parenthèses
                    self.state = data[2]
                    self.ppid = int(data[3])
                    self.pgrp = int(data[4])
                    self.session = int(data[5])
                    self.tty_nr = int(data[6])
                    self.tpgid = int(data[7])
                    self.flags = int(data[8])
                    self.minflt = int(data[9])
                    self.cminflt = int(data[10])
                    self.majflt = int(data[11])
                    self.cmajflt = int(data[12])
                    self.utime = int(data[13])
                    self.stime = int(data[14])
                    self.cutime = int(data[15])
                    self.cstime = int(data[16])
                    self.priority = int(data[17])
                    self.nice = int(data[18])
                    self.num_threads = int(data[19])
                    self.itrealvalue = int(data[20])
                    self.starttime = int(data[21])
                    self.vsize = int(data[22])
                    self.rss = int(data[23])
                    self.rsslim = [int(data[24]), int(data[25])]
                    self.startcode = int(data[26])
                    self.endcode = int(data[27])
                    self.startstack = int(data[28])
                    self.kstkesp = int(data[29])
                    self.kstkeip = int(data[30])
                    self.signal = int(data[31])
                    self.blocked = int(data[32])
                    self.sigignore = int(data[33])
                    self.sigcatch = int(data[34])
                    self.wchan = int(data[35])
                    self.nswap = int(data[36])
                    self.cnswap = int(data[37])
                    self.exit_signal = int(data[38])
                    self.processor = int(data[39])
                    self.rt_priority = int(data[40])
                    self.policy = int(data[41])
                    self.delayacct_blkio_ticks = int(data[42])
                    self.cguest_time = int(data[43])
        except FileNotFoundError:
            print(f"Le fichier /proc/{pid}/stat n'existe pas.")
            return -1

    def display_info(self):
        """!
        Display the values of the Stat object.
        """

        print(f"Nom du processus : {self.name}")
        print(f"État du processus : {self.state}")
        print(f"PID du parent : {self.ppid}")
        print(f"Groupe de processus : {self.pgrp}")
        print(f"ID de session : {self.session}")
        print(f"Numéro de terminal : {self.tty_nr}")
        print(f"Groupe de processus du terminal : {self.tpgid}")
        print(f"Drapeaux : {self.flags}")
        print(f"Pages de fautes mineures : {self.minflt}")
        print(f"Pages de fautes mineures de l'enfant : {self.cminflt}")
        print(f"Pages de fautes majeures : {self.majflt}")
        print(f"Pages de fautes majeures de l'enfant : {self.cmajflt}")
        print(f"Temps utilisateur (jiffies) : {self.utime}")
        print(f"Temps système (jiffies) : {self.stime}")
        print(f"Temps utilisateur de l'enfant (jiffies) : {self.cutime}")
        print(f"Temps système de l'enfant (jiffies) : {self.cstime}")
        print(f"Priorité : {self.priority}")
        print(f"Valeur de nice : {self.nice}")
        print(f"Nombre de threads : {self.num_threads}")
        print(f"Valeur de la minuterie réelle : {self.itrealvalue}")
        print(f"Heure de démarrage (jiffies) : {self.starttime}")
        print(f"Taille virtuelle en octets : {self.vsize}")
        print(f"Taille résidente en pages : {self.rss}")
        print(f"Limites du processeur en octets : {self.rsslim}")
        print(f"Adresse de départ du code : {self.startcode}")
        print(f"Adresse de fin du code : {self.endcode}")
        print(f"Adresse de départ de la pile : {self.startstack}")
        print(f"Espacement actuel de la pile du noyau : {self.kstkesp}")
        print(f"Pointeur d'instruction de la pile du noyau : {self.kstkeip}")
        print(f"Masque de signaux en attente : {self.signal}")
        print(f"Masque de signaux bloqués : {self.blocked}")
        print(f"Masque de signaux ignorés : {self.sigignore}")
        print(f"Masque de signaux attrapés : {self.sigcatch}")
        print(f"Emplacement du système (si dormant) : {self.wchan}")
        print(f"Nombre de pages échangées : {self.nswap}")
        print(f"Nombre de pages échangées de l'enfant : {self.cnswap}")
        print(f"Signal de sortie du processus : {self.exit_signal}")
        print(f"Dernier processeur exécuté : {self.processor}")
        print(f"Priorité d'ordonnancement en temps réel : {self.rt_priority}")
        print(f"Politique d'ordonnancement : {self.policy}")
        print(
            f"Cumul des délais d'entrées et sorties, mesuré en top horloge (centième de seconde) : {self.delayacct_blkio_ticks}")
        print(f"Temps utilisateur de l'invité (jiffies) : {self.cguest_time}")
