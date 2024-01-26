""" @package Arguments
Documentation for Arguments module.

More details.
Function for parsing arguments.
"""

import argparse


def usage():
    """
    Parse arguments.
    :return: arguments parsed
    """

    parser = argparse.ArgumentParser(description="Process performance monitoring program.", add_help=False)

    help = parser.add_argument_group(title="Help")
    optional = parser.add_argument_group(title="Optional arguments")
    display = parser.add_argument_group(title="Display options")

    # Help
    help.add_argument('-h', '--help',
                      action='help',
                      help='Print this help message and exit',
                      default=False)
    help.add_argument('-v', '--verbose',
                      action='store_true',
                      help='Activates verbose mode. Default: False',
                      default=False)

    # Optional
    optional.add_argument('-p', '--pid',
                          help='PID of the process to be inspected. Default: 0 (all processes)',
                          type=int,
                          required=False,
                          dest='PID',
                          default=0)
    optional.add_argument('-cpu', '--cpu',
                          help='Displays CPU usage. Default: False',
                          action='store_true',
                          dest='CPU',
                          default=False)
    optional.add_argument('-gpu', '--gpu',
                          help='Displays GPU usage. Default: False',
                          action='store_true',
                          dest='GPU',
                          default=False)
    optional.add_argument('-mem', '--memory',
                          help='Displays memory usage. Default: False',
                          action='store_true',
                          dest='MEM',
                          default=False)
    optional.add_argument('-pow', '--power',
                          help='Displays energy consumption. Default: False',
                          action='store_true',
                          dest='POWER',
                          default=False)
    optional.add_argument('-a', '--all',
                          help='Displays all information. Default: False',
                          action='store_true',
                          dest='ALL',
                          default=False)
    optional.add_argument('-f', '--frequency',
                          help='Number of points per second wanted. Default: 10',
                          type=int,
                          dest='Frequency',
                          default=10)
    optional.add_argument('-i', '--interval',
                          help='Time of inspection (in seconds). Default: infinite',
                          type=float,
                          dest='Interval',
                          default=float('inf'))
    optional.add_argument('-plot', '--plot',
                          help='Display graphics. Default: False',
                          action='store_true',
                          dest='Plot',
                          default=False)
    optional.add_argument('-smo', '--smoothing',
                          help='Smoothing of the graphics. This is the number of points used for the average. Default: 1',
                          type=int,
                          dest='Smoothing',
                          default=1)
    optional.add_argument('-s', '--save',
                          help='Writes all data to files; Default: False',
                          type=str,
                          dest='Save')
    optional.add_argument('-r', '--read',
                          help='Reads data from files; Default: None',
                          type=str,
                          dest='Read',
                          default=None)
    args = parser.parse_args()

    return args
