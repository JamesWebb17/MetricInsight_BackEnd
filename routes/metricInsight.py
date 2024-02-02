import json
import time

from flask import Blueprint, jsonify, request, Response

import threading
import queue
from copy import deepcopy

from MetricInsight.GPU.utilisation import web_utilisation_gpu
from MetricInsight.Memory.utilisation import web_utilisation_all_memory, web_utilisation_memory
from MetricInsight.Power.utilisation import web_tilisation_power
from MetricInsight.Shared import flags

global shared_queues

MetricInsight_blueprint = Blueprint('MetricInsight', __name__, url_prefix='/MetricInsight')


def get_data(name):
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
    return Response(get_data('GPU'), mimetype='text/event-stream')

@MetricInsight_blueprint.route('/get_data/Memory', methods=['GET'])
def get_data_Memory():
    return Response(get_data('MEM'), mimetype='text/event-stream')

@MetricInsight_blueprint.route('/get_data/Memory_PID', methods=['GET'])
def get_data_Memory_PID():
    return Response(get_data('MEM'), mimetype='text/event-stream')

@MetricInsight_blueprint.route('/get_data/Power', methods=['GET'])
def get_data_Power():
    return Response(get_data('POWER'), mimetype='text/event-stream')


@MetricInsight_blueprint.route('/start', methods=['POST'])
def start():
    flags.END_FLAG = False
    data_received = request.get_json()

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
    print('Arrêt de MetricInsight...')
    flags.END_FLAG = True
    return jsonify({'acknowledgement': True})

def MetricInsight(configuration):
    MAX_QUEUE_SIZE = int(configuration['FreqInput']) * 10

    global shared_queues

    shared_queues = {}
    threads = {}

    if configuration['gpuCheckbox']:
        shared_queues['GPU'] = queue.Queue(MAX_QUEUE_SIZE)
        threads['thread_GPU'] = threading.Thread(target=web_utilisation_gpu, args=(shared_queues['GPU'], configuration))

    if configuration['powerCheckbox']:
        shared_queues['POWER'] = queue.Queue(MAX_QUEUE_SIZE)
        threads['thread_POWER'] = threading.Thread(target=web_tilisation_power, args=(shared_queues['POWER'], configuration))

    if configuration['pidCheckbox']:
        if configuration['cpuCheckbox']:
            shared_queues['CPU'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_CPU'] = threading.Thread(target=conso, args=(shared_queues['CPU'], configuration))
        if configuration['memoryCheckbox']:
            shared_queues['MEM'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_MEM'] = threading.Thread(target=web_utilisation_memory, args=(shared_queues['MEM'], configuration))
    else :
        if configuration['cpuCheckbox']:
            shared_queues['CPU'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_CPU'] = threading.Thread(target=conso, args=(shared_queues['CPU'], configuration))
        if configuration['memoryCheckbox']:
            shared_queues['MEM'] = queue.Queue(MAX_QUEUE_SIZE)
            threads['thread_MEM'] = threading.Thread(target=web_utilisation_all_memory, args=(shared_queues['MEM'], configuration))


    # Start threads
    for t in threads:
        threads[t].start()


def conso(queueP):
    L = []

    # Copie & vide la queue
    with queueP.mutex:
        queue_copy = deepcopy(queueP.queue)

    # Vidange de la copie
    for item in queue_copy:
        queueP.get()

        # Vérifier si c'est le signal de fin
        if item == "END":
            print("Le producteur a terminé. Fin du traitement.")
            return L, False
        L.append(item)

    return L, True
