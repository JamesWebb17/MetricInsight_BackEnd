"""!
@brief Documentation for proc/meminfo file.

@section package File Information
- package : Read_File
- name : meminfo.py

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


class MemInfo:
    """!
    Documentation for MemInfo class

    @details The MemInfo class is used to read the /proc/meminfo file and store the values in an object.
    """

    def __init__(self):
        """!
        The constructor for MemInfo class.
        """

        ## Total usable RAM (i.e., physical RAM minus a few reserved bits and the kernel binary code)
        self.mem_total = 0

        ## Free memory in the system
        self.mem_free = 0

        ## An estimate of how much memory is available
        self.mem_available = 0

        ## Relatively temporary storage for raw disk blocks that shouldn't get tremendously large (20MB or so)
        self.buffers = 0

        ## In-memory cache for files read from the disk (the page cache)
        self.cached = 0

        ## Amount of swap space that is currently in use
        self.swap_cached = 0

        ## Memory that has been used more recently and usually not reclaimed unless absolutely necessary
        self.active = 0

        ## Memory which has been less recently used
        self.inactive = 0

        ## Memory that has been used more recently and usually not reclaimed unless absolutely necessary
        self.active_anon = 0

        ## Memory which has been less recently used
        self.inactive_anon = 0

        ## Memory that has been used more recently and usually not reclaimed unless absolutely necessary
        self.active_file = 0

        ## Memory which has been less recently used
        self.inactive_file = 0

        ## Memory that cannot be reclaimed
        self.unevictable = 0

        ## Memory that has been locked in memory
        self.mlocked = 0

        ## Total swap space
        self.swap_total = 0

        ## Swap space that is currently unused
        self.swap_free = 0

        ## Memory which is waiting to get written back to the disk
        self.dirty = 0

        ## Memory which is actively being written back to the disk
        self.writeback = 0

        ## Non-file backed pages mapped into user-space page tables
        self.anonPages = 0

        ## File-backed pages mapped into user-space page tables
        self.mapped = 0

        ## POSIX Shared Memory
        self.shmem = 0

        ## Kernel data structures
        self.slab = 0

        ## Part of the Slab that might be reclaimed, such as caches
        self.sreclaimable = 0

        ## Part of the Slab that cannot be reclaimed
        self.sunreclaim = 0

        ## Kernel stack
        self.kernelstack = 0

        ## Page tables
        self.pagetables = 0

        ## NFS pages sent to the server but not yet committed to stable storage
        self.nfs_unstable = 0

        ## Memory used for block device "bounce buffers"
        self.bounce = 0

        ## Memory used as a cache for files
        self.writebacktmp = 0

        ## The total amount of memory that the system can commit
        self.commitlimit = 0

        ## The total amount of memory currently committed to the system
        self.committed_as = 0

        ## Total size of vmalloc memory area
        self.vmaltotal = 0

        ## Amount of vmalloc area which is used
        self.vmallocused = 0

        ## Largest contiguous block of vmalloc area which is free
        self.vmallocchunk = 0

        ## Size of per-cpu memory area
        self.percpu = 0

        ## Memory that has been corrupted
        self.hardwarecorrupted = 0

        ## HugeTLB memory total
        self.anonhugepages = 0

        ## HugeTLB memory that is shared
        self.shmemhugepages = 0

        ## HugeTLB memory that is mapped into user space with VM_PFNMAP
        self.shmempmdmapped = 0

        ## HugeTLB memory that is file backed
        self.filehugepages = 0

        ## HugeTLB memory that is mapped into user space with VM_PFNMAP
        self.filepmdmapped = 0

        ## Total size of CMA memory area
        self.cmatotal = 0

        ## Amount of CMA memory which is free
        self.cmafree = 0

        ## HugeTLB memory total
        self.hugepages_total = 0

        ## HugeTLB memory that is free
        self.hugepages_free = 0

        ## HugeTLB memory that is reserved
        self.hugepages_rsvd = 0

        ## HugeTLB memory that is surplus
        self.hugepages_surp = 0

        ## HugeTLB memory page size
        self.hugetpagesize = 0

        ## HugeTLB memory that is free
        self.hugetlb = 0

    def read_meminfo(self):
        """!
        Read the values of the MemInfo object from the /proc/meminfo file.
        @return status of the read (0 if successful, -1 if not)
        """

        try:
            with open('/proc/meminfo') as f:
                for line in f:
                    key, value = line.split(':', 1)
                    if key == 'MemTotal':
                        self.mem_total = int(value.split()[0])
                    elif key == 'MemFree':
                        self.mem_free = int(value.split()[0])
                    elif key == 'MemAvailable':
                        self.mem_available = int(value.split()[0])
                    elif key == 'Buffers':
                        self.buffers = int(value.split()[0])
                    elif key == 'Cached':
                        self.cached = int(value.split()[0])
                    elif key == 'SwapCached':
                        self.swap_cached = int(value.split()[0])
                    elif key == 'Active':
                        self.active = int(value.split()[0])
                    elif key == 'Inactive':
                        self.inactive = int(value.split()[0])
                    elif key == 'Active(anon)':
                        self.active_anon = int(value.split()[0])
                    elif key == 'Inactive(anon)':
                        self.inactive_anon = int(value.split()[0])
                    elif key == 'Active(file)':
                        self.active_file = int(value.split()[0])
                    elif key == 'Inactive(file)':
                        self.inactive_file = int(value.split()[0])
                    elif key == 'Unevictable':
                        self.unevictable = int(value.split()[0])
                    elif key == 'Mlocked':
                        self.mlocked = int(value.split()[0])
                    elif key == 'SwapTotal':
                        self.swap_total = int(value.split()[0])
                    elif key == 'SwapFree':
                        self.swap_free = int(value.split()[0])
                    elif key == 'Dirty':
                        self.dirty = int(value.split()[0])
                    elif key == 'Writeback':
                        self.writeback = int(value.split()[0])
                    elif key == 'AnonPages':
                        self.anonPages = int(value.split()[0])
                    elif key == 'Mapped':
                        self.mapped = int(value.split()[0])
                    elif key == 'Shmem':
                        self.shmem = int(value.split()[0])
                    elif key == 'Slab':
                        self.slab = int(value.split()[0])
                    elif key == 'SReclaimable':
                        self.sreclaimable = int(value.split()[0])
                    elif key == 'SUnreclaim':
                        self.sunreclaim = int(value.split()[0])
                    elif key == 'KernelStack':
                        self.kernelstack = int(value.split()[0])
                    elif key == 'PageTables':
                        self.pagetables = int(value.split()[0])
                    elif key == 'NFS_Unstable':
                        self.nfs_unstable = int(value.split()[0])
                    elif key == 'Bounce':
                        self.bounce = int(value.split()[0])
                    elif key == 'WritebackTmp':
                        self.writebacktmp = int(value.split()[0])
                    elif key == 'CommitLimit':
                        self.commitlimit = int(value.split()[0])
                    elif key == 'Committed_AS':
                        self.committed_as = int(value.split()[0])
                    elif key == 'VmallocTotal':
                        self.vmaltotal = int(value.split()[0])
                    elif key == 'VmallocUsed':
                        self.vmallocused = int(value.split()[0])
                    elif key == 'VmallocChunk':
                        self.vmallocchunk = int(value.split()[0])
                    elif key == 'Percpu':
                        self.percpu = int(value.split()[0])
                    elif key == 'HardwareCorrupted':
                        self.hardwarecorrupted = int(value.split()[0])
                    elif key == 'AnonHugePages':
                        self.anonhugepages = int(value.split()[0])
                    elif key == 'ShmemHugePages':
                        self.shmemhugepages = int(value.split()[0])
                    elif key == 'ShmemPmdMapped':
                        self.shmempmdmapped = int(value.split()[0])
                    elif key == 'FileHugePages':
                        self.filehugepages = int(value.split()[0])
                    elif key == 'FilePmdMapped':
                        self.filepmdmapped = int(value.split()[0])
                    elif key == 'CmaTotal':
                        self.cmatotal = int(value.split()[0])
                    elif key == 'CmaFree':
                        self.cmafree = int(value.split()[0])
                    elif key == 'HugePages_Total':
                        self.hugepages_total = int(value.split()[0])
                    elif key == 'HugePages_Free':
                        self.hugepages_free = int(value.split()[0])
                    elif key == 'HugePages_Rsvd':
                        self.hugepages_rsvd = int(value.split()[0])
                    elif key == 'HugePages_Surp':
                        self.hugepages_surp = int(value.split()[0])
                    elif key == 'Hugepagesize':
                        self.hugetpagesize = int(value.split()[0])
                    elif key == 'Hugetlb':
                        self.hugetlb = int(value.split()[0])
        except FileNotFoundError:
            print("Le fichier /proc/meminfo n'existe pas.")
            return -1

    def __str__(self):
        """
        Return a string representation of the MemInfo object.
        @return the string representation of the MemInfo object
        """

        result_str = ""
        result_str += f"MemTotal: {self.mem_total} kB\n"
        result_str += f"MemFree: {self.mem_free} kB\n"
        result_str += f"MemAvailable: {self.mem_available} kB\n"
        result_str += f"Buffers: {self.buffers} kB\n"
        result_str += f"Cached: {self.cached} kB\n"
        result_str += f"SwapCached: {self.swap_cached} kB\n"
        result_str += f"Active: {self.active} kB\n"
        result_str += f"Inactive: {self.inactive} kB\n"
        result_str += f"Active(anon): {self.active_anon} kB\n"
        result_str += f"Inactive(anon): {self.inactive_anon} kB\n"
        result_str += f"Active(file): {self.active_file} kB\n"
        result_str += f"Inactive(file): {self.inactive_file} kB\n"
        result_str += f"Unevictable: {self.unevictable} kB\n"
        result_str += f"Mlocked: {self.mlocked} kB\n"
        result_str += f"SwapTotal: {self.swap_total} kB\n"
        result_str += f"SwapFree: {self.swap_free} kB\n"
        result_str += f"Dirty: {self.dirty} kB\n"
        result_str += f"Writeback: {self.writeback} kB\n"
        result_str += f"AnonPages: {self.anonPages} kB\n"
        result_str += f"Mapped: {self.mapped} kB\n"
        result_str += f"Shmem: {self.shmem} kB\n"
        result_str += f"Slab: {self.slab} kB\n"
        result_str += f"SReclaimable: {self.sreclaimable} kB\n"
        result_str += f"SUnreclaim: {self.sunreclaim} kB\n"
        result_str += f"KernelStack: {self.kernelstack} kB\n"
        result_str += f"PageTables: {self.pagetables} kB\n"
        result_str += f"NFS_Unstable: {self.nfs_unstable} kB\n"
        result_str += f"Bounce: {self.bounce} kB\n"
        result_str += f"WritebackTmp: {self.writebacktmp} kB\n"
        result_str += f"CommitLimit: {self.commitlimit} kB\n"
        result_str += f"Committed_AS: {self.committed_as} kB\n"
        result_str += f"VmallocTotal: {self.vmaltotal} kB\n"
        result_str += f"VmallocUsed: {self.vmallocused} kB\n"
        result_str += f"VmallocChunk: {self.vmallocchunk} kB\n"
        result_str += f"Percpu: {self.percpu} kB\n"
        result_str += f"HardwareCorrupted: {self.hardwarecorrupted} kB\n"
        result_str += f"AnonHugePages: {self.anonhugepages} kB\n"
        result_str += f"ShmemHugePages: {self.shmemhugepages} kB\n"
        result_str += f"ShmemPmdMapped: {self.shmempmdmapped} kB\n"
        result_str += f"FileHugePages: {self.filehugepages} kB\n"
        result_str += f"FilePmdMapped: {self.filepmdmapped} kB\n"
        result_str += f"CmaTotal: {self.cmatotal} kB\n"
        result_str += f"CmaFree: {self.cmafree} kB\n"
        result_str += f"HugePages_Total: {self.hugepages_total} kB\n"
        result_str += f"HugePages_Free: {self.hugepages_free} kB\n"
        result_str += f"HugePages_Rsvd: {self.hugepages_rsvd} kB\n"
        result_str += f"HugePages_Surp: {self.hugepages_surp} kB\n"
        result_str += f"Hugepagesize: {self.hugetpagesize} kB\n"
        result_str += f"Hugetlb: {self.hugetlb} kB\n"
        return result_str
