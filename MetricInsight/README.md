# Overview

This project is a tools like top, htop, etc. command in linux. 
It finds the utilisation of the CPU, the memory and the power of a particular process.

This project is made in python 3.8.5.

This project is only made for Nvidia JetSon on linux distribution (for the moment).

This project is made by : Faucher Simon

Version : 1.0

# Summary

* [Contents](#contents)
  * [Sources files and folders](#sources-files-and-folders)
      * [Sources files](#sources-files)
      * [Sources folders](#sources-folders)
* [Installation](#installation)
  * [Requirements](#requirements)
  * [Run the project](#run-the-project)

## Contents

### Sources files and folders

#### Sources files
* [main.py](./MetricInsight.py) : Main file to run the project

#### Sources folders
* [Arguments](./Arguments) : Folder containing the arguments module
* [Read File](./Read_File) : Folder containing the read_file module
* [CPU](./CPU) : Folder containing the CPU module
* [Memory](./Memory) : Folder containing the memory module
* [Power](./Power) : Folder containing the power module


## Installation

### Requirements
csv : `pip install csv`

threading : `pip install threading`

matplotlib : `pip install matplotlib`

time : `pip install time`

argparse : `pip install argparse`

### Run the project
For run this project you need to have sudo rights. They are needed for the power module, to access to the power of the process.

run the main.py file with the command :`sudo python main.py -p PID [option]` in the terminal.

#### Options are :
* Help :
  * -h / --help :  Print help message and exit
  * -v / --verbose : Activates verbose mode
  
* Obligatory :
  * -p / --pid : PID of the process to be inspected

* Optionnal :
  * -cpu / -- cpu : Displays CPU usage
  * -mem / --memory : Displays memory usage
  * -pow / --power  : Displays power usage
  * -a / --all : Displays all usage
  * -f / --frequency :  Sampling frequency in seconds
  * -n / --number : Number of samples
  * -plot / --plot : Displays graphics
  * -s / --save : Write the data in files

