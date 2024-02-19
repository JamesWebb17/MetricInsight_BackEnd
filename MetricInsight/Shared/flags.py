"""!
@brief Documentation for flags file.

@section package File Information
- package : Shared
- name : flags.py

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


##flag that indicates if the verbose mode is activated or not.
VERBOSE_MODE_FLAG = False


##flag that indicates if the thread for the CPU is running or not.
THREAD_CPU_END_FLAG = False


##flag that indicates if the thread for the MEM is running or not.
THREAD_MEM_END_FLAG = False

##flag that indicates if the thread for the POWER is running or not.
THREAD_POWER_END_FLAG = False

##flag that indicates if the thread for the GPU is running or not.
THREAD_GPU_END_FLAG = False

##flag that indicates to all threads to stop.
END_FLAG = False

