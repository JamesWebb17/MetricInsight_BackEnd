"""
@package routes
@file metricInsight.py
@brief This file is the entry point for the MetricInsight program. It defines the routes and the functions to start and stop the program.
@details The program is started and stopped using the start and stop routes. The data is sent to the client using the get_data routes.
@version 1.0
@date 2024-02-12
"""

# Import the required packages
import json
import time

from flask import Blueprint, jsonify, request, Response

import threading
import queue
from copy import deepcopy

from MetricInsight.GPU.utilisation import web_utilisation_gpu
from MetricInsight.Memory.utilisation import web_utilisation_all_memory, web_utilisation_memory
from MetricInsight.Power.utilisation import web_tilisation_power
from MetricInsight.CPU.utilisation import web_utilisation_cpu, web_utilisation_cpus
from MetricInsight.Shared import flags

# Global variables
global shared_queues

# Create the blueprint
MetricInsight_blueprint = Blueprint('MetricInsight', __name__, url_prefix='/MetricInsight')


def get_data(name):
    """
    Send data to the client
    :param name: name of the queue
    :return:
    """
    time.sleep(1)
    while True:
        data, flag = conso(shared_queues[name])
        time.sleep(1)
        if flag:
            yield f'data: {json.dumps({"data": data})}\n\n'
        else:
            yield f'data: {json.dumps({"data": data})}\n\n'
            yield f'data: {json.dumps({"end": -1})}\n\n'
            break


@MetricInsight_blueprint.route('/get_data/GPU', methods=['GET'])
def get_data_GPU():
    """
    Sending GPU data to the client
    :return: Data for the client
    """
    return Response(get_data('GPU'), mimetype='text/event-stream')


@MetricInsight_blueprint.route('/get_data/Memory', methods=['GET'])
def get_data_Memory():
    """
    Sending Memory data to the client
    :return: Data for the client
    """
    return Response(get_data('MEM'), mimetype='text/event-stream')


@MetricInsight_blueprint.route('/get_data/Memory_PID', methods=['GET'])
def get_data_Memory_PID():
    """
    Sending Memory_PID data to the client
    :return: Data for the client
    """
    return Response(get_data('MEM'), mimetype='text/event-stream')


@MetricInsight_blueprint.route('/get_data/CPU_PID', methods=['GET'])
def get_data_CPU_PID():
    """
    Sending CPU_PID data to the client
    :return: Data for the client
    """
    return Response(get_data('CPU'), mimetype='text/event-stream')

@MetricInsight_blueprint.route('/get_data/CPU', methods=['GET'])
def get_data_CPU():
    """
    Sending CPU data to the client
    :return: Data for the client
    """
    return Response(get_data('CPU'), mimetype='text/event-stream')


@MetricInsight_blueprint.route('/get_data/Power', methods=['GET'])
def get_data_Power():
    """
    Sending Power data to the client
    :return: Data for the client
    """
    return Response(get_data('POWER'), mimetype='text/event-stream')


@MetricInsight_blueprint.route('/start', methods=['POST'])
def start():
    """
    Start the MetricInsight program
    :return: Response to the client (acknowledgement : True or False)
    """

    flags.END_FLAG = False
    data_received = request.get_json()

    # Get the configuration and set default values if not present
    pid_checkbox_value = data_received.get('pidCheckbox', False)
    pid_value = data_received.get('pidInput', 0)

    gpu_checkbox_value = data_received.get('gpuCheckbox', False)
    cpu_checkbox_value = data_received.get('cpuCheckbox', False)
    mem_checkbox_value = data_received.get('memoryCheckbox', False)
    power_checkbox_value = data_received.get('powerCheckbox', False)

    freq_checkbox_value = data_received.get('freqCheckbox', False)
    freq_value = data_received.get('FreqInput', 10)

    interval_checkbox_value = data_received.get('intervalCheckbox', False)
    interval_value = data_received.get('IntervalInput', -1)

    smoothing_checkbox_value = data_received.get('smoothingCheckbox', False)
    smoothing_value = data_received.get('SmoothingInput', 1)

    # Create the configuration
    configuration = {
        'pidCheckbox': pid_checkbox_value,
        'pidInput': pid_value,
        'gpuCheckbox': gpu_checkbox_value,
        'cpuCheckbox': cpu_checkbox_value,
        'memoryCheckbox': mem_checkbox_value,
        'powerCheckbox': power_checkbox_value,
        'freqCheckbox': freq_checkbox_value,
        'FreqInput': freq_value,
        'intervalCheckbox': interval_checkbox_value,
        'IntervalInput': interval_value,
        'smoothingCheckbox': smoothing_checkbox_value,
        'SmoothingInput': smoothing_value,
    }

    # Check if the configuration is valid
    if (configuration['cpuCheckbox'] or configuration['gpuCheckbox'] or configuration['memoryCheckbox'] or
            configuration['powerCheckbox']):
        response_data = {'acknowledgement': True}
        print('Lancement de MetricInsight...')
        MetricInsight(configuration)
    else:
        response_data = {'acknowledgement': False}

    print('Data send :', response_data)

    return jsonify(response_data)


@MetricInsight_blueprint.route('/stop', methods=['POST'])
def stop():
    """
    Stop the MetricInsight program
    :return: Response to the client (acknowledgement : True or False)
    """

    print('Arrêt de MetricInsight...')
    flags.END_FLAG = True
    return jsonify({'acknowledgement': True})


def MetricInsight(configuration):
    """
    Start the different threads for the MetricInsight program
    :param configuration:
    :return:
    """

    MAX_QUEUE_SIZE = int(configuration['FreqInput']) * 10

    global shared_queues

    shared_queues = {}
    threads = {}

    # Create the threads depending on the configuration
    if configuration['gpuCheckbox']:
        shared_queues['GPU'] = queue.Queue(MAX_QUEUE_SIZE)
        threads['thread_GPU'] = threading.Thread(target=web_utilisation_gpu, args=(shared_queues['GPU'], configuration))

    if configuration['powerCheckbox']:
        shared_queues['POWER'] = queue.Queue(MAX_QUEUE_SIZE)
        threads['thread_POWER'] = threading.Thread(target=web_tilisation_power,
                                                   args=(shared_queues['POWER'], configuration))

    if configuration['pidCheckbox']:
        if configuration['cpuCheckbox']:
            shared_queues['CPU'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_CPU'] = threading.Thread(target=web_utilisation_cpu,
                                                     args=(shared_queues['CPU'], configuration))
        if configuration['memoryCheckbox']:
            shared_queues['MEM'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_MEM'] = threading.Thread(target=web_utilisation_memory,
                                                     args=(shared_queues['MEM'], configuration))
    else:
        if configuration['cpuCheckbox']:
            shared_queues['CPU'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_CPU'] = threading.Thread(target=web_utilisation_cpus, args=(shared_queues['CPU'], configuration))
        if configuration['memoryCheckbox']:
            shared_queues['MEM'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_MEM'] = threading.Thread(target=web_utilisation_all_memory,
                                                     args=(shared_queues['MEM'], configuration))

    # Start threads
    for t in threads:
        threads[t].start()


def conso(queueP):
    """
    Consume the queue
    :param queueP:
    :return: List of data and flag (True if the program is still running, False if the program is finished)
    """
    L = []

    # Copy of the queue
    with queueP.mutex:
        queue_copy = deepcopy(queueP.queue)

    # Consume the queue
    for item in queue_copy:
        queueP.get()

        # If the item is "END", the program is finished
        if item == "END":
            print("Le producteur a terminé. Fin du traitement.")
            return L, False
        L.append(item)

    return L, True
